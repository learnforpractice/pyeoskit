import os
import sys
import time
import json
import pytest
import logging
import hashlib
from uuoskit import uuosapi, config, wallet
from uuoskit.chainapi import ChainApiAsync
from uuoskit.exceptions import ChainException, WalletException

from uuoskit.testnet import Testnet
Testnet.__test__ = False

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)
test_dir = os.path.dirname(__file__)

# config.main_token = 'UUOS'
# config.main_token_contract = 'uuos.token'
# config.system_contract = 'uuos'

# uuosapi.set_node('http://127.0.0.1:8899')

# config.setup_uuos_network()

uuosapi_async = None

class TestUUOSApi(object):

    @classmethod
    def setup_class(cls):
        uuosapi.set_node('http://127.0.0.1:9000')
        uuosapi_async = ChainApiAsync('http://127.0.0.1:9000')

        cls.testnet = Testnet(single_node=True, show_log=False)
        cls.testnet.run()
        cls.info = uuosapi.get_info()
        # logger.info(cls.info)
        cls.chain_id = cls.info['chain_id']
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

    def test_gen_transaction(self):
        args = {
            'from': 'alice',
            'to': 'bob',
            'quantity': '1.0000 UUOS',
            'memo': 'hello,world'
        }
        a = ['eosio.token', 'transfer', args, {'alice': 'active'}]
        r = uuosapi.generate_transaction([a], 60, self.info['last_irreversible_block_id'])
        logger.info(r)
        assert r

        r = uuosapi_async.generate_transaction([a], 60, self.info['last_irreversible_block_id'])
        logger.info(r)
        assert r


        args = {
            'from': 'alice',
            'to': 'bob',
            'quantity': '1.0000 UUOS',
            'typo_memo': 'hello,world'
        }
        a = ['eosio.token', 'transfer', args, {'alice': 'active'}]

        with pytest.raises(Exception):
            r = uuosapi.generate_transaction([a], 60, self.info['last_irreversible_block_id'])

        with pytest.raises(Exception):
            r = uuosapi_async.generate_transaction([a], 60, self.info['last_irreversible_block_id'])

    @pytest.mark.asyncio
    async def test_sign_transaction(self):
        trx = '{"expiration":"2021-04-13T04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        priv_key = '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p'
        r = uuosapi.sign_transaction(trx, priv_key, self.info['chain_id'])
        logger.info(r)
        r = uuosapi_async.sign_transaction(trx, priv_key, self.info['chain_id'])

        trx = '{"expiration":"2021-04-13t04:05:10","ref_block_num":6467,"ref_block_prefix":2631147246,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"testaccount","permission":"active"}],"data":"00f2d4142193b1ca0000000000ea3055e80300000000000004454f53000000000568656c6c6f"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}'
        priv_key = '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p'
        with pytest.raises(ChainException):
            r = uuosapi.sign_transaction(trx, priv_key, self.info['chain_id'])
            logger.info(r)

        with pytest.raises(ChainException):
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
        assert pub == uuosapi.get_public_key_prefix() + '8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr'

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

        r = uuosapi.get_table_rows(True, 'eosio.token', 'helloworld11', 'accounts', '', '', 10)
        logger.info(r)
        assert r['rows']

        r = await uuosapi_async.get_table_rows(True, 'eosio.token', symbol_code, 'stat', '', '', 10)
        logger.info(r)
        assert r['rows']

        r = await uuosapi_async.get_table_rows(True, 'eosio.token', 'helloworld11', 'accounts', '', '', 10)
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

        logger.info('++++++++%s', uuosapi.s2n('notexists.a'))

        a = uuosapi.get_account('notexists')
        assert not a

        a = await uuosapi_async.get_account('notexists')
        assert not a


        with pytest.raises(ChainException):
            a = await uuosapi_async.get_account('notexists...')
            assert not a
            logger.info(a)

    def test_chain_exception(self):
        try:
            raise ChainException('oops!')
        except ChainException as e:
            assert not e.json

        try:
            raise ChainException('{"a":1}')
        except ChainException as e:
            assert e.json

        try:
            raise ChainException({"a":1})
        except ChainException as e:
            assert e.json

    def test_deploy_python_code_sync(self):
        uuosapi.set_node('http://127.0.0.1:9000')
        code = '''
import chain
def apply(a, b, c):
    data = chain.read_action_data()
    print(data)
        '''

        account = 'helloworld11'
        config.python_contract = account
        code = uuosapi.mp_compile(account, code)

        uuosapi.deploy_python_contract(account, code, b'')

        r = uuosapi.push_action(account, 'sayhello', b'hellooo,world', {account:'active'})
        console = r['processed']['action_traces'][0]['console']
        logger.info(console)
        assert console == "b'hellooo,world'\r\n"

        r = uuosapi.push_action(account, 'sayhello', b'goodbye,world', {account:'active'})
        console = r['processed']['action_traces'][0]['console']
        logger.info(console)
        assert console == "b'goodbye,world'\r\n"

    @pytest.mark.asyncio
    async def test_deploy_python_code_async(self):
        uuosapi_async = ChainApiAsync('http://127.0.0.1:9000')

        code = '''
import chain
def apply(a, b, c):
    data = chain.read_action_data()
    print(data)
    return
        '''

        account = 'helloworld11'
        code = uuosapi_async.mp_compile(account, code)

        async def run_code(code):
            await uuosapi_async.deploy_python_contract(account, code, b'')

            r = await uuosapi_async.push_action(account, 'sayhello', b'hellooo,world', {account:'active'})
            console = r['processed']['action_traces'][0]['console']
            assert console == "b'hellooo,world'\r\n"

            r = await uuosapi_async.push_action(account, 'sayhello', b'goodbye,world', {account:'active'})
            console = r['processed']['action_traces'][0]['console']
            assert console == "b'goodbye,world'\r\n"

        await run_code(code)

    @pytest.mark.asyncio
    async def test_pack_unpack_args(self):
        from uuoskit import ABI
        args = {
            'from': 'test1',
            'to': 'test2',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        r = ABI.pack_action_args('eosio.token', 'transfer', json.dumps(args))
        logger.info(r)

        r = uuosapi.pack_args('eosio.token', 'transfer', args)
        assert r
        logger.info(r)

        r = uuosapi.pack_args('eosio.token', 'transfer', json.dumps(args))
        assert r

        r = uuosapi.unpack_args('eosio.token', 'transfer', r)
        logger.info(r)
        return

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', {'a':1})

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', json.dumps({'a':1}))

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', b'hello')

        with pytest.raises(Exception):
            r = uuosapi.unpack_args('eosio.token', 'transfer', 'aabb')

    def test_get_required_keys(self):
        args = {
            'from': 'helloworld11',
            'to': 'helloworld12',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        act = ['eosio.token', 'transfer', args, {'helloworld11': 'active'}]
        chain_info = uuosapi.get_info()
        reference_block_id = chain_info['head_block_id']
        trx = uuosapi.generate_transaction([act], 60, reference_block_id)
        keys = uuosapi.get_required_keys(trx, wallet.get_public_keys())
        assert keys

        chain_id = chain_info['chain_id']
        trx = wallet.sign_transaction(trx, keys, chain_id, json=True)
        assert trx['signatures']
        # logger.info(trx)

    def test_push_action(self):
        r = uuosapi.push_action('hello', 'sayhello', b'hello')
        print(r)

    def test_push_actions(self):
        args = {
            'from': 'helloworld11',
            'to': 'helloworld12',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        a1 = ['eosio.token', 'transfer', args, {'helloworld11': 'active'}]

        args = {
            'from': 'helloworld12',
            'to': 'helloworld11',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        a2 = ['eosio.token', 'transfer', args, {'helloworld12': 'active'}]
        balance1 = uuosapi.get_balance('helloworld11')
        r = uuosapi.push_actions([a1, a2])
        balance2 = uuosapi.get_balance('helloworld11')
        logger.info('+++++%s, %s\n', balance1, balance2)

        try:
            uuosapi.push_action('token', 'transfer', args, {'helloworld11': 'active'})
        except Exception as e:
            assert e.args[0] == '[error] in main.transaction_add_action_[/Users/newworld/dev/uuoskit/src/uuoskit/lib.go:150] abi struct not found for token::transfer'

        #test for comporessed transaction
        uuosapi.push_action('eosio.token', 'transfer', args, {'helloworld12': 'active'}, compress=True)

    def test_crypto(self):
        key_pair = uuosapi.create_key()
        logger.info(key_pair)

    def gen_tx(self):
        args = {
            'from': 'helloworld11',
            'to': 'eosio',
            'quantity': '0.0100 EOS',
            'memo': 'hello'
        }
        action = ['eosio.token', 'transfer', args, {'helloworld11': 'active'}]
        chain_info = uuosapi.get_info()
        chain_id = chain_info['chain_id']
        reference_block_id = chain_info['head_block_id']
        tx = uuosapi.generate_transaction([action], 60, reference_block_id, chain_id)
        return tx

    def test_gen_tx(self):
        tx = self.gen_tx()
        logger.info(tx)
        assert tx

    def test_sign_tx(self):
        from uuoskit.transaction import Transaction
        tx = self.gen_tx()
        logger.info(tx)
        t = Transaction.from_json(tx)
        pub_key = 'EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV'
        sign = t.sign(pub_key)
        logger.info(sign)
        logger.info(t.pack())

    def test_unpack_tx(self):
        from uuoskit.transaction import Transaction
        tx = self.gen_tx()
        logger.info(tx)
        t = Transaction.from_json(tx)
        pub_key = 'EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV'
        sign = t.sign(pub_key)
        logger.info(sign)
        tx = t.pack()
        logger.info(tx)
        tx = Transaction.unpack(tx['packed_trx'])
        logger.info(tx)

    def test_wallet_sign(self):
        from uuoskit.transaction import Transaction
        from uuoskit import wallet
        tx = self.gen_tx()
        pubs = ['EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV']
        tx = wallet.sign_transaction(tx, pubs, self.chain_id)
        logger.info(tx)

    def test_get_public_key(self):
        priv = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
        pub_eos = uuosapi.get_public_key(priv)
        pub_common = uuosapi.get_public_key(priv, False)
        assert pub_eos == 'EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV'
        assert pub_common == 'PUB_K1_6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5BoDq63'
