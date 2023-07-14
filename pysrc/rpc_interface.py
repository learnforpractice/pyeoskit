import time
import json

from .http_client import HttpClient
from . import config
from typing import Dict, List, Union, Optional

class RPCInterface(HttpClient):
    def __init__(self, nodes=None, _async=False, **kwargs):
        nodes = nodes or config.nodes or ['http://127.0.0.1:8888']
        super().__init__(nodes=nodes, _async=_async, **kwargs)

    def stream_blocks(self, start_block=None, mode='irreversible'):
        """ Stream raw blocks.

        Args:
             start_block (int): Block number to start streaming from. If None,
                                head block is used.
             mode (str): `irreversible` or `head`.
        """
        mode = 'last_irreversible_block_num' if mode == 'irreversible' \
            else 'head_block_num'

        # convert block id to block number
        if type(start_block) == str:
            start_block = int(start_block[:8], base=16)

        if not start_block:
            start_block = self.get_info()[mode]

        block_interval = 3  # todo: confirm this assumption trough api

        while True:
            head_block = self.get_info()[mode]
            for block_num in range(start_block, head_block + 1):
                yield self.get_block(block_num)
            start_block = head_block + 1
            time.sleep(block_interval)

    ##############################
    # apigen.py generated methods
    # below this point
    ##############################

    # ---------------------------
    # /v1/chain/*
    # ---------------------------
    def get_currency_balance(self, code, account, symbol) -> Dict:
        """ get_currency_balance """

        body = dict(
            code=code,
            account=account,
            symbol=symbol,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_currency_balance',
            body=body
        )

    def get_currency_stats(self, code, symbol) -> Dict:
        """ get_currency_stats """

        body = dict(
            code=code,
            symbol=symbol,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_currency_stats',
            body=body
        )

    def get_info(self) -> Dict:
        """ Return general network information. """

        body = dict(
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_info',
            body=body
        )

    def get_activated_protocol_features(self, lower_bound=0, upper_bound=0xffffffff, limit=10, search_by_block_num=False, reverse=False):
        body = dict(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit = limit,
            search_by_block_num = search_by_block_num,
            reverse = reverse,
        )
        return self.rpc_request(
            api='chain',
            endpoint='get_activated_protocol_features',
            body=body
        )

    def get_block_trace(self, block_num) -> Dict:
        """ Fetch a block trace from the blockchain. """

        body = dict(
            block_num=block_num,
        )

        return self.rpc_request(
            api='trace_api',
            endpoint='get_block',
            body=body
        )

    def get_block(self, block_num_or_id) -> Dict:
        """ Fetch a block from the blockchain. """

        body = dict(
            block_num_or_id=block_num_or_id,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_block',
            body=body
        )
        
    def get_block_header_state(self, block_num_or_id):
        """ Fetch a block header state from the blockchain. """

        body = dict(
            block_num_or_id=block_num_or_id,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_block_header_state',
            body=body
        )

    def get_account(self, account_name) -> Dict:
        """ Fetch a blockchain account """

        body = dict(
            account_name=account_name,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_account',
            body=body
        )

    def get_code(self, account_name, code_as_wasm=True) -> Dict:
        """ Fetch smart contract code """

        body = dict(
            account_name=account_name,
            code_as_wasm=code_as_wasm,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_code',
            body=body
        )

    def get_code_hash(self, account_name) -> Dict:
        """ Fetch smart contract code """

        body = dict(
            account_name=account_name,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_code_hash',
            body=body
        )

    def get_abi(self, account_name) -> Dict:
        """ Fetch a blockchain account """

        body = dict(
            account_name=account_name,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_abi',
            body=body
        )

    def get_raw_code_and_abi(self, account_name) -> Dict:
        """ Fetch blockchain code and abi of an account """

        body = dict(
            account_name=account_name,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_raw_code_and_abi',
            body=body
        )

    def get_raw_abi(self, account_name, abi_hash=None) -> Dict:
        """ Fetch blockchain account abi info """

        body = dict(
            account_name=account_name,
            abi_hash=abi_hash
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_raw_abi',
            body=body
        )

    def get_table_rows(self, json, code, scope, table, lower_bound,
                       upper_bound, limit, key_type='', index_position='', encode_type='',
                       reverse = False, show_payer = False) -> Dict:
        """ Fetch smart contract data from an account. 
        key_type: "i64"|"i128"|"i256"|"float64"|"float128"|"sha256"|"ripemd160"
        index_position: "2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"10"
        encode_type: "dec" or "hex", default to "dec"
        """

        body = dict(
            json=json,
            code=code,
            scope=scope,
            table=table,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit=limit,
            key_type=key_type,
            index_position=index_position,
            encode_type=encode_type,
            reverse = False,
            show_payer = False
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_table_rows',
            body=body
        )

    def get_table_by_scope(self, code, table, lower_bound, upper_bound) -> Dict:
        """ Fetch smart contract data from an account. """

        body = dict(
            code=code,
            table=table,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit=10
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_table_by_scope',
            body=body
        )

    def get_currency_balance(self, code, account, symbol) -> Dict:
        """ Get balance from an account. """

        body = dict(
            code=code,
            account=account,
            symbol=symbol
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_currency_balance',
            body=body
        )

    def get_currency_stats(self, code, symbol) -> Dict:

        body = dict(
            code=code,
            symbol=symbol
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_currency_stats',
            body=body
        )

    def get_producers(self, json, lower_bound, limit) -> Dict:
        """
        Example: eosapi.get_producers(True, "", 100)
        """
        body = dict(
            json=json,
            lower_bound=lower_bound,
            limit=limit
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_producers',
            body=body
        )

    def get_producer_schedule(self) -> Dict:

        body = dict(
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_producer_schedule',
            body=body
        )

    def get_scheduled_transactions(self, json, lower_bound, limit=50) -> Dict:

        body = dict(
            json=json,
            lower_bound=lower_bound,
            limit=limit
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_scheduled_transactions',
            body=body
        )

    def abi_json_to_bin(self, code, action, args) -> Dict:
        """ Manually serialize json into binary hex.  The binayargs is usually stored in Message.data. """

        body = dict(
            code=code,
            action=action,
            args=args,
        )

        return self.rpc_request(
            api='chain',
            endpoint='abi_json_to_bin',
            body=body
        )

    def abi_bin_to_json(self, code, action, binargs) -> Dict:
        """ Convert bin hex back into Abi json definition. """

        body = dict(
            code=code,
            action=action,
            binargs=binargs,
        )

        return self.rpc_request(
            api='chain',
            endpoint='abi_bin_to_json',
            body=body
        )


    def call_contract(self, code, action, args) -> Dict:
        """ Convert bin hex back into Abi json definition. """

        body = dict(
            code=code,
            action=action,
            binargs=args,
        )

        return self.rpc_request(
            api='contract',
            endpoint='call_contract',
            body=body
        )

    def get_required_keys(self, transaction: Union[dict, str], available_keys) -> Dict:
        """ get_required_keys """
        if isinstance(transaction, str):
            transaction = json.loads(transaction)
        else:
            assert isinstance(transaction, dict)
        body = dict(
            transaction=transaction,
            available_keys=available_keys,
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_required_keys',
            body=body
        )

    def push_block(self, block) -> Dict:
        """ Append a block to the chain database. """

        body = dict(
            block=block,
        )

        return self.rpc_request(
            api='chain',
            endpoint='push_block',
            body=body
        )

    def push_transaction(self, signed_transaction) -> Dict:
        """ Attempts to push the transaction into the pending queue. """

        return self.rpc_request(
            api='chain',
            endpoint='push_transaction',
            body=signed_transaction
        )

    def push_transactions(self, signed_transactions) -> Dict:
        """ Attempts to push transactions into the pending queue. """
        trxs = []
        for trx in signed_transactions:
            if not isinstance(trx, dict):
                trx = json.loads(trx)
            trxs.append(trx)

        body = trxs

        return self.rpc_request(
            api='chain',
            endpoint='push_transactions',
            body=body
        )

    # ---------------------------
    # /v1/history/*
    # ---------------------------
    def get_actions(self, account_name, pos, offset) -> Dict:
        """ get_actions """

        body = dict(
            account_name=account_name,
            pos=pos,
            offset=offset,
        )

        return self.rpc_request(
            api='history',
            endpoint='get_actions',
            body=body
        )

    def get_transaction(self, id, block_num_hint=0) -> Dict:
        """ Retrieve a transaction from the blockchain. """

        body = dict(
            id=id,
            block_num_hint=block_num_hint
        )

        return self.rpc_request(
            api='history',
            endpoint='get_transaction',
            body=body
        )

    def get_key_accounts(self, public_key) -> Dict:
        """ Retrieve accounts has the specified key. """
        body = dict(
            public_key=public_key,
        )

        return self.rpc_request(
            api='history',
            endpoint='get_key_accounts',
            body=body
        )

    def get_key_accounts_ex(self, public_key) -> Dict:
        """ Retrieve accounts has the specified key. """
        body = dict(
            public_key=public_key,
        )

        return self.rpc_request(
            api='history',
            endpoint='get_key_accounts_ex',
            body=body
        )

    def get_accounts_by_authorizers(self, keys: Optional[List[str]], accounts: Optional[List[str]] = None) -> Dict:
        """
        example:
            get_accounts_by_authorizers([], [{'actor':'eosio', 'permission':'eosio.code'}])
        """
        if not keys and not accounts:
            raise Exception("keys and accounts are all empty")

        if keys is None:
            keys = []

        if accounts is None:
            accounts = []
        
        body = dict(
            accounts=accounts,
            keys=keys
        )

        return self.rpc_request(
            api='chain',
            endpoint='get_accounts_by_authorizers',
            body=body
        )

    def get_controlled_accounts(self, controlling_account) -> Dict:
        """ Retrieve accounts has the specified key. """
        body = dict(
            controlling_account=controlling_account,
        )

        return self.rpc_request(
            api='history',
            endpoint='get_controlled_accounts',
            body=body
        )

    def get_history_db_size(self) -> Dict:
        body = None
        return self.rpc_request(
            api='history',
            endpoint='get_db_size',
            body=body
        )

    def get_db_size(self) -> Dict:
        """ Retrieve accounts has the specified key. """
        body = dict()

        return self.rpc_request(
            api='db_size',
            endpoint='get',
            body=body
        )

    def net_connect(self, address) -> Dict:
        """ Connect to a node address. """
        body = json.dumps(address)

        return self.rpc_request(
            api='net',
            endpoint='connect',
            body=body
        )

    def net_disconnect(self, address) -> Dict:
        """ Disconnect from a node address. """
        body = json.dumps(address)

        return self.rpc_request(
            api='net',
            endpoint='disconnect',
            body=body
        )

    def net_status(self, address) -> Dict:
        """ Retrieve connection status. """
        body = json.dumps(address)

        return self.rpc_request(
            api='net',
            endpoint='status',
            body=body
        )

    def net_connections(self) -> Dict:
        """ Get node connections. """
        body = dict()

        return self.rpc_request(
            api='net',
            endpoint='connections',
            body=body
        )

    def get_supported_apis(self) -> Dict:
        """ Retrieve supported apis. """
        body = dict()

        return self.rpc_request(
            api='node',
            endpoint='get_supported_apis',
            body=body
        )

    def enable_debug(self, enable) -> Dict:
        """ Retrieve supported apis. """
        body = json.dumps(enable)

        return self.rpc_request(
            api='debug',
            endpoint='enable_debug',
            body=body
        )

    def is_debug_enabled(self) -> Dict:
        """  """
        body = dict()

        return self.rpc_request(
            api='debug',
            endpoint='is_debug_enabled',
            body=body
        )

    def add_debug_contract(self, name, shared_lib_path) -> Dict:
        """  """
        body = dict(
            name=name,
            path=shared_lib_path
        )
        return self.rpc_request(
            api='debug',
            endpoint='add_debug_contract',
            body=body
        )

    def clear_debug_contract(self, name) -> Dict:
        """ """
        body = json.dumps(name)

        return self.rpc_request(
            api='debug',
            endpoint='clear_debug_contract',
            body=body
        )

    def set_logger_level(self, logger='default', level='info') -> Dict:
        """
        logger: default
        level: debug, info, warn, error, off
        """
        body = dict(
            logger=logger,
            level = level
        )
        return self.rpc_request(
            api='debug',
            endpoint='set_logger_level',
            body=body
        )

    def pause(self):
        body = None
        return self.rpc_request(
            api='producer',
            endpoint='pause',
            body=body
        )

    def resume(self):
        body = None
        return self.rpc_request(
            api='producer',
            endpoint='resume',
            body=body
        )

    def paused(self):
        body = None
        return self.rpc_request(
            api='producer',
            endpoint='paused',
            body=body
        )

    def get_runtime_options(self):
        body = None
        return self.rpc_request(
            api='producer',
            endpoint='get_runtime_options',
            body=body
        )

    def update_runtime_options(self, max_transaction_time=None, 
                                    max_irreversible_block_age=None,
                                    produce_time_offset_us=None,
                                    last_block_time_offset_us=None,
                                    max_scheduled_transaction_time_per_block_ms=None,
                                    subjective_cpu_leeway_us=None,
                                    incoming_defer_ratio=None) -> Dict:
        '''
            struct runtime_options {
                fc::optional<int32_t> max_transaction_time;
                fc::optional<int32_t> max_irreversible_block_age;
                fc::optional<int32_t> produce_time_offset_us;
                fc::optional<int32_t> last_block_time_offset_us;
                fc::optional<int32_t> max_scheduled_transaction_time_per_block_ms;
                fc::optional<int32_t> subjective_cpu_leeway_us;
                fc::optional<double>  incoming_defer_ratio;
            };
        '''
        body = dict()
        if max_transaction_time is not None:
            body['max_transaction_time']=max_transaction_time

        if max_irreversible_block_age is not None:
            body['max_irreversible_block_age']=max_irreversible_block_age,

        if produce_time_offset_us is not None:
            body['produce_time_offset_us']=produce_time_offset_us,

        if last_block_time_offset_us is not None:
            body['last_block_time_offset_us']=last_block_time_offset_us

        if max_scheduled_transaction_time_per_block_ms is not None:
            body['max_scheduled_transaction_time_per_block_ms']=max_scheduled_transaction_time_per_block_ms,

        if subjective_cpu_leeway_us is not None:
            body['subjective_cpu_leeway_us']=subjective_cpu_leeway_us,

        if incoming_defer_ratio is not None:
            body['incoming_defer_ratio']=incoming_defer_ratio

        return self.rpc_request(
            api='producer',
            endpoint='update_runtime_options',
            body=body
        )

    def add_greylist_accounts(self, accounts) -> Dict:
        """ """
        body = dict(
            accounts=accounts
        )

        return self.rpc_request(
            api='producer',
            endpoint='add_greylist_accounts',
            body=body
        )

    def remove_greylist_accounts(self, accounts) -> Dict:
        """ """
        body = dict(
            accounts=accounts
        )

        return self.rpc_request(
            api='producer',
            endpoint='remove_greylist_accounts',
            body=body
        )

    def get_greylist(self) -> Dict:
        """ """
        body = None

        return self.rpc_request(
            api='producer',
            endpoint='get_greylist',
            body=body
        )

    def get_whitelist_blacklist(self) -> Dict:
        """ """
        body = None

        return self.rpc_request(
            api='producer',
            endpoint='get_whitelist_blacklist',
            body=body
        )

    def set_whitelist_blacklist(self, actor_whitelist, actor_blacklist, contract_whitelist, contract_blacklist, action_blacklist, key_blacklist) -> Dict:
        '''
        fc::optional< flat_set<account_name> > actor_whitelist;
        fc::optional< flat_set<account_name> > actor_blacklist;
        fc::optional< flat_set<account_name> > contract_whitelist;
        fc::optional< flat_set<account_name> > contract_blacklist;
        fc::optional< flat_set< std::pair<account_name, action_name> > > action_blacklist;
        fc::optional< flat_set<public_key_type> > key_blacklist;
        '''
        body = dict(
            actor_whitelist=actor_whitelist,
            actor_blacklist=actor_blacklist,
            contract_whitelist=contract_whitelist,
            contract_blacklist=contract_blacklist,
            action_blacklist=action_blacklist,
            key_blacklist=key_blacklist
        )
        return self.rpc_request(
            api='producer',
            endpoint='set_whitelist_blacklist',
            body=body
        )

    def get_integrity_hash(self) -> Dict:
        """  """
        body = None
        return self.rpc_request(
            api='producer',
            endpoint='get_integrity_hash',
            body=body
        )

    def create_snapshot(self, head_block_id="", snapshot_name="") -> Dict:
        """  """
        body = dict(
            head_block_id=head_block_id,
            snapshot_name=snapshot_name,
        )
        return self.rpc_request(
            api='producer',
            endpoint='create_snapshot',
            body=body
        )

    def schedule_protocol_feature_activations(self, protocol_features) -> Dict:
        """  """
        body = dict(
            protocol_features_to_activate=protocol_features,
        )
        return self.rpc_request(
            api='producer',
            endpoint='schedule_protocol_feature_activations',
            body=body
        )

    def get_scheduled_protocol_feature_activations(self) -> Dict:
        """  """
        body = dict()
        return self.rpc_request(
            api='producer',
            endpoint='get_scheduled_protocol_feature_activations',
            body=body
        )

    def get_supported_protocol_features(self, exclude_disabled=False, exclude_unactivatable=False) -> Dict:
        """  """
        body = dict(exclude_disabled=exclude_disabled, exclude_unactivatable=exclude_unactivatable)
        return self.rpc_request(
            api='producer',
            endpoint='get_supported_protocol_features',
            body=body
        )

    def get_account_ram_corrections(self, lower_bound='', upper_bound='', limit=10) -> Dict:
        """  """
        body = dict(
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit=limit,
        )
        return self.rpc_request(
            api='producer',
            endpoint='get_account_ram_corrections',
            body=body
        )

    def set_filter_on(self, filter_in) -> Dict:
        """
        receiver:action:actor
        * to pass all actions
        """
        body = json.dumps(filter_in)
        return self.rpc_request(
            api='action_publisher',
            endpoint='set_filter_on',
            body=body
        )

    def set_filter_out(self, filter_out) -> Dict:
        """
        receiver:action:actor
        * to pass all action
        """
        body = json.dumps(filter_out)
        return self.rpc_request(
            api='action_publisher',
            endpoint='set_filter_out',
            body=body
        )

    def clear_filter_on(self) -> Dict:
        """
        """
        body = None
        return self.rpc_request(
            api='action_publisher',
            endpoint='clear_filter_on',
            body=body
        )

    def clear_filter_out(self) -> Dict:
        """
        """
        body = None
        return self.rpc_request(
            api='action_publisher',
            endpoint='clear_filter_out',
            body=body
        )

class WalletClient(HttpClient):
    def __init__(self, host='127.0.0.1', port=8888, **kwargs):
        hostname = host.split('//')[-1].split(':')[0]
        if hostname not in ['localhost', '127.0.0.1']:
            import warnings
            warnings.warn("Using the wallet API on {} might be insecure!".format(hostname))

        protocol = 'http'
        if host.split(':')[0] == 'https' or kwargs.get('https'):
            protocol = 'https'
        nodes = ["{}://{}:{}".format(protocol, hostname, port).rstrip(':')]
        super().__init__(nodes=nodes, **kwargs)

        # TODO: API gen wallet methods


if __name__ == '__main__':
    client = RPCInterface(['http://127.0.0.1:8888'])
