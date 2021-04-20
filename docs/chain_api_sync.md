# ChainApiSync

## create_key

## n2s
```
@staticmethod
def n2s(n):
```

## s2n
```
@staticmethod
def s2n(s):
```

## s2b
```
@staticmethod
def s2b(s):
```

## b2s
```
@staticmethod
def b2s(b):
```

    @staticmethod
    def string_to_symbol(precision, str_symbol):
        return _uuosapi.string_to_symbol(precision, str_symbol)

    @staticmethod
    def pack_args(account, action, args):
        ret = _uuosapi.pack_args(account, action, args)
        return check_result(ret)

    @staticmethod
    def unpack_args(account, action, binargs):
        if isinstance(binargs, str):
            binargs = bytes.fromhex(binargs)
        ret = _uuosapi.unpack_args(account, action, binargs)
        return check_result(ret)

    @staticmethod
    def pack_abi_type(account, struct_name, args):
        if isinstance(args, dict):
            args = json.dumps(args)
        return _uuosapi.pack_abi_type(account, struct_name, args)

    @staticmethod
    def unpack_abi_type(account, struct_name, binargs):
        return _uuosapi.unpack_abi_type(account, struct_name, binargs)

    @staticmethod
    def clear_abi_cache(account):
        return _uuosapi.clear_abi_cache(account)

    @staticmethod
    def set_abi(account, abi):
        ret = _uuosapi.set_abi(account, abi)
        return check_result(ret)

    @staticmethod
    def pack_abi(abi):
        if isinstance(abi, dict):
            abi = json.dumps(abi)
        return _uuosapi.pack_abi(abi)

    @staticmethod
    def unpack_abi(packed_abi):
        return _uuosapi.unpack_abi(packed_abi)

    @staticmethod
    def gen_transaction(actions, expiration, reference_block_id):
        r = _uuosapi.gen_transaction(actions, expiration, reference_block_id)
        return check_result(r)

    @staticmethod
    def sign_transaction(trx, private_key, chain_id):
        if isinstance(trx, dict):
            trx = json.loads(trx)
        ret = _uuosapi.sign_transaction(trx, private_key, chain_id)
        return check_result(ret)

    @staticmethod
    def pack_transaction(trx, compress=0):
        return _uuosapi.pack_transaction(trx, compress)

    @staticmethod
    def unpack_transaction(trx):
        return _uuosapi.unpack_transaction(trx)

    @staticmethod
    def create_key():
        return _uuosapi.create_key()

    @staticmethod
    def get_public_key(priv):
        return _uuosapi.get_public_key(priv)

    @staticmethod
    def from_base58(pub_key):
        return _uuosapi.from_base58(pub_key)

    @staticmethod
    def to_base58(raw_pub_key):
        return _uuosapi.to_base58(raw_pub_key)

    @staticmethod
    def recover_key(digest, sign):
        return _uuosapi.recover_key(digest, sign)

    @staticmethod
    def pack_cpp_object(obj_type, json_str):
        return _uuosapi.pack_cpp_object(obj_type, json_str)

    @staticmethod
    def unpack_cpp_object(obj_type, raw_data):
        return _uuosapi.unpack_cpp_object(obj_type, raw_data)

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
        return _uuosapi.sign_digest(priv_key, digest)

    @staticmethod
    def set_public_key_prefix(prefix):
        _uuosapi.set_public_key_prefix(prefix)

    @staticmethod
    def get_public_key_prefix():
        return _uuosapi.get_public_key_prefix()

    @staticmethod
    def mp_compile(contract, src):
        return _uuosapi.compile_py(contract, src)

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

    def compile(self, contract_name, code, vm_type):
        if vm_type == 0:
            return wasmcompiler.compile_cpp_src(contract_name, code)
        elif vm_type == 1:
            code = self.mp_compile(contract_name, code)
            assert code
            return self.mp_make_frozen(code)
        else:
            assert 0, f'unsupported vm type: {vm_type}'

    @staticmethod
    def get_last_error():
        return _uuosapi.get_last_error()
