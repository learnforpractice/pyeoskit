import time
import json
import httpx

from . import _pyeoskit
from . import wasmcompiler
from .exceptions import ChainException
from . import ABI
from .common import check_result
from . import crypto
from .transaction import Transaction

SRC_TYPE_CPP = 0
SRC_TYPE_PY = 1
SRC_TYPE_GO = 2

class ChainNative(object):

    def get_abi_sync(self, account):
        args = {
            'account_name': account
        }
        r = httpx.post(f'{self.node_url}/v1/chain/get_abi', json=args)
        try:
            r = r.json()
        except json.decoder.JSONDecodeError:
            return ''

        try:
            abi = r['abi']
            return json.dumps(abi)
        except KeyError:
            return ''

    @staticmethod
    def n2s(n):
        '''convert integer to name string
        Example:
        ```python
            from pyeoskit import eosapi
            s = eosapi.n2s(10927537166380695552)
            print(s)
        ```
        ```
            'myname'
        ```
        '''
        return _pyeoskit.n2s(n)

    @staticmethod
    def s2n(s):
        n = _pyeoskit.s2n(s)
        if not _pyeoskit.n2s(n) == s:
            return 0
        return n

    @staticmethod
    def s2b(s):
        n = _pyeoskit.s2n(s)
        return int.to_bytes(n, 8, 'little')

    @staticmethod
    def b2s(b):
        n = int.from_bytes(b, 'little')
        return _pyeoskit.n2s(n)

    @staticmethod
    def string_to_symbol(sym):
        try:
            precision, str_sym = sym.split(',')
            print('++++++++:', precision, str_sym)
            return _pyeoskit.sym2n(str_sym, int(precision))
        except Exception as e:
            print(e)
            return 0

    def check_abi(self, account):
        if not ABI.is_abi_cached(account):
            abi = self.get_abi_sync(account)
            self.set_abi(account, abi.encode('utf8'))

    def pack_args(self, account, action, args):
        if isinstance(args, dict):
            args = json.dumps(args)
        else:
            assert isinstance(args, (str, bytes))

        self.check_abi(account)

        binargs = ABI.pack_action_args(account, action, args)
        return bytes.fromhex(binargs)

    def unpack_args(self, account, action, binargs, json=False):
        if isinstance(binargs, bytes):
            binargs = binargs.hex()

        self.check_abi(account)

        return ABI.unpack_action_args(account, action, binargs)

    def pack_abi_type(self, account, struct_name, args):
        if isinstance(args, dict):
            args = json.dumps(args)

        self.check_abi(account)

        return ABI.pack_abi_type(account, struct_name, args)

    def unpack_abi_type(self, account, struct_name, binargs):
        self.check_abi(account)
        return ABI.unpack_abi_type(account, struct_name, binargs)

    @staticmethod
    def clear_abi_cache(account):
        return ABI.set_contract_abi(account, "")

    @staticmethod
    def set_abi(account, abi):
        if isinstance(abi, str):
            abi = abi.encode('utf8')
        return ABI.set_contract_abi(account, abi)

    @staticmethod
    def pack_abi(abi):
        if isinstance(abi, dict):
            abi = json.dumps(abi)
        return ABI.pack_abi(abi)

    @staticmethod
    def unpack_abi(packed_abi):
        return ABI.unpack_abi(packed_abi)

    def gen_transaction(self, actions, expiration, reference_block_id, chain_id):
        if not expiration:
            expiration = int(time.time()) + 60
        else:
            expiration = int(time.time()) + expiration

        tx = Transaction(expiration, reference_block_id, chain_id)
        for a in actions:
            contract, action_name, args, permissions = a
            if isinstance(args, bytes):
                args = args.hex()
            elif isinstance(args, dict):
                args = json.dumps(args)
            elif isinstance(args, str):
                pass
            else:
                tx.free()
                raise Exception('Invalid args type')
            permissions = json.dumps(permissions)
            self.check_abi(contract)
            tx.add_action(contract, action_name, args, permissions)

        try:
            return tx.marshal()
        finally:
            tx.free()

    def generate_transaction(self, actions, expiration, reference_block_id, chain_id):
        return self.gen_transaction(actions, expiration, reference_block_id, chain_id)

    @staticmethod
    def sign_transaction(tx, private_key, chain_id, json=False):
        t = Transaction.from_json(tx, chain_id)
        return t.sign_by_private_key(private_key)

    @staticmethod
    def pack_transaction(tx, compress=0, json=False):
        t = Transaction.from_json(tx, '00'*32)
        r = t.pack(compress)
        return r['packed_trx']

    @staticmethod
    def unpack_transaction(trx, json=False):
        return Transaction.unpack(trx)

    @staticmethod
    def create_key():
        return crypto.create_key()

    @staticmethod
    def get_public_key(priv, eos_pub = True):
        ret = _pyeoskit.crypto_get_public_key(priv, eos_pub)
        return check_result(ret)

    @staticmethod
    def recover_key(digest, sign):
        ret = _pyeoskit.crypto_recover_key(digest, sign)
        return check_result(ret)

    @staticmethod
    def sign_digest(digest, priv_key):
        if isinstance(digest, bytes):
            digest = digest.hex()
        ret = _pyeoskit.crypto_sign_digest(digest, priv_key)
        return check_result(ret)

    @staticmethod
    def mp_compile(contract, src):
        return _eosapi.compile_py(contract, src)

    def mp_make_frozen(self, code):
        mpy_code = ((code, len(code)),)

        code_region = b''
        code_size_region = b''
        for code, size in mpy_code:
            code_region += code
            code_size_region += int.to_bytes(size, 4, 'little')

        name_region = b'main.mpy\x00'

        region_sizes = b''
        region_sizes += int.to_bytes(len(name_region), 4, 'little')
        region_sizes += int.to_bytes(len(code_size_region), 4, 'little')
        region_sizes += int.to_bytes(len(code_region), 4, 'little')

        header = int.to_bytes(5, 4, 'little')
        header += bytearray(60)
        frozen_code = header + region_sizes + name_region + code_size_region + code_region
        return frozen_code

    def compile(self, contract_name, code, src_type=SRC_TYPE_CPP):
        '''
        :param contract_name: contract name
        :param code: source code
        :param src_type: 0: py, 1: cpp 2: go
        :return: bytecode and abi
        '''
        if src_type == SRC_TYPE_CPP:
            code = wasmcompiler.compile_cpp_src(contract_name, code)
            return code, None
        elif src_type == SRC_TYPE_PY:
            code = self.mp_compile(contract_name, code)
            assert code
            return self.mp_make_frozen(code), None
        elif src_type == SRC_TYPE_GO:
            return wasmcompiler.compile_go_src(contract_name, code)
        else:
            assert 0, f'unsupported file type: {src_type}'

    @staticmethod
    def set_debug_flag(debug):
        _pyeoskit.set_debug_flag_(debug)

    @staticmethod
    def get_debug_flag() -> bool:
        return _pyeoskit.get_debug_flag_()
