import time
import json

from .http_client import HttpClient
from . import config

class Client(HttpClient):
    def __init__(self, nodes=None, **kwargs):
        nodes =nodes or config.nodes or ['http://127.0.0.1:8888']
        super().__init__(nodes=nodes, **kwargs)

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
    def get_currency_balance(self, code, account, symbol) -> dict:
        """ get_currency_balance """

        body = dict(
            code=code,
            account=account,
            symbol=symbol,
        )

        return self.exec(
            api='chain',
            endpoint='get_currency_balance',
            body=body
        )

    def get_currency_stats(self, code, symbol) -> dict:
        """ get_currency_stats """

        body = dict(
            code=code,
            symbol=symbol,
        )

        return self.exec(
            api='chain',
            endpoint='get_currency_stats',
            body=body
        )

    def get_info(self) -> dict:
        """ Return general network information. """

        body = dict(
        )

        return self.exec(
            api='chain',
            endpoint='get_info',
            body=body
        )

    def get_block(self, block_num_or_id) -> dict:
        """ Fetch a block from the blockchain. """

        body = dict(
            block_num_or_id=block_num_or_id,
        )

        return self.exec(
            api='chain',
            endpoint='get_block',
            body=body
        )
        
    def get_block_header_state(self, block_num_or_id):
        """ Fetch a block header state from the blockchain. """

        body = dict(
            block_num_or_id=block_num_or_id,
        )

        return self.exec(
            api='chain',
            endpoint='get_block_header_state',
            body=body
        )

    def get_account(self, account_name) -> dict:
        """ Fetch a blockchain account """

        body = dict(
            account_name=account_name,
        )

        return self.exec(
            api='chain',
            endpoint='get_account',
            body=body
        )

    def get_code(self, account_name, code_as_wasm=True) -> dict:
        """ Fetch smart contract code """

        body = dict(
            account_name=account_name,
            code_as_wasm=code_as_wasm,
        )

        return self.exec(
            api='chain',
            endpoint='get_code',
            body=body
        )

    def get_abi(self, account_name) -> dict:
        """ Fetch a blockchain account """

        body = dict(
            account_name=account_name,
        )

        return self.exec(
            api='chain',
            endpoint='get_abi',
            body=body
        )

    def get_raw_code_and_abi(self, account_name) -> dict:
        """ Fetch blockchain code and abi of an account """

        body = dict(
            account_name=account_name,
        )

        return self.exec(
            api='chain',
            endpoint='get_raw_code_and_abi',
            body=body
        )

    def get_raw_abi(self, account_name, abi_hash=None) -> dict:
        """ Fetch blockchain account abi info """

        body = dict(
            account_name=account_name,
            abi_hash=abi_hash
        )

        return self.exec(
            api='chain',
            endpoint='get_raw_abi',
            body=body
        )

    def get_table_rows(self, json, code, scope, table, table_key, lower_bound,
                       upper_bound, limit, encode_type='dec') -> dict:
        """ Fetch smart contract data from an account. """

        body = dict(
            json=json,
            code=code,
            scope=scope,
            table=table,
            table_key=table_key,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit=limit,
            encode_type=encode_type
        )

        return self.exec(
            api='chain',
            endpoint='get_table_rows',
            body=body
        )

    def get_table_by_scope(self, code, table, lower_bound, upper_bound) -> dict:
        """ Fetch smart contract data from an account. """

        body = dict(
            code=code,
            table=table,
            lower_bound=lower_bound,
            upper_bound=upper_bound,
            limit=10
        )

        return self.exec(
            api='chain',
            endpoint='get_table_by_scope',
            body=body
        )

    def get_currency_balance(self, code, account, symbol) -> dict:
        """ Get balance from an account. """

        body = dict(
            code=code,
            account=account,
            symbol=symbol
        )

        return self.exec(
            api='chain',
            endpoint='get_currency_balance',
            body=body
        )

    def get_currency_stats(self, code, symbol) -> dict:

        body = dict(
            code=code,
            symbol=symbol
        )

        return self.exec(
            api='chain',
            endpoint='get_currency_stats',
            body=body
        )

    def get_producers(self, json, lower_bound, limit) -> dict:
        """
        Example: eosapi.get_producers(True, "", 100)
        """
        body = dict(
            json=json,
            lower_bound=lower_bound,
            limit=limit
        )

        return self.exec(
            api='chain',
            endpoint='get_producers',
            body=body
        )

    def get_producer_schedule(self) -> dict:

        body = dict(
        )

        return self.exec(
            api='chain',
            endpoint='get_producer_schedule',
            body=body
        )

    def get_scheduled_transactions(self, json, lower_bound) -> dict:

        body = dict(
            json=json,
            lower_bound=lower_bound,
            limit=50
        )

        return self.exec(
            api='chain',
            endpoint='get_scheduled_transactions',
            body=body
        )

    def abi_json_to_bin(self, code, action, args) -> dict:
        """ Manually serialize json into binary hex.  The binayargs is usually stored in Message.data. """

        body = dict(
            code=code,
            action=action,
            args=args,
        )

        return self.exec(
            api='chain',
            endpoint='abi_json_to_bin',
            body=body
        )

    def abi_bin_to_json(self, code, action, binargs) -> dict:
        """ Convert bin hex back into Abi json definition. """

        body = dict(
            code=code,
            action=action,
            binargs=binargs,
        )

        return self.exec(
            api='chain',
            endpoint='abi_bin_to_json',
            body=body
        )

    def get_required_keys(self, transaction, available_keys) -> dict:
        """ get_required_keys """

        body = dict(
            transaction=transaction,
            available_keys=available_keys,
        )

        return self.exec(
            api='chain',
            endpoint='get_required_keys',
            body=body
        )

    def push_block(self, block) -> dict:
        """ Append a block to the chain database. """

        body = dict(
            block=block,
        )

        return self.exec(
            api='chain',
            endpoint='push_block',
            body=body
        )

    def push_transaction(self, signed_transaction) -> dict:
        """ Attempts to push the transaction into the pending queue. """
        if not isinstance(signed_transaction, dict):
            signed_transaction = json.loads(signed_transaction)
        body = dict(
            signed_transaction
        )
        return self.exec(
            api='chain',
            endpoint='push_transaction',
            body=body
        )

    def push_transactions(self, signed_transactions) -> dict:
        """ Attempts to push transactions into the pending queue. """
        trxs = []
        for trx in signed_transactions:
            if not isinstance(trx, dict):
                trx = json.loads(trx)
            trxs.append(trx)

        body = trxs

        return self.exec(
            api='chain',
            endpoint='push_transactions',
            body=body
        )

    # ---------------------------
    # /v1/history/*
    # ---------------------------
    def get_actions(self, account_name, pos, offset) -> dict:
        """ get_actions """

        body = dict(
            account_name=account_name,
            pos=pos,
            offset=offset,
        )

        return self.exec(
            api='history',
            endpoint='get_actions',
            body=body
        )

    def get_transaction(self, id) -> dict:
        """ Retrieve a transaction from the blockchain. """

        body = dict(
            id=id,
        )

        return self.exec(
            api='history',
            endpoint='get_transaction',
            body=body
        )

    def get_key_accounts(self, public_key) -> dict:
        """ Retrieve accounts has the specified key. """
        body = dict(
            public_key=public_key,
        )

        return self.exec(
            api='history',
            endpoint='get_key_accounts',
            body=body
        )

    def get_controlled_accounts(self, controlling_account) -> dict:
        """ Retrieve accounts has the specified key. """
        body = dict(
            controlling_account=controlling_account,
        )

        return self.exec(
            api='history',
            endpoint='get_controlled_accounts',
            body=body
        )

    def get_db_size(self) -> dict:
        """ Retrieve accounts has the specified key. """
        body = dict()

        return self.exec(
            api='db_size',
            endpoint='get',
            body=body
        )

    def net_connect(self, address) -> dict:
        """ Connect to a node address. """
        body = json.dumps(address)

        return self.exec(
            api='net',
            endpoint='connect',
            body=body
        )

    def net_disconnect(self, address) -> dict:
        """ Disconnect from a node address. """
        body = json.dumps(address)

        return self.exec(
            api='net',
            endpoint='disconnect',
            body=body
        )

    def net_status(self, address) -> dict:
        """ Retrieve connection status. """
        body = json.dumps(address)

        return self.exec(
            api='net',
            endpoint='status',
            body=body
        )

    def net_connections(self) -> dict:
        """ Get node connections. """
        body = dict()

        return self.exec(
            api='net',
            endpoint='connections',
            body=body
        )

    def get_supported_apis(self) -> dict:
        """ Retrieve supported apis. """
        body = dict()

        return self.exec(
            api='node',
            endpoint='get_supported_apis',
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
    client = Client(['http://127.0.0.1:8888'])
