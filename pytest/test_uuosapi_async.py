import os
import sys
import time
import json
import pytest
import logging
import hashlib
from uuoskit import config, wallet
from uuoskit.chainapi import ChainApiAsync
from uuoskit.exceptions import ChainException, WalletException

from uuoskit.testnet import Testnet

from uuosio import uuos


Testnet.__test__ = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)

# config.main_token = 'UUOS'
# config.main_token_contract = 'uuos.token'
# config.system_contract = 'uuos'

# uuosapi.set_node('http://127.0.0.1:8899')

# config.setup_uuos_network()


class TestUUOSApi(object):

    @classmethod
    def setup_class(cls):
        cls.uuosapi = ChainApiAsync('http://127.0.0.1:9000')

        cls.testnet = Testnet(single_node=True, show_log=True)
        cls.testnet.run()

        # wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')
        # wallet.import_key('mywallet', '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo')

    @classmethod
    def teardown_class(cls):
        cls.testnet.stop()
        cls.testnet.cleanup()

    def setup_method(self, method):
        global uuosapi_async
        uuosapi_async = ChainApiAsync('http://127.0.0.1:9000')

    def teardown_method(self, method):
        pass

    @pytest.mark.asyncio
    async def test_pack_unpack_args(self):
        self.uuosapi.clear_abi_cache('eosio.token')
        args = {
            'from': 'test1',
            'to': 'test2',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        r = self.uuosapi.pack_args('eosio.token', 'transfer', args)
        assert r

        r = self.uuosapi.pack_args('eosio.token', 'transfer', json.dumps(args))
        assert r

        r = self.uuosapi.unpack_args('eosio.token', 'transfer', r)
        logger.info(r)

        with pytest.raises(Exception):
            r = self.uuosapi.unpack_args('eosio.token', 'transfer', {'a':1})

        with pytest.raises(Exception):
            r = self.uuosapi.unpack_args('eosio.token', 'transfer', json.dumps({'a':1}))

        with pytest.raises(Exception):
            r = self.uuosapi.unpack_args('eosio.token', 'transfer', b'hello')

        with pytest.raises(Exception):
            r = self.uuosapi.unpack_args('eosio.token', 'transfer', 'aabb')


    @pytest.mark.asyncio
    async def test_get_required_keys(self):
        args = {
            'from': 'helloworld11',
            'to': 'helloworld12',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        act = ['eosio.token', 'transfer', args, {'helloworld11': 'active'}]
        chain_info = await self.uuosapi.get_info()
        reference_block_id = chain_info['head_block_id']
        trx = self.uuosapi.generate_transaction([act], 60, reference_block_id)
        keys = await self.uuosapi.get_required_keys(trx, wallet.get_public_keys())
        assert keys

        chain_id = chain_info['chain_id']
        trx = wallet.sign_transaction(trx, keys, chain_id, json=True)
        assert trx['signatures']
        logger.info(trx)

    @pytest.mark.asyncio
    async def test_push_action(self):
        r = await self.uuosapi.push_action('helloworld11', 'sayhello', b'hello')
