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

    def test_1sign_transaction(self):
        eosapi.set_node('http://127.0.0.1:9000')
        args = {
            'from': 'helloworld11',
            'to': 'b',
            'quantity': '1.0000 EOS',
            'memo': 'hello'
        }
        eosapi.push_action('eosio.token', 'transfer', args, {'helloworld11': 'active'}, indices=[0])

    def test_2ledger(self):
        from pyeoskit import ledger
        for i in range(0, 1):
            print('+++++++++++:', i)
            pub = ledger.get_public_key(i)
            print(pub)

    def test_3ledger(self):
        tx = {"expiration":"2021-12-11T09:34:49",
            "ref_block_num":32348,
            "ref_block_prefix":1365753157,
            "max_net_usage_words":0,
            "max_cpu_usage_ms":0,
            "delay_sec":0,
            "context_free_actions":[],
            "actions":[
                {
                    "account":"eosio.token",
                    "name":"transfer",
                    "authorization":[
                        {"actor":"helloworld11","permission":"active"}
                    ],
                    "data":"70d55697ae798d8a0000000000000038102700000000000004454f53000000000568656c6c6f"}
                ],"transaction_extensions":[]
            }
        
        from pyeoskit.transaction import Transaction
        t = Transaction.from_json(tx)
        logger.info("t.pack(): %s", t.pack())
        chain_id = 'aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906'
        digest = t.digest(chain_id)
        print(digest)

        from pyeoskit import ledger
        ledger.sign(tx, [0], chain_id)

