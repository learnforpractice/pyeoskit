import os
import sys
import time
import json
import pytest
import logging
import hashlib

from pyeoskit import ABI

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)


from pyeoskit.chainapi import ChainApi

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

        from pyeoskit import _pyeoskit
        _pyeoskit.init()

        _pyeoskit.wallet_import("test", "5JRYimgLBrRLCBAcjHUWCYRv3asNedTYYzVgmiU4q2ZVxMBiJXL")

        idx = _pyeoskit.transaction_new(int(time.time()) + 60, ref_block, chain_id)
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
        _pyeoskit.transaction_add_action(idx, 'eosio.token', 'transfer', transfer, perms)
        r = _pyeoskit.transaction_sign(idx, pub)
        logger.info(r)
        r = _pyeoskit.transaction_pack(idx, 0)
        logger.info(r)
        r = json.loads(r)
        logger.info(r)
        r = json.loads(r['data'])
        logger.info(r)

    def test_debug(self):
        from pyeoskit import _pyeoskit
        _pyeoskit.set_debug_flag(False)
        assert _pyeoskit.get_debug_flag() == False

    def test_bad_abi(self):
        from pyeoskit import _pyeoskit
        #_pyeoskit.set_debug_flag(False)
        with pytest.raises(Exception) as e_info:
            abi = '{\n    "version": "eosio::abi/1.1",\n '
            r = ABI.set_contract_abi("test", abi)
            logger.info(r)

    def test_abi(self):
        from pyeoskit import _pyeoskit
        _pyeoskit.init()

        abi = '{\n    "version": "eosio::abi/1.1",\n    "structs": [],\n    "types": [],\n    "actions": [],\n    "tables": [],\n    "ricardian_clauses": [],\n    "variants": [],\n    "abi_extensions": [],\n    "error_messages": []\n}'
        r = ABI.set_contract_abi("test", abi)

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

        abi = '''
{
    "version": "eosio::abi/1.0",
    "types": [
    ],
    "structs": [
            {
            "name": "sayhello",
            "base": "",
            "fields": [
                {
                    "name": "name",
                    "type": "int32[]"
                }
            ]
        }
    ],
    "actions": [{
        "name": "sayhello",
        "type": "sayhello",
        "ricardian_contract": ""
    }],
    "tables": [],
    "ricardian_clauses": [],
    "error_messages": [],
    "abi_extensions": []
}
'''
        r = ABI.set_contract_abi("test", abi)
        args = {'name': [123, 456]}
        r = ABI.pack_abi_type('test', 'sayhello', json.dumps(args))
        logger.info(r)

        r = ABI.unpack_abi_type('test', 'sayhello', r)
        logger.info(r)

        packed_abi = ABI.pack_abi(abi)
        logger.info(packed_abi)

        unpacked_abi = ABI.unpack_abi(packed_abi)
        logger.info(unpacked_abi)

    def test_wallet(self):
        from pyeoskit import wallet, eosapi
        h = hashlib.sha256(b'123').hexdigest()

        priv = '5JRYimgLBrRLCBAcjHUWCYRv3asNedTYYzVgmiU4q2ZVxMBiJXL'
        wallet.import_key('test', priv)
        pub = eosapi.get_public_key(priv)
        sign = wallet.sign_digest(h, pub)

        sign2 = eosapi.sign_digest(h, priv)
        assert sign == sign2

        pub2 = eosapi.recover_key(h, sign)
        assert sign == sign2

    def test_optional(self):
        abi = '''
    {
        "version": "eosio::abi/1.1",
        "structs": [
            {
                "name": "testext",
                "base": "",
                "fields": [
                    {
                        "name": "a",
                        "type": "string"
                    },
                    {
                        "name": "b",
                        "type": "checksum256?"
                    },
                    {
                        "name": "c",
                        "type": "checksum256$"
                    }
                ]
            }
        ],
        "types": [],
        "actions": [
            {
                "name": "testext",
                "type": "testext",
                "ricardian_contract": ""
            }
        ],
        "tables": [],
        "ricardian_clauses": [],
        "variants": [],
        "abi_extensions": [],
        "error_messages": []
    }        
'''
        r = ABI.set_contract_abi("test", abi)
        args = {
            "a": "hello", 
            "b": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            "c": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        }
        r = ABI.pack_abi_type('test', 'testext', json.dumps(args))
        assert r == '0568656c6c6f01aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        r = ABI.unpack_abi_type('test', 'testext', r)
        logger.info(r)
        assert r == '{"a":"hello","b":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa","c":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}'

        args = {"a": "hello", "b": None, "c": 'aa'*32}
        r = ABI.pack_abi_type('test', 'testext', json.dumps(args))
        logger.info(r)
        assert r == '0568656c6c6f00aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        r = ABI.unpack_abi_type('test', 'testext', r)
        logger.info(r)
        assert r == '{"a":"hello","b":null,"c":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}'

        args = {"a": "hello", "b": None}
        r = ABI.pack_abi_type('test', 'testext', json.dumps(args))
        logger.info(r)
        assert r == '0568656c6c6f00'
        r = ABI.unpack_abi_type('test', 'testext', r)
        logger.info(r)
        assert r == '{"a":"hello","b":null}'
