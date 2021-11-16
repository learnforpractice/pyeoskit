import os
import sys
import time
import pytest
import logging
import asyncio

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from pyeoskit.chainapi import ChainApi, ChainApiAsync
from pyeoskit import eosapi, wallet, config

@pytest.fixture
def event_loop():
    pass

g_abi = r'''{
    "version": "eosio::abi/1.0",
    "types": [],
    "structs": [
    ],
    "actions": [],
    "tables": [],
    "ricardian_clauses": [],
    "error_messages": [],
    "abi_extensions": []
}'''

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

    def test_set_code_get_code(self):
        api = ChainApi('http://127.0.0.1:8888')
        api.set_code('hello', b'abc')
        assert api.get_code('hello') == b'abc'

    def test_set_code_get_code_async(self):
        async def set_code_get_code_async():
            api = ChainApiAsync('http://127.0.0.1:8888')
            api.set_code('hello', b'abc')
            assert await api.get_code('hello') == b'abc'

        loop = asyncio.get_event_loop()
        loop.run_until_complete(set_code_get_code_async())

    def test_set_contract(self):

        if os.path.exists('test.wallet'):
            os.remove('test.wallet')
        psw = wallet.create('test')
        wallet.import_key('test', '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo')

        #eosapi.set_nodes(['https://nodes.uuos.network:8443'])
        eosapi.set_node('http://127.0.0.1:8888')
        eosapi.db.reset()

        account_name = 'helloworld11'

        code = '''
def apply(receiver, code, action):
    print('hello,worldd')
'''
        code = eosapi.compile(account_name, code, 1)
        r = eosapi.deploy_contract(account_name, code, g_abi, 1)
        print('done!')

    def test_set_contract_async(self):
        async def set_contract_async():
            if os.path.exists('test.wallet'):
                os.remove('test.wallet')
            psw = wallet.create('test')
            wallet.import_key('test', '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo')

            #eosapi.set_nodes(['https://nodes.uuos.network:8443'])
            api = ChainApiAsync('http://127.0.0.1:8888', 'UUOS')
            account_name = 'helloworld11'

            code = '''
def apply(receiver, code, action):
    print('hello,world, async')
'''
            code = await api.compile(account_name, code, 1)
            r = await api.deploy_contract(account_name, code, g_abi, 1)
            print('done!')

        loop = asyncio.get_event_loop()
        loop.run_until_complete(set_contract_async())

    def test_get_abi_sync(self):
        async def get_abi(account):
            return 'hellooo'
        loop = asyncio.get_event_loop()
        ret = loop.run_until_complete(get_abi('hello'))
        logger.info('+++++ret:%s', ret)
        assert ret == 'hellooo'
