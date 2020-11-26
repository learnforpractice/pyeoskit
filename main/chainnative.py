from . import _eosapi

class ChainNative(object):

    @staticmethod
    def n2s(n):
        return _eosapi.n2s(n)

    @staticmethod
    def s2n(s):
        return _eosapi.s2n(s)

    @staticmethod
    def string_to_symbol(precision, str_symbol):
        return _eosapi.string_to_symbol(precision, str_symbol)

    @staticmethod
    def pack_args(account, action, args):
        return _eosapi.pack_args(account, action, args)

    @staticmethod
    def unpack_args(account, action, binargs):
        return _eosapi.unpack_args(account, action, binargs)

    @staticmethod
    def clear_abi_cache(account):
        return _eosapi.clear_abi_cache(account)

    @staticmethod
    def set_abi(account, abi):
        return _eosapi.set_abi(account, abi)

    @staticmethod
    def pack_abi(abi):
        return _eosapi.pack_abi(abi)

    @staticmethod
    def gen_transaction(actions, expiration, reference_block_id):
        return _eosapi.gen_transaction(actions, expiration, reference_block_id)

    @staticmethod
    def sign_transaction(trx, private_key, chain_id):
        if isinstance(trx, dict):
            trx = json.loads(trx)
        return _eosapi.sign_transaction(trx, private_key, chain_id)

    @staticmethod
    def pack_transaction(trx, compress=0):
        return _eosapi.pack_transaction(trx, compress)

    @staticmethod
    def unpack_transaction(trx):
        return _eosapi.unpack_transaction(trx)

    @staticmethod
    def create_key():
        return _eosapi.create_key()

    @staticmethod
    def get_public_key(priv):
        return _eosapi.get_public_key(priv)

    @staticmethod
    def from_base58(pub_key):
        return _eosapi.from_base58(pub_key)

    @staticmethod
    def to_base58(raw_pub_key):
        return _eosapi.to_base58(raw_pub_key)

    @staticmethod
    def recover_key(digest, sign):
        return _eosapi.recover_key(digest, sign)

    @staticmethod
    def pack_cpp_object(obj_type, json_str):
        return _eosapi.pack_cpp_object(obj_type, json_str)

    @staticmethod
    def unpack_cpp_object(obj_type, raw_data):
        return _eosapi.unpack_cpp_object(obj_type, raw_data)

    @staticmethod
    def sign_digest(priv_key, digest):
        if isinstance(digest, str):
            if not len(digest) == 64:
                raise Exception('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
            digest = bytes.fromhex(digest)
        elif isinstance(digest, bytes):
            if not len(digest) == 32:
                raise Exception('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
        else:
            raise TypeError('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
        return _eosapi.sign_digest(priv_key, digest)

    @staticmethod
    def set_public_key_prefix(prefix):
        _eosapi.set_public_key_prefix(prefix)

    @staticmethod
    def get_public_key_prefix():
        return _eosapi.get_public_key_prefix()

    @staticmethod
    def compile(src):
        return _eosapi.compile_py(src)

