# ChainCache

> Auto-generated documentation for [pysrc.chaincache](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / ChainCache
    - [ChainCache](#chaincache)
        - [ChainCache().get_abi](#chaincacheget_abi)
        - [ChainCache().get_account](#chaincacheget_account)
        - [ChainCache().get_code](#chaincacheget_code)
        - [ChainCache().get_info](#chaincacheget_info)
        - [ChainCache().get_public_keys](#chaincacheget_public_keys)
        - [ChainCache().get_value](#chaincacheget_value)
        - [ChainCache().remove_abi](#chaincacheremove_abi)
        - [ChainCache().remove_code](#chaincacheremove_code)
        - [ChainCache().reset](#chaincachereset)
        - [ChainCache().save](#chaincachesave)
        - [ChainCache().set_abi](#chaincacheset_abi)
        - [ChainCache().set_account](#chaincacheset_account)
        - [ChainCache().set_code](#chaincacheset_code)
        - [ChainCache().set_info](#chaincacheset_info)
        - [ChainCache().set_value](#chaincacheset_value)

## ChainCache

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L12)

```python
class ChainCache(object):
    def __init__(client, network):
```

### ChainCache().get_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L52)

```python
def get_abi(account):
```

### ChainCache().get_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L69)

```python
def get_account(account):
```

### ChainCache().get_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L40)

```python
def get_code(account):
```

### ChainCache().get_info

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L37)

```python
def get_info(info):
```

### ChainCache().get_public_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L81)

```python
def get_public_keys(account, key_type):
```

### ChainCache().get_value

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L24)

```python
def get_value(key):
```

### ChainCache().remove_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L60)

```python
def remove_abi(account):
```

### ChainCache().remove_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L48)

```python
def remove_code(account):
```

### ChainCache().reset

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L18)

```python
def reset():
```

### ChainCache().save

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L21)

```python
def save():
```

### ChainCache().set_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L57)

```python
def set_abi(account, abi):
```

### ChainCache().set_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L64)

```python
def set_account(account, info):
```

### ChainCache().set_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L45)

```python
def set_code(account, code):
```

### ChainCache().set_info

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L34)

```python
def set_info(info):
```

### ChainCache().set_value

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chaincache.py#L30)

```python
def set_value(key, value):
```
