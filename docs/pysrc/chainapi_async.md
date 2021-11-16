# ChainApiAsync

> Auto-generated documentation for [pysrc.chainapi_async](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / ChainApiAsync
    - [ChainApiAsync](#chainapiasync)
        - [ChainApiAsync().create_account](#chainapiasynccreate_account)
        - [ChainApiAsync().deploy_abi](#chainapiasyncdeploy_abi)
        - [ChainApiAsync().deploy_code](#chainapiasyncdeploy_code)
        - [ChainApiAsync().deploy_contract](#chainapiasyncdeploy_contract)
        - [ChainApiAsync().deploy_module](#chainapiasyncdeploy_module)
        - [ChainApiAsync().deploy_python_code](#chainapiasyncdeploy_python_code)
        - [ChainApiAsync().deploy_python_contract](#chainapiasyncdeploy_python_contract)
        - [ChainApiAsync().deploy_wasm_contract](#chainapiasyncdeploy_wasm_contract)
        - [ChainApiAsync().enable_decode](#chainapiasyncenable_decode)
        - [ChainApiAsync().exec](#chainapiasyncexec)
        - [ChainApiAsync().generate_packed_transaction](#chainapiasyncgenerate_packed_transaction)
        - [ChainApiAsync().get_abi](#chainapiasyncget_abi)
        - [ChainApiAsync().get_account](#chainapiasyncget_account)
        - [ChainApiAsync().get_balance](#chainapiasyncget_balance)
        - [ChainApiAsync().get_chain_id](#chainapiasyncget_chain_id)
        - [ChainApiAsync().get_code](#chainapiasyncget_code)
        - [ChainApiAsync().get_keys](#chainapiasyncget_keys)
        - [ChainApiAsync().get_public_keys](#chainapiasyncget_public_keys)
        - [ChainApiAsync().get_raw_code](#chainapiasyncget_raw_code)
        - [ChainApiAsync().get_required_keys](#chainapiasyncget_required_keys)
        - [ChainApiAsync().get_sign_keys](#chainapiasyncget_sign_keys)
        - [ChainApiAsync().init](#chainapiasyncinit)
        - [ChainApiAsync().push_action](#chainapiasyncpush_action)
        - [ChainApiAsync().push_actions](#chainapiasyncpush_actions)
        - [ChainApiAsync().push_transaction](#chainapiasyncpush_transaction)
        - [ChainApiAsync().push_transactions](#chainapiasyncpush_transactions)
        - [ChainApiAsync().set_abi](#chainapiasyncset_abi)
        - [ChainApiAsync().set_code](#chainapiasyncset_code)
        - [ChainApiAsync().set_node](#chainapiasyncset_node)
        - [ChainApiAsync().strip_prefix](#chainapiasyncstrip_prefix)
        - [ChainApiAsync().transfer](#chainapiasynctransfer)

## ChainApiAsync

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L24)

```python
class ChainApiAsync(RPCInterface, ChainNative):
    def __init__(node_url='http://127.0.0.1:8888', network='EOS'):
```

### ChainApiAsync().create_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L161)

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

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L329)

```python
async def deploy_abi(account, abi):
```

### ChainApiAsync().deploy_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L318)

```python
async def deploy_code(account, code, vm_type=0, vm_version=0):
```

### ChainApiAsync().deploy_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L279)

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

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L395)

```python
async def deploy_module(account, module_name, code, deploy_type=1):
```

### ChainApiAsync().deploy_python_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L392)

```python
async def deploy_python_code(account, code, deploy_type=0):
```

### ChainApiAsync().deploy_python_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L341)

```python
async def deploy_python_contract(account, code, abi, deploy_type=0):
```

Deploy a python contract to EOSIO based network

#### Arguments

deploy_type (int) : 0 for UUOS network, 1 for EOS network

### ChainApiAsync().deploy_wasm_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L287)

```python
def deploy_wasm_contract(
    account,
    code,
    abi,
    vm_type=0,
    vm_version=0,
    sign=True,
    compress=0,
):
```

### ChainApiAsync().enable_decode

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L34)

```python
def enable_decode(json_format):
```

### ChainApiAsync().exec

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L404)

```python
async def exec(account, args, permissions={}):
```

### ChainApiAsync().generate_packed_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L84)

```python
async def generate_packed_transaction(
    actions,
    expiration,
    ref_block,
    chain_id,
    compress=0,
):
```

### ChainApiAsync().get_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L256)

```python
async def get_abi(account):
```

### ChainApiAsync().get_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L151)

```python
async def get_account(account):
```

### ChainApiAsync().get_balance

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L202)

```python
async def get_balance(account, token_account=None, token_name=None):
```

### ChainApiAsync().get_chain_id

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L41)

```python
def get_chain_id():
```

### ChainApiAsync().get_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L229)

```python
async def get_code(account):
```

### ChainApiAsync().get_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L427)

```python
async def get_keys(account_name, perm_name):
```

### ChainApiAsync().get_public_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L421)

```python
async def get_public_keys(account_name, perm_name):
```

### ChainApiAsync().get_raw_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L242)

```python
async def get_raw_code(account):
```

### ChainApiAsync().get_required_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L47)

```python
async def get_required_keys(trx, public_keys):
```

### ChainApiAsync().get_sign_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L51)

```python
async def get_sign_keys(actions):
```

### ChainApiAsync().init

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L37)

```python
def init():
```

### ChainApiAsync().push_action

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L118)

```python
async def push_action(
    contract,
    action,
    args,
    permissions=None,
    compress=0,
    expiration=0,
):
```

### ChainApiAsync().push_actions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L124)

```python
async def push_actions(actions, expiration=0, compress=0):
```

### ChainApiAsync().push_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L44)

```python
def push_transaction(trx: Union[str, dict], compress=0):
```

### ChainApiAsync().push_transactions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L132)

```python
async def push_transactions(aaa, expiration=60, compress=0):
```

### ChainApiAsync().set_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L252)

```python
def set_abi(account, abi):
```

### ChainApiAsync().set_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L249)

```python
def set_code(account, code):
```

### ChainApiAsync().set_node

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L31)

```python
def set_node(node_url):
```

### ChainApiAsync().strip_prefix

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L143)

```python
def strip_prefix(pub_key):
```

### ChainApiAsync().transfer

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_async.py#L220)

```python
async def transfer(
    _from,
    to,
    amount,
    memo='',
    token_account=None,
    token_name=None,
    token_precision=4,
    permission='active',
):
```
