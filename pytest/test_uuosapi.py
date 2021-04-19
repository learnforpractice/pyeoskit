import os
import sys
import time
import pytest
import logging
import hashlib
from uuoskit import uuosapi, config, wallet
from uuoskit.chainapi import ChainApiAsync
from uuoskit.exceptions import ChainException, WalletException

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)

config.main_token = 'UUOS'
config.main_token_contract = 'uuos.token'
config.system_contract = 'uuos'

uuosapi.set_node('http://127.0.0.1:8899')

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

uuosapi_async = ChainApiAsync('https://eos.greymass.com')

class TestUUOSApi(object):

    @classmethod
    def setup_class(cls):
        uuosapi.set_node('https://eos.greymass.com')
        cls.info = uuosapi.get_info()

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_gen_transaction(self):
        args = {
            'from': 'alice',
            'to': 'bob',
            'quantity': '1.0000 EOS',
            'memo': 'hello,world'
        }
        a = ['eosio.token', 'transfer', args, {'alice': 'active'}]
        r = uuosapi.gen_transaction([a], 60, self.info['last_irreversible_block_id'])
        logger.info(r)
        assert r

        r = uuosapi_async.gen_transaction([a], 60, self.info['last_irreversible_block_id'])
        logger.info(r)
        assert r


        args = {
            'from': 'alice',
            'to': 'bob',
            'quantity': '1.0000 EOS',
            'typo_memo': 'hello,world'
        }
        a = ['eosio.token', 'transfer', args, {'alice': 'active'}]

        with pytest.raises(Exception):
            r = uuosapi.gen_transaction([a], 60, self.info['last_irreversible_block_id'])

        with pytest.raises(Exception):
            r = uuosapi_async.gen_transaction([a], 60, self.info['last_irreversible_block_id'])

    @pytest.mark.asyncio
    async def test_sign_transaction(self):
        trx = '{"expiration":"2021-04-13T04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        priv_key = '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p'
        r = uuosapi.sign_transaction(trx, priv_key, self.info['chain_id'])
        logger.info(r)
        r = uuosapi_async.sign_transaction(trx, priv_key, self.info['chain_id'])

        trx = '{"expiration":"2021-04-13t04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        priv_key = '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p'
        with pytest.raises(Exception):
            r = uuosapi.sign_transaction(trx, priv_key, self.info['chain_id'])
            logger.info(r)

        with pytest.raises(Exception):
            uuosapi_async.sign_transaction(trx, priv_key, self.info['chain_id'])

    @pytest.mark.asyncio
    async def test_pack_transaction(self):
        trx = '{"expiration":"2021-04-13T04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        r = uuosapi.pack_transaction(trx, True)
        logger.info(r)
        assert r

        r = uuosapi.pack_transaction(trx, False)
        logger.info(r)
        assert r

        r = uuosapi_async.pack_transaction(trx, True)
        logger.info(r)
        assert r

        r = uuosapi_async.pack_transaction(trx, False)
        logger.info(r)
        assert r

    @pytest.mark.asyncio
    async def test_basic(self):
        priv_key = '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p'
        pub = uuosapi.get_public_key(priv_key)
        logger.info(pub)
        assert pub == 'EOS8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr'

        key = uuosapi.create_key()
        logger.info(key)
        assert key

    @pytest.mark.asyncio
    async def test_get_table_rows(self):
        symbol = uuosapi.string_to_symbol(4, 'EOS')
        symbol_code = symbol >> 8
        symbol_code = uuosapi.n2s(symbol_code)

        r = uuosapi.get_table_rows(True, 'eosio.token', symbol_code, 'stat', '', '', 10)
        logger.info(r)
        assert r['rows']

        r = uuosapi.get_table_rows(True, 'eosio.token', 'learnfortest', 'accounts', '', '', 10)
        logger.info(r)
        assert r['rows']

        r = await uuosapi_async.get_table_rows(True, 'eosio.token', symbol_code, 'stat', '', '', 10)
        logger.info(r)
        assert r['rows']

        r = await uuosapi_async.get_table_rows(True, 'eosio.token', 'learnfortest', 'accounts', '', '', 10)
        logger.info(r)
        assert r['rows']

    @pytest.mark.asyncio
    async def test_get_account(self):
        a = uuosapi.get_account('learnfortest')
        assert a
        logger.info(a)

        a = await uuosapi_async.get_account('learnfortest')
        assert a
        logger.info(a)
