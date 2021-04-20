# Client

> Auto-generated documentation for [pysrc.client](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py) module.

- [Uuoskit](../README.md#uuoskit-index) / [Modules](../MODULES.md#uuoskit-modules) / [Pysrc](index.md#pysrc) / Client
    - [Client](#client)
        - [Client().abi_bin_to_json](#clientabi_bin_to_json)
        - [Client().abi_json_to_bin](#clientabi_json_to_bin)
        - [Client().add_debug_contract](#clientadd_debug_contract)
        - [Client().add_greylist_accounts](#clientadd_greylist_accounts)
        - [Client().call_contract](#clientcall_contract)
        - [Client().clear_debug_contract](#clientclear_debug_contract)
        - [Client().clear_filter_on](#clientclear_filter_on)
        - [Client().clear_filter_out](#clientclear_filter_out)
        - [Client().create_snapshot](#clientcreate_snapshot)
        - [Client().enable_debug](#clientenable_debug)
        - [Client().get_abi](#clientget_abi)
        - [Client().get_account](#clientget_account)
        - [Client().get_account_ram_corrections](#clientget_account_ram_corrections)
        - [Client().get_actions](#clientget_actions)
        - [Client().get_activated_protocol_features](#clientget_activated_protocol_features)
        - [Client().get_block](#clientget_block)
        - [Client().get_block_header_state](#clientget_block_header_state)
        - [Client().get_code](#clientget_code)
        - [Client().get_code_hash](#clientget_code_hash)
        - [Client().get_controlled_accounts](#clientget_controlled_accounts)
        - [Client().get_currency_balance](#clientget_currency_balance)
        - [Client().get_currency_balance](#clientget_currency_balance)
        - [Client().get_currency_stats](#clientget_currency_stats)
        - [Client().get_currency_stats](#clientget_currency_stats)
        - [Client().get_db_size](#clientget_db_size)
        - [Client().get_greylist](#clientget_greylist)
        - [Client().get_history_db_size](#clientget_history_db_size)
        - [Client().get_info](#clientget_info)
        - [Client().get_integrity_hash](#clientget_integrity_hash)
        - [Client().get_key_accounts](#clientget_key_accounts)
        - [Client().get_key_accounts_ex](#clientget_key_accounts_ex)
        - [Client().get_producer_schedule](#clientget_producer_schedule)
        - [Client().get_producers](#clientget_producers)
        - [Client().get_raw_abi](#clientget_raw_abi)
        - [Client().get_raw_code_and_abi](#clientget_raw_code_and_abi)
        - [Client().get_required_keys](#clientget_required_keys)
        - [Client().get_runtime_options](#clientget_runtime_options)
        - [Client().get_scheduled_protocol_feature_activations](#clientget_scheduled_protocol_feature_activations)
        - [Client().get_scheduled_transactions](#clientget_scheduled_transactions)
        - [Client().get_supported_apis](#clientget_supported_apis)
        - [Client().get_supported_protocol_features](#clientget_supported_protocol_features)
        - [Client().get_table_by_scope](#clientget_table_by_scope)
        - [Client().get_table_rows](#clientget_table_rows)
        - [Client().get_transaction](#clientget_transaction)
        - [Client().get_whitelist_blacklist](#clientget_whitelist_blacklist)
        - [Client().is_debug_enabled](#clientis_debug_enabled)
        - [Client().net_connect](#clientnet_connect)
        - [Client().net_connections](#clientnet_connections)
        - [Client().net_disconnect](#clientnet_disconnect)
        - [Client().net_status](#clientnet_status)
        - [Client().pause](#clientpause)
        - [Client().paused](#clientpaused)
        - [Client().push_block](#clientpush_block)
        - [Client().push_transaction](#clientpush_transaction)
        - [Client().push_transactions](#clientpush_transactions)
        - [Client().remove_greylist_accounts](#clientremove_greylist_accounts)
        - [Client().resume](#clientresume)
        - [Client().schedule_protocol_feature_activations](#clientschedule_protocol_feature_activations)
        - [Client().set_filter_on](#clientset_filter_on)
        - [Client().set_filter_out](#clientset_filter_out)
        - [Client().set_logger_level](#clientset_logger_level)
        - [Client().set_whitelist_blacklist](#clientset_whitelist_blacklist)
        - [Client().stream_blocks](#clientstream_blocks)
        - [Client().update_runtime_options](#clientupdate_runtime_options)
    - [WalletClient](#walletclient)

## Client

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L7)

```python
class Client(HttpClient):
    def __init__(nodes=None, _async=False, **kwargs):
```

### Client().abi_bin_to_json

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L336)

```python
def abi_bin_to_json(code, action, binargs) -> dict:
```

Convert bin hex back into Abi json definition.

### Client().abi_json_to_bin

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L321)

```python
def abi_json_to_bin(code, action, args) -> dict:
```

Manually serialize json into binary hex.  The binayargs is usually stored in Message.data.

### Client().add_debug_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L579)

```python
def add_debug_contract(name, shared_lib_path) -> dict:
```

### Client().add_greylist_accounts

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L694)

```python
def add_greylist_accounts(accounts) -> dict:
```

### Client().call_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L352)

```python
def call_contract(code, action, args) -> dict:
```

Convert bin hex back into Abi json definition.

### Client().clear_debug_contract

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L591)

```python
def clear_debug_contract(name) -> dict:
```

### Client().clear_filter_on

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L848)

```python
def clear_filter_on() -> dict:
```

### Client().clear_filter_out

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L858)

```python
def clear_filter_out() -> dict:
```

### Client().create_snapshot

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L770)

```python
def create_snapshot(head_block_id, snapshot_name) -> dict:
```

### Client().enable_debug

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L559)

```python
def enable_debug(enable) -> dict:
```

Retrieve supported apis.

### Client().get_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L168)

```python
def get_abi(account_name) -> dict:
```

Fetch a blockchain account

### Client().get_account

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L128)

```python
def get_account(account_name) -> dict:
```

Fetch a blockchain account

### Client().get_account_ram_corrections

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L811)

```python
def get_account_ram_corrections(
    lower_bound='',
    upper_bound='',
    limit=10,
) -> dict:
```

### Client().get_actions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L426)

```python
def get_actions(account_name, pos, offset) -> dict:
```

get_actions

### Client().get_activated_protocol_features

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L88)

```python
def get_activated_protocol_features(
    lower_bound=0,
    upper_bound=4294967295,
    limit=10,
    search_by_block_num=False,
    reverse=False,
):
```

### Client().get_block

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L102)

```python
def get_block(block_num_or_id) -> dict:
```

Fetch a block from the blockchain.

### Client().get_block_header_state

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L115)

```python
def get_block_header_state(block_num_or_id):
```

Fetch a block header state from the blockchain.

### Client().get_code

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L141)

```python
def get_code(account_name, code_as_wasm=True) -> dict:
```

Fetch smart contract code

### Client().get_code_hash

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L155)

```python
def get_code_hash(account_name) -> dict:
```

Fetch smart contract code

### Client().get_controlled_accounts

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L479)

```python
def get_controlled_accounts(controlling_account) -> dict:
```

Retrieve accounts has the specified key.

### Client().get_currency_balance

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L47)

```python
def get_currency_balance(code, account, symbol) -> dict:
```

get_currency_balance

### Client().get_currency_balance

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L252)

```python
def get_currency_balance(code, account, symbol) -> dict:
```

Get balance from an account.

### Client().get_currency_stats

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L62)

```python
def get_currency_stats(code, symbol) -> dict:
```

get_currency_stats

### Client().get_currency_stats

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L267)

```python
def get_currency_stats(code, symbol) -> dict:
```

### Client().get_db_size

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L499)

```python
def get_db_size() -> dict:
```

Retrieve accounts has the specified key.

### Client().get_greylist

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L718)

```python
def get_greylist() -> dict:
```

### Client().get_history_db_size

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L491)

```python
def get_history_db_size() -> dict:
```

### Client().get_info

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L76)

```python
def get_info() -> dict:
```

Return general network information.

### Client().get_integrity_hash

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L761)

```python
def get_integrity_hash() -> dict:
```

### Client().get_key_accounts

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L455)

```python
def get_key_accounts(public_key) -> dict:
```

Retrieve accounts has the specified key.

### Client().get_key_accounts_ex

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L467)

```python
def get_key_accounts_ex(public_key) -> dict:
```

Retrieve accounts has the specified key.

### Client().get_producer_schedule

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L296)

```python
def get_producer_schedule() -> dict:
```

### Client().get_producers

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L280)

```python
def get_producers(json, lower_bound, limit) -> dict:
```

Example: uuosapi.get_producers(True, "", 100)

### Client().get_raw_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L194)

```python
def get_raw_abi(account_name, abi_hash=None) -> dict:
```

Fetch blockchain account abi info

### Client().get_raw_code_and_abi

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L181)

```python
def get_raw_code_and_abi(account_name) -> dict:
```

Fetch blockchain code and abi of an account

### Client().get_required_keys

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L367)

```python
def get_required_keys(transaction, available_keys) -> dict:
```

get_required_keys

### Client().get_runtime_options

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L640)

```python
def get_runtime_options():
```

### Client().get_scheduled_protocol_feature_activations

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L793)

```python
def get_scheduled_protocol_feature_activations() -> dict:
```

### Client().get_scheduled_transactions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L307)

```python
def get_scheduled_transactions(json, lower_bound, limit=50) -> dict:
```

### Client().get_supported_apis

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L549)

```python
def get_supported_apis() -> dict:
```

Retrieve supported apis.

### Client().get_supported_protocol_features

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L802)

```python
def get_supported_protocol_features(
    exclude_disabled=False,
    exclude_unactivatable=False,
) -> dict:
```

### Client().get_table_by_scope

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L235)

```python
def get_table_by_scope(code, table, lower_bound, upper_bound) -> dict:
```

Fetch smart contract data from an account.

### Client().get_table_rows

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L208)

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
    encode_type='dec',
) -> dict:
```

 Fetch smart contract data from an account.
key_type: "i64"|"i128"|"i256"|"float64"|"float128"|"sha256"|"ripemd160"
index_position: "2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"10"

### Client().get_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L441)

```python
def get_transaction(id, block_num_hint=0) -> dict:
```

Retrieve a transaction from the blockchain.

### Client().get_whitelist_blacklist

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L728)

```python
def get_whitelist_blacklist() -> dict:
```

### Client().is_debug_enabled

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L569)

```python
def is_debug_enabled() -> dict:
```

### Client().net_connect

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L509)

```python
def net_connect(address) -> dict:
```

Connect to a node address.

### Client().net_connections

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L539)

```python
def net_connections() -> dict:
```

Get node connections.

### Client().net_disconnect

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L519)

```python
def net_disconnect(address) -> dict:
```

Disconnect from a node address.

### Client().net_status

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L529)

```python
def net_status(address) -> dict:
```

Retrieve connection status.

### Client().pause

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L616)

```python
def pause():
```

### Client().paused

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L632)

```python
def paused():
```

### Client().push_block

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L381)

```python
def push_block(block) -> dict:
```

Append a block to the chain database.

### Client().push_transaction

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L394)

```python
def push_transaction(signed_transaction) -> dict:
```

Attempts to push the transaction into the pending queue.

### Client().push_transactions

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L407)

```python
def push_transactions(signed_transactions) -> dict:
```

Attempts to push transactions into the pending queue.

### Client().remove_greylist_accounts

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L706)

```python
def remove_greylist_accounts(accounts) -> dict:
```

### Client().resume

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L624)

```python
def resume():
```

### Client().schedule_protocol_feature_activations

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L782)

```python
def schedule_protocol_feature_activations(protocol_features) -> dict:
```

### Client().set_filter_on

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L824)

```python
def set_filter_on(filter_in) -> dict:
```

receiver:action:actor
* to pass all actions

### Client().set_filter_out

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L836)

```python
def set_filter_out(filter_out) -> dict:
```

receiver:action:actor
* to pass all action

### Client().set_logger_level

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L601)

```python
def set_logger_level(logger='default', level='info') -> dict:
```

logger: default
level: debug, info, warn, error, off

### Client().set_whitelist_blacklist

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L738)

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

### Client().stream_blocks

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L12)

```python
def stream_blocks(start_block=None, mode='irreversible'):
```

Stream raw blocks.

#### Arguments

- `start_block` *int* - Block number to start streaming from. If None,
                   head block is used.
- `mode` *str* - `irreversible` or `head`.

### Client().update_runtime_options

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L648)

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

[[find in source code]](https://github.com/uuosio/UUOSKit/blob/master/pysrc/client.py#L868)

```python
class WalletClient(HttpClient):
    def __init__(host='127.0.0.1', port=8888, **kwargs):
```
