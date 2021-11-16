# ChainNative

> Auto-generated documentation for [pysrc.chainnative](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / ChainNative
    - [ChainNative](#chainnative)
        - [ChainNative.b2s](#chainnativeb2s)
        - [ChainNative().check_abi](#chainnativecheck_abi)
        - [ChainNative.clear_abi_cache](#chainnativeclear_abi_cache)
        - [ChainNative().compile](#chainnativecompile)
        - [ChainNative.create_key](#chainnativecreate_key)
        - [ChainNative().gen_transaction](#chainnativegen_transaction)
        - [ChainNative().generate_transaction](#chainnativegenerate_transaction)
        - [ChainNative().get_abi_sync](#chainnativeget_abi_sync)
        - [ChainNative.get_debug_flag](#chainnativeget_debug_flag)
        - [ChainNative.get_public_key](#chainnativeget_public_key)
        - [ChainNative.mp_compile](#chainnativemp_compile)
        - [ChainNative().mp_make_frozen](#chainnativemp_make_frozen)
        - [ChainNative.n2s](#chainnativen2s)
        - [ChainNative.pack_abi](#chainnativepack_abi)
        - [ChainNative().pack_abi_type](#chainnativepack_abi_type)
        - [ChainNative().pack_args](#chainnativepack_args)
        - [ChainNative.pack_transaction](#chainnativepack_transaction)
        - [ChainNative.recover_key](#chainnativerecover_key)
        - [ChainNative.s2b](#chainnatives2b)
        - [ChainNative.s2n](#chainnatives2n)
        - [ChainNative.set_abi](#chainnativeset_abi)
        - [ChainNative.set_debug_flag](#chainnativeset_debug_flag)
        - [ChainNative.sign_digest](#chainnativesign_digest)
        - [ChainNative.sign_transaction](#chainnativesign_transaction)
        - [ChainNative.string_to_symbol](#chainnativestring_to_symbol)
        - [ChainNative.unpack_abi](#chainnativeunpack_abi)
        - [ChainNative().unpack_abi_type](#chainnativeunpack_abi_type)
        - [ChainNative().unpack_args](#chainnativeunpack_args)
        - [ChainNative.unpack_transaction](#chainnativeunpack_transaction)

## ChainNative

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L17)

```python
class ChainNative(object):
```

### ChainNative.b2s

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L62)

```python
@staticmethod
def b2s(b):
```

### ChainNative().check_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L77)

```python
def check_abi(account):
```

### ChainNative.clear_abi_cache

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L113)

```python
@staticmethod
def clear_abi_cache(account):
```

### ChainNative().compile

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L224)

```python
def compile(contract_name, code, src_type=SRC_TYPE_CPP):
```

#### Arguments

- `contract_name` - contract name
- `code` - source code
- `src_type` - 0: py, 1: cpp 2: go

#### Returns

bytecode and abi

#### See also

- [SRC_TYPE_CPP](#src_type_cpp)

### ChainNative.create_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L178)

```python
@staticmethod
def create_key():
```

### ChainNative().gen_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L133)

```python
def gen_transaction(actions, expiration, reference_block_id, chain_id):
```

### ChainNative().generate_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L160)

```python
def generate_transaction(actions, expiration, reference_block_id, chain_id):
```

### ChainNative().get_abi_sync

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L19)

```python
def get_abi_sync(account):
```

### ChainNative.get_debug_flag

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L247)

```python
@staticmethod
def get_debug_flag() -> bool:
```

### ChainNative.get_public_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L182)

```python
@staticmethod
def get_public_key(priv, eos_pub=True):
```

### ChainNative.mp_compile

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L199)

```python
@staticmethod
def mp_compile(contract, src):
```

### ChainNative().mp_make_frozen

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L203)

```python
def mp_make_frozen(code):
```

### ChainNative.n2s

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L35)

```python
@staticmethod
def n2s(n):
```

convert integer to name string

#### Examples

```python
from pyeoskit import eosapi
s = eosapi.n2s(10927537166380695552)
print(s)
```

```
'myname'
```

### ChainNative.pack_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L123)

```python
@staticmethod
def pack_abi(abi):
```

### ChainNative().pack_abi_type

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L101)

```python
def pack_abi_type(account, struct_name, args):
```

### ChainNative().pack_args

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L82)

```python
def pack_args(account, action, args):
```

### ChainNative.pack_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L168)

```python
@staticmethod
def pack_transaction(tx, compress=0, json=False):
```

### ChainNative.recover_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L187)

```python
@staticmethod
def recover_key(digest, sign):
```

### ChainNative.s2b

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L57)

```python
@staticmethod
def s2b(s):
```

### ChainNative.s2n

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L50)

```python
@staticmethod
def s2n(s):
```

### ChainNative.set_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L117)

```python
@staticmethod
def set_abi(account, abi):
```

### ChainNative.set_debug_flag

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L243)

```python
@staticmethod
def set_debug_flag(debug):
```

### ChainNative.sign_digest

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L192)

```python
@staticmethod
def sign_digest(digest, priv_key):
```

### ChainNative.sign_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L163)

```python
@staticmethod
def sign_transaction(tx, private_key, chain_id, json=False):
```

### ChainNative.string_to_symbol

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L67)

```python
@staticmethod
def string_to_symbol(sym):
```

### ChainNative.unpack_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L129)

```python
@staticmethod
def unpack_abi(packed_abi):
```

### ChainNative().unpack_abi_type

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L109)

```python
def unpack_abi_type(account, struct_name, binargs):
```

### ChainNative().unpack_args

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L93)

```python
def unpack_args(account, action, binargs, json=False):
```

### ChainNative.unpack_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainnative.py#L174)

```python
@staticmethod
def unpack_transaction(trx, json=False):
```
