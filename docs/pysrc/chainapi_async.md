# ChainApiAsync

> Auto-generated documentation for [pysrc.chainapi_async](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / ChainApiAsync
    - [ChainApiAsync](#chainapiasync)
        - [ChainApiAsync().compile](#chainapiasynccompile)
        - [ChainApiAsync().create_account](#chainapiasynccreate_account)
        - [ChainApiAsync().deploy_abi](#chainapiasyncdeploy_abi)
        - [ChainApiAsync().deploy_code](#chainapiasyncdeploy_code)
        - [ChainApiAsync().deploy_contract](#chainapiasyncdeploy_contract)
        - [ChainApiAsync().deploy_module](#chainapiasyncdeploy_module)
        - [ChainApiAsync().deploy_python_code](#chainapiasyncdeploy_python_code)
        - [ChainApiAsync().deploy_python_contract](#chainapiasyncdeploy_python_contract)
        - [ChainApiAsync().enable_decode](#chainapiasyncenable_decode)
        - [ChainApiAsync().exec](#chainapiasyncexec)
        - [ChainApiAsync().get_abi](#chainapiasyncget_abi)
        - [ChainApiAsync().get_account](#chainapiasyncget_account)
        - [ChainApiAsync().get_available_public_keys](#chainapiasyncget_available_public_keys)
        - [ChainApiAsync().get_balance](#chainapiasyncget_balance)
        - [ChainApiAsync().get_chain_id](#chainapiasyncget_chain_id)
        - [ChainApiAsync().get_code](#chainapiasyncget_code)
        - [ChainApiAsync().get_keys](#chainapiasyncget_keys)
        - [ChainApiAsync().get_public_keys](#chainapiasyncget_public_keys)
        - [ChainApiAsync().init](#chainapiasyncinit)
        - [ChainApiAsync().push_action](#chainapiasyncpush_action)
        - [ChainApiAsync().push_actions](#chainapiasyncpush_actions)
        - [ChainApiAsync().push_transaction](#chainapiasyncpush_transaction)
        - [ChainApiAsync().push_transactions](#chainapiasyncpush_transactions)
        - [ChainApiAsync().python_contract_get_table_rows](#chainapiasyncpython_contract_get_table_rows)
        - [ChainApiAsync().set_abi](#chainapiasyncset_abi)
        - [ChainApiAsync().set_code](#chainapiasyncset_code)
        - [ChainApiAsync().set_node](#chainapiasyncset_node)
        - [ChainApiAsync().strip_prefix](#chainapiasyncstrip_prefix)
        - [ChainApiAsync().transfer](#chainapiasynctransfer)

## ChainApiAsync

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L17)

```python
class ChainApiAsync(Client, ChainNative):
    def __init__(node_url='http://127.0.0.1:8888', network='EOS'):
```

### ChainApiAsync().compile

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L240)

```python
async def compile(contract_name, src, vm_type):
```

### ChainApiAsync().create_account

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L141)

```python
async def create_account(
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

### ChainApiAsync().deploy_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L391)

```python
async def deploy_abi(account, abi):
```

### ChainApiAsync().deploy_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L380)

```python
async def deploy_code(account, code, vm_type=0, vm_version=0):
```

### ChainApiAsync().deploy_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L243)

```python
async def deploy_contract(
    account,
    code,
    abi,
    vm_type=0,
    vm_version=0,
    sign=True,
    compress=0,
):
```

### ChainApiAsync().deploy_module

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L329)

```python
async def deploy_module(account, module_name, code, deploy_type=1):
```

### ChainApiAsync().deploy_python_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L306)

```python
async def deploy_python_code(account, code, deploy_type=0):
```

### ChainApiAsync().deploy_python_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L266)

```python
async def deploy_python_contract(account, code, abi, deploy_type=0):
```

### ChainApiAsync().enable_decode

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L32)

```python
def enable_decode(json_format):
```

### ChainApiAsync().exec

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L338)

```python
async def exec(account, args, permissions={}):
```

### ChainApiAsync().get_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L223)

```python
async def get_abi(account):
```

### ChainApiAsync().get_account

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L131)

```python
async def get_account(account):
```

### ChainApiAsync().get_available_public_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L114)

```python
async def get_available_public_keys(account, permission):
```

### ChainApiAsync().get_balance

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L182)

```python
async def get_balance(account, token_account=None, token_name=None):
```

### ChainApiAsync().get_chain_id

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L39)

```python
def get_chain_id():
```

### ChainApiAsync().get_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L203)

```python
async def get_code(account):
```

### ChainApiAsync().get_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L407)

```python
async def get_keys(account_name, perm_name):
```

### ChainApiAsync().get_public_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L401)

```python
async def get_public_keys(account_name, perm_name):
```

### ChainApiAsync().init

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L35)

```python
def init():
```

### ChainApiAsync().push_action

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L46)

```python
async def push_action(contract, action, args, permissions=None, compress=0):
```

### ChainApiAsync().push_actions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L65)

```python
async def push_actions(actions, compress=0):
```

### ChainApiAsync().push_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L42)

```python
def push_transaction(trx, compress=0):
```

### ChainApiAsync().push_transactions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L87)

```python
async def push_transactions(aaa, expiration=60):
```

### ChainApiAsync().python_contract_get_table_rows

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L355)

```python
async def python_contract_get_table_rows(
    code,
    scope,
    table,
    lower_bound,
    upper_bound,
    limit=10,
):
```

### ChainApiAsync().set_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L219)

```python
def set_abi(account, abi):
```

### ChainApiAsync().set_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L216)

```python
def set_code(account, code):
```

### ChainApiAsync().set_node

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L28)

```python
def set_node(node_url):
```

### ChainApiAsync().strip_prefix

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L106)

```python
def strip_prefix(pub_key):
```

### ChainApiAsync().transfer

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/chainapi_async.py#L195)

```python
async def transfer(
    _from,
    to,
    amount,
    memo='',
    token_account=None,
    token_name=None,
    permission='active',
):
```
