# ChainNative

> Auto-generated documentation for [pysrc.chainnative](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / ChainNative
    - [ChainNative](#chainnative)
        - [ChainNative.b2s](#chainnativeb2s)
        - [ChainNative.clear_abi_cache](#chainnativeclear_abi_cache)
        - [ChainNative().compile](#chainnativecompile)
        - [ChainNative.create_key](#chainnativecreate_key)
        - [ChainNative.from_base58](#chainnativefrom_base58)
        - [ChainNative.gen_transaction](#chainnativegen_transaction)
        - [ChainNative.get_last_error](#chainnativeget_last_error)
        - [ChainNative.get_public_key](#chainnativeget_public_key)
        - [ChainNative.get_public_key_prefix](#chainnativeget_public_key_prefix)
        - [ChainNative.mp_compile](#chainnativemp_compile)
        - [ChainNative().mp_make_frozen](#chainnativemp_make_frozen)
        - [ChainNative.n2s](#chainnativen2s)
        - [ChainNative.pack_abi](#chainnativepack_abi)
        - [ChainNative.pack_abi_type](#chainnativepack_abi_type)
        - [ChainNative.pack_args](#chainnativepack_args)
        - [ChainNative.pack_cpp_object](#chainnativepack_cpp_object)
        - [ChainNative.pack_transaction](#chainnativepack_transaction)
        - [ChainNative.recover_key](#chainnativerecover_key)
        - [ChainNative.s2b](#chainnatives2b)
        - [ChainNative.s2n](#chainnatives2n)
        - [ChainNative.set_abi](#chainnativeset_abi)
        - [ChainNative.set_public_key_prefix](#chainnativeset_public_key_prefix)
        - [ChainNative.sign_digest](#chainnativesign_digest)
        - [ChainNative.sign_transaction](#chainnativesign_transaction)
        - [ChainNative.string_to_symbol](#chainnativestring_to_symbol)
        - [ChainNative.to_base58](#chainnativeto_base58)
        - [ChainNative.unpack_abi](#chainnativeunpack_abi)
        - [ChainNative.unpack_abi_type](#chainnativeunpack_abi_type)
        - [ChainNative.unpack_args](#chainnativeunpack_args)
        - [ChainNative.unpack_cpp_object](#chainnativeunpack_cpp_object)
        - [ChainNative.unpack_transaction](#chainnativeunpack_transaction)
    - [check_result](#check_result)
    - [raise_last_error](#raise_last_error)

## ChainNative

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L14)

```python
class ChainNative(object):
```

### ChainNative.b2s

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L40)

```python
@staticmethod
def b2s(b):
```

### ChainNative.clear_abi_cache

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L71)

```python
@staticmethod
def clear_abi_cache(account):
```

### ChainNative().compile

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L184)

```python
def compile(contract_name, code, vm_type):
```

### ChainNative.create_key

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L110)

```python
@staticmethod
def create_key():
```

### ChainNative.from_base58

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L118)

```python
@staticmethod
def from_base58(pub_key):
```

### ChainNative.gen_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L90)

```python
@staticmethod
def gen_transaction(actions, expiration, reference_block_id):
```

### ChainNative.get_last_error

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L194)

```python
@staticmethod
def get_last_error():
```

### ChainNative.get_public_key

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L114)

```python
@staticmethod
def get_public_key(priv):
```

### ChainNative.get_public_key_prefix

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L155)

```python
@staticmethod
def get_public_key_prefix():
```

### ChainNative.mp_compile

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L159)

```python
@staticmethod
def mp_compile(contract, src):
```

### ChainNative().mp_make_frozen

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L163)

```python
def mp_make_frozen(code):
```

### ChainNative.n2s

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L16)

```python
@staticmethod
def n2s(n):
```

convert integer to name string

#### Examples

```python
from uuoskit import uuosapi
uuosapi.n2s(10927537166380695552)
```

```
Output:
'myname'
```

### ChainNative.pack_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L80)

```python
@staticmethod
def pack_abi(abi):
```

### ChainNative.pack_abi_type

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L61)

```python
@staticmethod
def pack_abi_type(account, struct_name, args):
```

### ChainNative.pack_args

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L49)

```python
@staticmethod
def pack_args(account, action, args):
```

### ChainNative.pack_cpp_object

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L130)

```python
@staticmethod
def pack_cpp_object(obj_type, json_str):
```

### ChainNative.pack_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L102)

```python
@staticmethod
def pack_transaction(trx, compress=0):
```

### ChainNative.recover_key

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L126)

```python
@staticmethod
def recover_key(digest, sign):
```

### ChainNative.s2b

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L35)

```python
@staticmethod
def s2b(s):
```

### ChainNative.s2n

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L31)

```python
@staticmethod
def s2n(s):
```

### ChainNative.set_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L75)

```python
@staticmethod
def set_abi(account, abi):
```

### ChainNative.set_public_key_prefix

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L151)

```python
@staticmethod
def set_public_key_prefix(prefix):
```

### ChainNative.sign_digest

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L138)

```python
@staticmethod
def sign_digest(priv_key, digest):
```

### ChainNative.sign_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L95)

```python
@staticmethod
def sign_transaction(trx, private_key, chain_id):
```

### ChainNative.string_to_symbol

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L45)

```python
@staticmethod
def string_to_symbol(precision, str_symbol):
```

### ChainNative.to_base58

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L122)

```python
@staticmethod
def to_base58(raw_pub_key):
```

### ChainNative.unpack_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L86)

```python
@staticmethod
def unpack_abi(packed_abi):
```

### ChainNative.unpack_abi_type

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L67)

```python
@staticmethod
def unpack_abi_type(account, struct_name, binargs):
```

### ChainNative.unpack_args

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L54)

```python
@staticmethod
def unpack_args(account, action, binargs):
```

### ChainNative.unpack_cpp_object

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L134)

```python
@staticmethod
def unpack_cpp_object(obj_type, raw_data):
```

### ChainNative.unpack_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L106)

```python
@staticmethod
def unpack_transaction(trx):
```

## check_result

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L9)

```python
def check_result(r):
```

## raise_last_error

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainnative.py#L6)

```python
def raise_last_error():
```
