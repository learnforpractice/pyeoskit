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

config.setup_uuos_network()

uuosapi = None

class TestUUOSApi(object):

    @classmethod
    def setup_class(cls):
        global uuosapi
        uuosapi = ChainApiAsync('http://127.0.0.1:9000')

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
        uuosapi.clear_abi_cache('eosio.token')
        args = {
            'from': 'test1',
            'to': 'test2',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        r = uuosapi.pack_args('eosio.token', 'transfer', args)
        assert r

        r = uuosapi.pack_args('eosio.token', 'transfer', json.dumps(args))
        assert r

        r = uuosapi.unpack_args('eosio.token', 'transfer', r)
        logger.info(r)

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', {'a':1})

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', json.dumps({'a':1}))

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', b'hello')

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', 'aabb')

