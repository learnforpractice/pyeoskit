# Chainapi Sync

> Auto-generated documentation for [pysrc.chainapi_sync](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / Chainapi Sync
    - [ChainApi](#chainapi)
        - [ChainApi().create_account](#chainapicreate_account)
        - [ChainApi().deploy_abi](#chainapideploy_abi)
        - [ChainApi().deploy_code](#chainapideploy_code)
        - [ChainApi().deploy_contract](#chainapideploy_contract)
        - [ChainApi().deploy_module](#chainapideploy_module)
        - [ChainApi().deploy_python_code](#chainapideploy_python_code)
        - [ChainApi().deploy_python_contract](#chainapideploy_python_contract)
        - [ChainApi().enable_decode](#chainapienable_decode)
        - [ChainApi().exec](#chainapiexec)
        - [ChainApi().get_abi](#chainapiget_abi)
        - [ChainApi().get_account](#chainapiget_account)
        - [ChainApi().get_available_public_keys](#chainapiget_available_public_keys)
        - [ChainApi().get_balance](#chainapiget_balance)
        - [ChainApi().get_chain_id](#chainapiget_chain_id)
        - [ChainApi().get_code](#chainapiget_code)
        - [ChainApi().get_keys](#chainapiget_keys)
        - [ChainApi().get_packed_abi](#chainapiget_packed_abi)
        - [ChainApi().get_public_keys](#chainapiget_public_keys)
        - [ChainApi().get_raw_code](#chainapiget_raw_code)
        - [ChainApi().init](#chainapiinit)
        - [ChainApi().push_action](#chainapipush_action)
        - [ChainApi().push_actions](#chainapipush_actions)
        - [ChainApi().push_transaction](#chainapipush_transaction)
        - [ChainApi().push_transactions](#chainapipush_transactions)
        - [ChainApi().set_abi](#chainapiset_abi)
        - [ChainApi().set_code](#chainapiset_code)
        - [ChainApi().strip_prefix](#chainapistrip_prefix)
        - [ChainApi().transfer](#chainapitransfer)

## ChainApi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L17)

```python
class ChainApi(Client, ChainNative):
    def __init__(node_url='http://127.0.0.1:8888', network='EOS'):
```

### ChainApi().create_account

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L141)

```python
def create_account(
    creator,
    account,
    owner_key,
    active_key,
    ram_bytes=0,
    stake_net=0.0,
    stake_cpu=0.0,
    sign=True,
):
```

### ChainApi().deploy_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L308)

```python
def deploy_abi(account, abi):
```

### ChainApi().deploy_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L297)

```python
def deploy_code(account, code, vm_type=0, vm_version=0):
```

### ChainApi().deploy_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L266)

```python
def deploy_contract(
    account,
    code,
    abi,
    vm_type=0,
    vm_version=0,
    sign=True,
    compress=0,
):
```

### ChainApi().deploy_module

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L388)

```python
def deploy_module(account, module_name, code, deploy_type=1):
```

### ChainApi().deploy_python_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L364)

```python
def deploy_python_code(account, code, deploy_type=0):
```

### ChainApi().deploy_python_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L320)

```python
def deploy_python_contract(account, code, abi, deploy_type=0):
```

### ChainApi().enable_decode

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L25)

```python
def enable_decode(json_format):
```

### ChainApi().exec

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L397)

```python
def exec(account, args, permissions={}):
```

### ChainApi().get_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L230)

```python
def get_abi(account):
```

### ChainApi().get_account

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L131)

```python
def get_account(account):
```

### ChainApi().get_available_public_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L114)

```python
def get_available_public_keys(account, permission):
```

### ChainApi().get_balance

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L182)

```python
def get_balance(account, token_account=None, token_name=None):
```

### ChainApi().get_chain_id

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L32)

```python
def get_chain_id():
```

### ChainApi().get_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L203)

```python
def get_code(account):
```

### ChainApi().get_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L420)

```python
def get_keys(account_name, perm_name):
```

### ChainApi().get_packed_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L252)

```python
def get_packed_abi(account):
```

### ChainApi().get_public_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L414)

```python
def get_public_keys(account_name, perm_name):
```

### ChainApi().get_raw_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L216)

```python
def get_raw_code(account):
```

### ChainApi().init

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L28)

```python
def init():
```

### ChainApi().push_action

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L39)

```python
def push_action(contract, action, args, permissions=None, compress=0):
```

### ChainApi().push_actions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L67)

```python
def push_actions(actions, compress=0):
```

### ChainApi().push_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L35)

```python
def push_transaction(trx, compress=0):
```

### ChainApi().push_transactions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L87)

```python
def push_transactions(aaa, expiration=60):
```

### ChainApi().set_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L226)

```python
def set_abi(account, abi):
```

### ChainApi().set_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L223)

```python
def set_code(account, code):
```

### ChainApi().strip_prefix

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L106)

```python
def strip_prefix(pub_key):
```

### ChainApi().transfer

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_sync.py#L195)

```python
def transfer(
    _from,
    to,
    amount,
    memo='',
    token_account=None,
    token_name=None,
    permission='active',
):
```
