import os
import sys
import time
import pytest
import logging
import hashlib
from pyeoskit import eosapi, config, wallet
from pyeoskit.exceptions import ChainException, WalletException

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)

eosapi.set_node('http://127.0.0.1:8899')

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

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

    def test_sign_transaction(self):
        trx = '{"expiration":"2021-04-13T04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        chain_id = 'aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906'
        r = wallet.sign_transaction(trx, ['EOS8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr'], chain_id)
        logger.info(r)
        assert r

    def test_sign_raw_transaction(self):
        raw = '5277866015ca01ba7664000000000100a6823403ea3055000000572d3ccdcd0190b1ca97ae798d8a00000000a8ed32322c90b1ca97ae798d8a901544b44e056976010000000000000004454f53000000000b7465737420656f736a733200'
        raw = bytes.fromhex(raw)
        chain_id = 'aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906'
        r = wallet.sign_raw_transaction(raw, ['EOS8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr'], chain_id)
        logger.info(r)
        assert r

        # eosapi.unpack_transaction(raw)

    
    def test_basic(self):
        mywallet = 'mywallet2'
        if os.path.exists(f'{mywallet}.wallet'):
            os.remove(f'{mywallet}.wallet')
        psw = wallet.create(mywallet)

        key = eosapi.create_key()
        logger.info(key)

        priv_key = key['private']
        r = wallet.import_key(mywallet, priv_key)
        assert r

        r = wallet.import_key(mywallet, priv_key)
        assert not r
        logger.error(eosapi.get_last_error())

        wallet.save(mywallet)
        wallet.set_timeout(1)
        time.sleep(2)
        priv_key = eosapi.create_key()['private']
        r = wallet.import_key(mywallet, priv_key)
        assert not r
        logger.error(eosapi.get_last_error())

        r = wallet.unlock(mywallet, psw)
        assert r

        priv_key = eosapi.create_key()['private']
        r = wallet.import_key(mywallet, priv_key)
        assert r

        with pytest.raises(WalletException):
            psw = wallet.create('a/mywallet2')

        wallets = wallet.list_wallets()
        logger.info(wallets)
        assert wallets

        keys = wallet.list_keys(mywallet, psw)
        assert keys
        logger.info(keys)

        pub_keys = wallet.get_public_keys()
        assert pub_keys
        logger.info(pub_keys)

        wallet.lock_all()
        wallets = wallet.list_wallets()
        logger.info(wallets)
        assert wallets == ['mywallet', 'mywallet2']

    def test_sign_digest(self):
        pub = eosapi.get_public_key('5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')
        digest = hashlib.sha256(b'hello,world').digest()
        signature1 = wallet.sign_digest(digest, pub)
        logger.info(signature1)

        digest = hashlib.sha256(b'hello,world').hexdigest()
        signature2 = wallet.sign_digest(digest, pub)
        logger.info(signature2)
        assert signature1 == signature2

    def test_import_key(self):
        wallet.unlock('mywallet', psw)
        priv_key = '5J4LuMP6A7R4QiEHFJX1FJQDy9RqUjMpkpdoTLTuPFgTyxBNsUp'
        pub_key = eosapi.get_public_key(priv_key)
        wallet.import_key('mywallet', priv_key)
        keys = wallet.list_keys('mywallet', psw)
        logger.info(keys)
        assert pub_key in keys
        wallet.remove_key('mywallet', psw, pub_key)
        keys = wallet.list_keys('mywallet', psw)
        assert not pub_key in keys

        wallets = wallet.list_wallets()
        assert 'mywallet *' in wallets
