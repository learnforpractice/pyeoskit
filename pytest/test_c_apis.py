import os
import sys
import time
import json
import pytest
import logging
from uuoskit import ABI

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from uuoskit.chainapi import ChainApi

class Test(object):

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_transaction(self):
        logger.info('hello,world')
        api = ChainApi('https://testnode.uuos.network:8443', 'UUOS')
        info = api.get_info()

        chain_id = info['chain_id']
        ref_block = info['last_irreversible_block_id']

        from uuoskit import _uuoskit
        _uuoskit.init()

        _uuoskit.wallet_import("test", "5JRYimgLBrRLCBAcjHUWCYRv3asNedTYYzVgmiU4q2ZVxMBiJXL")

        idx = _uuoskit.transaction_new(int(time.time()) + 60, ref_block, chain_id)
        pub = 'EOS6AjF6hvF7GSuSd4sCgfPKq5uWaXvGM2aQtEUCwmEHygQaqxBSV'

        transfer = {
            'from': 'helloworld11',
            'to': 'eosio',
            'quantity': '1.0000 EOS',
            'memo': 'transfer 1.0000 EOS from helloworld11 to eosio',
        }

        transfer = json.dumps(transfer)
        perms = {
            'helloworld11': 'active'
        }
        perms = json.dumps(perms)
        _uuoskit.transaction_add_action(idx, 'eosio.token', 'transfer', transfer, perms)
        r = _uuoskit.transaction_sign(idx, pub)
        logger.info(r)
        r = _uuoskit.transaction_pack(idx)
        logger.info(r)
        r = json.loads(r)
        logger.info(r)
        r = json.loads(r['data'])
        logger.info(r)

    def test_abi(self):
        from uuoskit import _uuoskit
        _uuoskit.init()

        with open('data/eosio.token.abi', 'rb') as f:
            abi = f.read()
        r = ABI.set_contract_abi("hello", abi)
        logger.info(r)
        transfer = {
            'from': 'helloworld11',
            'to': 'eosio',
            'quantity': '1.0000 EOS',
            'memo': 'transfer 1.0000 EOS from helloworld11 to eosio',
        }
        transfer = json.dumps(transfer)
        logger.info(transfer)

        r = ABI.pack_action_args('hello', 'transfer', transfer)
        logger.info(r)

        r = ABI.unpack_action_args('hello', 'transfer', r)
        logger.info(r)


        r = ABI.pack_abi_type('hello', 'transfer', transfer)
        logger.info(r)

        r = ABI.unpack_abi_type('hello', 'transfer', r)
        logger.info(r)
