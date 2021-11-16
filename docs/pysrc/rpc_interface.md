# RPCInterface

> Auto-generated documentation for [pysrc.rpc_interface](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / RPCInterface
    - [RPCInterface](#rpcinterface)
        - [RPCInterface().abi_bin_to_json](#rpcinterfaceabi_bin_to_json)
        - [RPCInterface().abi_json_to_bin](#rpcinterfaceabi_json_to_bin)
        - [RPCInterface().add_debug_contract](#rpcinterfaceadd_debug_contract)
        - [RPCInterface().add_greylist_accounts](#rpcinterfaceadd_greylist_accounts)
        - [RPCInterface().call_contract](#rpcinterfacecall_contract)
        - [RPCInterface().clear_debug_contract](#rpcinterfaceclear_debug_contract)
        - [RPCInterface().clear_filter_on](#rpcinterfaceclear_filter_on)
        - [RPCInterface().clear_filter_out](#rpcinterfaceclear_filter_out)
        - [RPCInterface().create_snapshot](#rpcinterfacecreate_snapshot)
        - [RPCInterface().enable_debug](#rpcinterfaceenable_debug)
        - [RPCInterface().get_abi](#rpcinterfaceget_abi)
        - [RPCInterface().get_account](#rpcinterfaceget_account)
        - [RPCInterface().get_account_ram_corrections](#rpcinterfaceget_account_ram_corrections)
        - [RPCInterface().get_actions](#rpcinterfaceget_actions)
        - [RPCInterface().get_activated_protocol_features](#rpcinterfaceget_activated_protocol_features)
        - [RPCInterface().get_block](#rpcinterfaceget_block)
        - [RPCInterface().get_block_header_state](#rpcinterfaceget_block_header_state)
        - [RPCInterface().get_code](#rpcinterfaceget_code)
        - [RPCInterface().get_code_hash](#rpcinterfaceget_code_hash)
        - [RPCInterface().get_controlled_accounts](#rpcinterfaceget_controlled_accounts)
        - [RPCInterface().get_currency_balance](#rpcinterfaceget_currency_balance)
        - [RPCInterface().get_currency_balance](#rpcinterfaceget_currency_balance)
        - [RPCInterface().get_currency_stats](#rpcinterfaceget_currency_stats)
        - [RPCInterface().get_currency_stats](#rpcinterfaceget_currency_stats)
        - [RPCInterface().get_db_size](#rpcinterfaceget_db_size)
        - [RPCInterface().get_greylist](#rpcinterfaceget_greylist)
        - [RPCInterface().get_history_db_size](#rpcinterfaceget_history_db_size)
        - [RPCInterface().get_info](#rpcinterfaceget_info)
        - [RPCInterface().get_integrity_hash](#rpcinterfaceget_integrity_hash)
        - [RPCInterface().get_key_accounts](#rpcinterfaceget_key_accounts)
        - [RPCInterface().get_key_accounts_ex](#rpcinterfaceget_key_accounts_ex)
        - [RPCInterface().get_producer_schedule](#rpcinterfaceget_producer_schedule)
        - [RPCInterface().get_producers](#rpcinterfaceget_producers)
        - [RPCInterface().get_raw_abi](#rpcinterfaceget_raw_abi)
        - [RPCInterface().get_raw_code_and_abi](#rpcinterfaceget_raw_code_and_abi)
        - [RPCInterface().get_required_keys](#rpcinterfaceget_required_keys)
        - [RPCInterface().get_runtime_options](#rpcinterfaceget_runtime_options)
        - [RPCInterface().get_scheduled_protocol_feature_activations](#rpcinterfaceget_scheduled_protocol_feature_activations)
        - [RPCInterface().get_scheduled_transactions](#rpcinterfaceget_scheduled_transactions)
        - [RPCInterface().get_supported_apis](#rpcinterfaceget_supported_apis)
        - [RPCInterface().get_supported_protocol_features](#rpcinterfaceget_supported_protocol_features)
        - [RPCInterface().get_table_by_scope](#rpcinterfaceget_table_by_scope)
        - [RPCInterface().get_table_rows](#rpcinterfaceget_table_rows)
        - [RPCInterface().get_transaction](#rpcinterfaceget_transaction)
        - [RPCInterface().get_whitelist_blacklist](#rpcinterfaceget_whitelist_blacklist)
        - [RPCInterface().is_debug_enabled](#rpcinterfaceis_debug_enabled)
        - [RPCInterface().net_connect](#rpcinterfacenet_connect)
        - [RPCInterface().net_connections](#rpcinterfacenet_connections)
        - [RPCInterface().net_disconnect](#rpcinterfacenet_disconnect)
        - [RPCInterface().net_status](#rpcinterfacenet_status)
        - [RPCInterface().pause](#rpcinterfacepause)
        - [RPCInterface().paused](#rpcinterfacepaused)
        - [RPCInterface().push_block](#rpcinterfacepush_block)
        - [RPCInterface().push_transaction](#rpcinterfacepush_transaction)
        - [RPCInterface().push_transactions](#rpcinterfacepush_transactions)
        - [RPCInterface().remove_greylist_accounts](#rpcinterfaceremove_greylist_accounts)
        - [RPCInterface().resume](#rpcinterfaceresume)
        - [RPCInterface().schedule_protocol_feature_activations](#rpcinterfaceschedule_protocol_feature_activations)
        - [RPCInterface().set_filter_on](#rpcinterfaceset_filter_on)
        - [RPCInterface().set_filter_out](#rpcinterfaceset_filter_out)
        - [RPCInterface().set_logger_level](#rpcinterfaceset_logger_level)
        - [RPCInterface().set_whitelist_blacklist](#rpcinterfaceset_whitelist_blacklist)
        - [RPCInterface().stream_blocks](#rpcinterfacestream_blocks)
        - [RPCInterface().update_runtime_options](#rpcinterfaceupdate_runtime_options)
    - [WalletClient](#walletclient)

## RPCInterface

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L8)

```python
class RPCInterface(HttpClient):
    def __init__(nodes=None, _async=False, **kwargs):
```

### RPCInterface().abi_bin_to_json

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L338)

```python
def abi_bin_to_json(code, action, binargs) -> dict:
```

Convert bin hex back into Abi json definition.

### RPCInterface().abi_json_to_bin

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L323)

```python
def abi_json_to_bin(code, action, args) -> dict:
```

Manually serialize json into binary hex.  The binayargs is usually stored in Message.data.

### RPCInterface().add_debug_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L580)

```python
def add_debug_contract(name, shared_lib_path) -> dict:
```

### RPCInterface().add_greylist_accounts

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L695)

```python
def add_greylist_accounts(accounts) -> dict:
```

### RPCInterface().call_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L354)

```python
def call_contract(code, action, args) -> dict:
```

Convert bin hex back into Abi json definition.

### RPCInterface().clear_debug_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L592)

```python
def clear_debug_contract(name) -> dict:
```

### RPCInterface().clear_filter_on

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L849)

```python
def clear_filter_on() -> dict:
```

### RPCInterface().clear_filter_out

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L859)

```python
def clear_filter_out() -> dict:
```

### RPCInterface().create_snapshot

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L771)

```python
def create_snapshot(head_block_id, snapshot_name) -> dict:
```

### RPCInterface().enable_debug

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L560)

```python
def enable_debug(enable) -> dict:
```

Retrieve supported apis.

### RPCInterface().get_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L169)

```python
def get_abi(account_name) -> dict:
```

Fetch a blockchain account

### RPCInterface().get_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L129)

```python
def get_account(account_name) -> dict:
```

Fetch a blockchain account

### RPCInterface().get_account_ram_corrections

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L812)

```python
def get_account_ram_corrections(
    lower_bound='',
    upper_bound='',
    limit=10,
) -> dict:
```

### RPCInterface().get_actions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L427)

```python
def get_actions(account_name, pos, offset) -> dict:
```

get_actions

### RPCInterface().get_activated_protocol_features

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L89)

```python
def get_activated_protocol_features(
    lower_bound=0,
    upper_bound=4294967295,
    limit=10,
    search_by_block_num=False,
    reverse=False,
):
```

### RPCInterface().get_block

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L103)

```python
def get_block(block_num_or_id) -> dict:
```

Fetch a block from the blockchain.

### RPCInterface().get_block_header_state

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L116)

```python
def get_block_header_state(block_num_or_id):
```

Fetch a block header state from the blockchain.

### RPCInterface().get_code

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L142)

```python
def get_code(account_name, code_as_wasm=True) -> dict:
```

Fetch smart contract code

### RPCInterface().get_code_hash

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L156)

```python
def get_code_hash(account_name) -> dict:
```

Fetch smart contract code

### RPCInterface().get_controlled_accounts

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L480)

```python
def get_controlled_accounts(controlling_account) -> dict:
```

Retrieve accounts has the specified key.

### RPCInterface().get_currency_balance

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L48)

```python
def get_currency_balance(code, account, symbol) -> dict:
```

get_currency_balance

### RPCInterface().get_currency_balance

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L254)

```python
def get_currency_balance(code, account, symbol) -> dict:
```

Get balance from an account.

### RPCInterface().get_currency_stats

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L63)

```python
def get_currency_stats(code, symbol) -> dict:
```

get_currency_stats

### RPCInterface().get_currency_stats

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L269)

```python
def get_currency_stats(code, symbol) -> dict:
```

### RPCInterface().get_db_size

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L500)

```python
def get_db_size() -> dict:
```

Retrieve accounts has the specified key.

### RPCInterface().get_greylist

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L719)

```python
def get_greylist() -> dict:
```

### RPCInterface().get_history_db_size

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L492)

```python
def get_history_db_size() -> dict:
```

### RPCInterface().get_info

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L77)

```python
def get_info() -> dict:
```

Return general network information.

### RPCInterface().get_integrity_hash

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L762)

```python
def get_integrity_hash() -> dict:
```

### RPCInterface().get_key_accounts

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L456)

```python
def get_key_accounts(public_key) -> dict:
```

Retrieve accounts has the specified key.

### RPCInterface().get_key_accounts_ex

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L468)

```python
def get_key_accounts_ex(public_key) -> dict:
```

Retrieve accounts has the specified key.

### RPCInterface().get_producer_schedule

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L298)

```python
def get_producer_schedule() -> dict:
```

### RPCInterface().get_producers

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L282)

```python
def get_producers(json, lower_bound, limit) -> dict:
```

Example: eosapi.get_producers(True, "", 100)

### RPCInterface().get_raw_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L195)

```python
def get_raw_abi(account_name, abi_hash=None) -> dict:
```

Fetch blockchain account abi info

### RPCInterface().get_raw_code_and_abi

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L182)

```python
def get_raw_code_and_abi(account_name) -> dict:
```

Fetch blockchain code and abi of an account

### RPCInterface().get_required_keys

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L369)

```python
def get_required_keys(transaction: Union[dict, str], available_keys) -> dict:
```

get_required_keys

### RPCInterface().get_runtime_options

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L641)

```python
def get_runtime_options():
```

### RPCInterface().get_scheduled_protocol_feature_activations

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L794)

```python
def get_scheduled_protocol_feature_activations() -> dict:
```

### RPCInterface().get_scheduled_transactions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L309)

```python
def get_scheduled_transactions(json, lower_bound, limit=50) -> dict:
```

### RPCInterface().get_supported_apis

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L550)

```python
def get_supported_apis() -> dict:
```

Retrieve supported apis.

### RPCInterface().get_supported_protocol_features

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L803)

```python
def get_supported_protocol_features(
    exclude_disabled=False,
    exclude_unactivatable=False,
) -> dict:
```

### RPCInterface().get_table_by_scope

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L237)

```python
def get_table_by_scope(code, table, lower_bound, upper_bound) -> dict:
```

Fetch smart contract data from an account.

### RPCInterface().get_table_rows

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L209)

```python
def get_table_rows(
    json,
    code,
    scope,
    table,
    lower_bound,
    upper_bound,
    limit,
    key_type='',
    index_position='',
    reverse=False,
    show_payer=False,
) -> dict:
```

 Fetch smart contract data from an account.
key_type: "i64"|"i128"|"i256"|"float64"|"float128"|"sha256"|"ripemd160"
index_position: "2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"10"

### RPCInterface().get_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L442)

```python
def get_transaction(id, block_num_hint=0) -> dict:
```

Retrieve a transaction from the blockchain.

### RPCInterface().get_whitelist_blacklist

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L729)

```python
def get_whitelist_blacklist() -> dict:
```

### RPCInterface().is_debug_enabled

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L570)

```python
def is_debug_enabled() -> dict:
```

### RPCInterface().net_connect

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L510)

```python
def net_connect(address) -> dict:
```

Connect to a node address.

### RPCInterface().net_connections

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L540)

```python
def net_connections() -> dict:
```

Get node connections.

### RPCInterface().net_disconnect

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L520)

```python
def net_disconnect(address) -> dict:
```

Disconnect from a node address.

### RPCInterface().net_status

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L530)

```python
def net_status(address) -> dict:
```

Retrieve connection status.

### RPCInterface().pause

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L617)

```python
def pause():
```

### RPCInterface().paused

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L633)

```python
def paused():
```

### RPCInterface().push_block

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L386)

```python
def push_block(block) -> dict:
```

Append a block to the chain database.

### RPCInterface().push_transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L399)

```python
def push_transaction(signed_transaction) -> dict:
```

Attempts to push the transaction into the pending queue.

### RPCInterface().push_transactions

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L408)

```python
def push_transactions(signed_transactions) -> dict:
```

Attempts to push transactions into the pending queue.

### RPCInterface().remove_greylist_accounts

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L707)

```python
def remove_greylist_accounts(accounts) -> dict:
```

### RPCInterface().resume

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L625)

```python
def resume():
```

### RPCInterface().schedule_protocol_feature_activations

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L783)

```python
def schedule_protocol_feature_activations(protocol_features) -> dict:
```

### RPCInterface().set_filter_on

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L825)

```python
def set_filter_on(filter_in) -> dict:
```

receiver:action:actor
* to pass all actions

### RPCInterface().set_filter_out

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L837)

```python
def set_filter_out(filter_out) -> dict:
```

receiver:action:actor
* to pass all action

### RPCInterface().set_logger_level

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L602)

```python
def set_logger_level(logger='default', level='info') -> dict:
```

logger: default
level: debug, info, warn, error, off

### RPCInterface().set_whitelist_blacklist

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L739)

```python
def set_whitelist_blacklist(
    actor_whitelist,
    actor_blacklist,
    contract_whitelist,
    contract_blacklist,
    action_blacklist,
    key_blacklist,
) -> dict:
```

fc::optional< flat_set<account_name> > actor_whitelist;
fc::optional< flat_set<account_name> > actor_blacklist;
fc::optional< flat_set<account_name> > contract_whitelist;
fc::optional< flat_set<account_name> > contract_blacklist;
fc::optional< flat_set< std::pair<account_name, action_name> > > action_blacklist;
fc::optional< flat_set<public_key_type> > key_blacklist;

### RPCInterface().stream_blocks

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L13)

```python
def stream_blocks(start_block=None, mode='irreversible'):
```

Stream raw blocks.

#### Arguments

- `start_block` *int* - Block number to start streaming from. If None,
                   head block is used.
- `mode` *str* - `irreversible` or `head`.

### RPCInterface().update_runtime_options

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L649)

```python
def update_runtime_options(
    max_transaction_time=None,
    max_irreversible_block_age=None,
    produce_time_offset_us=None,
    last_block_time_offset_us=None,
    max_scheduled_transaction_time_per_block_ms=None,
    subjective_cpu_leeway_us=None,
    incoming_defer_ratio=None,
) -> dict:
```

struct runtime_options {
    fc::optional<int32_t> max_transaction_time;
    fc::optional<int32_t> max_irreversible_block_age;
    fc::optional<int32_t> produce_time_offset_us;
    fc::optional<int32_t> last_block_time_offset_us;
    fc::optional<int32_t> max_scheduled_transaction_time_per_block_ms;
    fc::optional<int32_t> subjective_cpu_leeway_us;
    fc::optional<double>  incoming_defer_ratio;
};

## WalletClient

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/rpc_interface.py#L869)

```python
class WalletClient(HttpClient):
    def __init__(host='127.0.0.1', port=8888, **kwargs):
```
