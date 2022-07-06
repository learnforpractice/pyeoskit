# Chainapi Sync

> Auto-generated documentation for [pysrc.chainapi_sync](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Chainapi Sync
    - [ChainApi](#chainapi)
        - [ChainApi().create_account](#chainapicreate_account)
        - [ChainApi().deploy_abi](#chainapideploy_abi)
        - [ChainApi().deploy_code](#chainapideploy_code)
        - [ChainApi().deploy_contract](#chainapideploy_contract)
        - [ChainApi().deploy_module](#chainapideploy_module)
        - [ChainApi().deploy_python_code](#chainapideploy_python_code)
        - [ChainApi().deploy_python_contract](#chainapideploy_python_contract)
        - [ChainApi().deploy_wasm_contract](#chainapideploy_wasm_contract)
        - [ChainApi().enable_decode](#chainapienable_decode)
        - [ChainApi().exec](#chainapiexec)
        - [ChainApi().generate_packed_transaction](#chainapigenerate_packed_transaction)
        - [ChainApi().get_abi](#chainapiget_abi)
        - [ChainApi().get_account](#chainapiget_account)
        - [ChainApi().get_balance](#chainapiget_balance)
        - [ChainApi().get_chain_id](#chainapiget_chain_id)
        - [ChainApi().get_code](#chainapiget_code)
        - [ChainApi().get_keys](#chainapiget_keys)
        - [ChainApi().get_public_keys](#chainapiget_public_keys)
        - [ChainApi().get_raw_code](#chainapiget_raw_code)
        - [ChainApi().get_required_keys](#chainapiget_required_keys)
        - [ChainApi().get_sign_keys](#chainapiget_sign_keys)
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

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L25)

```python
class ChainApi(RPCInterface, ChainNative):
    def __init__(node_url='http://127.0.0.1:8888', network='EOS'):
```

### ChainApi().create_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L182)

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
    indices=None,
):
```

### ChainApi().deploy_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L348)

```python
def deploy_abi(account, abi, indices=None):
```

### ChainApi().deploy_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L337)

```python
def deploy_code(account, code, vm_type=0, vm_version=0):
```

### ChainApi().deploy_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L298)

```python
def deploy_contract(
    account,
    code,
    abi,
    vm_type=0,
    vm_version=0,
    sign=True,
    compress=False,
    indices=None,
):
```

### ChainApi().deploy_module

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L415)

```python
def deploy_module(account, module_name, code, deploy_type=1):
```

### ChainApi().deploy_python_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L412)

```python
def deploy_python_code(account, code, deploy_type=0):
```

### ChainApi().deploy_python_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L360)

```python
def deploy_python_contract(account, code, abi, deploy_type=0, indices=None):
```

Deploy a python contract to EOSIO based network

#### Arguments

deploy_type (int) : 0 for UUOS network, 1 for EOS network

### ChainApi().deploy_wasm_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L306)

```python
def deploy_wasm_contract(
    account,
    code,
    abi,
    vm_type=0,
    vm_version=0,
    sign=True,
    compress=0,
    indices=None,
):
```

### ChainApi().enable_decode

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L32)

```python
def enable_decode(json_format):
```

### ChainApi().exec

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L424)

```python
def exec(account, args, permissions={}):
```

### ChainApi().generate_packed_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L81)

```python
def generate_packed_transaction(
    actions,
    expiration,
    ref_block,
    chain_id,
    compress=0,
    indices=None,
):
```

### ChainApi().get_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L276)

```python
def get_abi(account):
```

### ChainApi().get_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L171)

```python
def get_account(account):
```

### ChainApi().get_balance

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L223)

```python
def get_balance(account, token_account=None, token_name=None):
```

### ChainApi().get_chain_id

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L39)

```python
def get_chain_id():
```

### ChainApi().get_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L249)

```python
def get_code(account):
```

### ChainApi().get_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L447)

```python
def get_keys(account_name, perm_name):
```

### ChainApi().get_public_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L441)

```python
def get_public_keys(account_name, perm_name):
```

### ChainApi().get_raw_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L262)

```python
def get_raw_code(account):
```

### ChainApi().get_required_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L45)

```python
def get_required_keys(trx, public_keys):
```

### ChainApi().get_sign_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L49)

```python
def get_sign_keys(actions, pub_keys):
```

### ChainApi().init

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L35)

```python
def init():
```

### ChainApi().push_action

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L137)

```python
def push_action(
    contract,
    action,
    args,
    permissions=None,
    compress=False,
    expiration=0,
    indices=None,
):
```

### ChainApi().push_actions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L143)

```python
def push_actions(actions, expiration=0, compress=0, indices=None):
```

### ChainApi().push_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L42)

```python
def push_transaction(trx: Union[str, dict]):
```

### ChainApi().push_transactions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L155)

```python
def push_transactions(aaa, expiration=60, compress=False, indices=None):
```

### ChainApi().set_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L272)

```python
def set_abi(account, abi):
```

### ChainApi().set_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L269)

```python
def set_code(account, code):
```

### ChainApi().strip_prefix

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L165)

```python
def strip_prefix(pub_key):
```

### ChainApi().transfer

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/chainapi_sync.py#L241)

```python
def transfer(
    _from,
    to,
    amount,
    memo='',
    token_account=None,
    token_name=None,
    token_precision=4,
    permission='active',
    indices=None,
):
```
