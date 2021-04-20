# Wallet

> Auto-generated documentation for [pysrc.wallet](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / Wallet
    - [check_result](#check_result)
    - [create](#create)
    - [get_public_keys](#get_public_keys)
    - [import_key](#import_key)
    - [list_keys](#list_keys)
    - [list_wallets](#list_wallets)
    - [lock](#lock)
    - [lock_all](#lock_all)
    - [open](#open)
    - [raise_last_error](#raise_last_error)
    - [remove_key](#remove_key)
    - [save](#save)
    - [set_dir](#set_dir)
    - [set_timeout](#set_timeout)
    - [sign_digest](#sign_digest)
    - [sign_transaction](#sign_transaction)
    - [unlock](#unlock)

## check_result

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L12)

```python
def check_result(result):
```

## create

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L17)

```python
def create(name):
```

## get_public_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L45)

```python
def get_public_keys():
```

## import_key

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L58)

```python
def import_key(name, wif_key, save=True):
```

## list_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L39)

```python
def list_keys(name, psw) -> Dict[str, str]:
```

## list_wallets

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L33)

```python
def list_wallets() -> List[bytes]:
```

## lock

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L52)

```python
def lock(name):
```

## lock_all

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L49)

```python
def lock_all():
```

## open

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L24)

```python
def open(name):
```

## raise_last_error

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L9)

```python
def raise_last_error():
```

## remove_key

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L61)

```python
def remove_key(name, password, pub_key):
```

## save

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L21)

```python
def save(name):
```

## set_dir

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L27)

```python
def set_dir(path_name):
```

## set_timeout

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L30)

```python
def set_timeout(secs):
```

## sign_digest

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L67)

```python
def sign_digest(digest, public_key: str):
```

## sign_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L64)

```python
def sign_transaction(trx: str, public_keys: List[str], chain_id: str):
```

## unlock

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/wallet.py#L55)

```python
def unlock(name, password):
```
