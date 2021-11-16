# Wallet

> Auto-generated documentation for [pysrc.wallet](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Wallet
    - [check_result](#check_result)
    - [create](#create)
    - [get_public_keys](#get_public_keys)
    - [import_key](#import_key)
    - [list_keys](#list_keys)
    - [list_wallets](#list_wallets)
    - [lock](#lock)
    - [lock_all](#lock_all)
    - [open](#open)
    - [remove_key](#remove_key)
    - [save](#save)
    - [set_dir](#set_dir)
    - [set_timeout](#set_timeout)
    - [sign_digest](#sign_digest)
    - [sign_transaction](#sign_transaction)
    - [unlock](#unlock)

## check_result

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L9)

```python
def check_result(result, json=False):
```

## create

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L15)

```python
def create(name):
```

## get_public_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L36)

```python
def get_public_keys():
```

## import_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L50)

```python
def import_key(name, wif_key, save=True):
```

## list_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L33)

```python
def list_keys(name, psw) -> Dict[str, str]:
```

## list_wallets

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L30)

```python
def list_wallets() -> List[bytes]:
```

## lock

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L44)

```python
def lock(name):
```

## lock_all

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L41)

```python
def lock_all():
```

## open

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L21)

```python
def open(name):
```

## remove_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L53)

```python
def remove_key(name, password, pub_key):
```

## save

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L18)

```python
def save(name):
```

## set_dir

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L24)

```python
def set_dir(path_name):
```

## set_timeout

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L27)

```python
def set_timeout(secs):
```

## sign_digest

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L64)

```python
def sign_digest(digest: Union[bytes, str], public_key: str):
```

## sign_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L56)

```python
def sign_transaction(
    trx: Union[str, dict],
    public_keys: List[str],
    chain_id: str,
    json=False,
):
```

## unlock

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/wallet.py#L47)

```python
def unlock(name, password):
```
