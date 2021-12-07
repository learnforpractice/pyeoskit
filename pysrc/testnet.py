import os
import sys
import time
import json
import copy
import shlex
import shutil
import random
import signal
import hashlib
import platform
import subprocess

from pyeoskit import config
from pyeoskit import wallet
from pyeoskit import utils
from pyeoskit import eosapi
from pyeoskit import log

logger = log.get_logger(__name__)

class Testnet(object):
    def __init__(self, host='127.0.0.1', single_node=True, show_log=False, log_config='', extra=''):
        self.host=host
        self.single_node = single_node
        self.show_log = show_log
        self.log_config = log_config
        self.extra = extra
        self.tmp_dir='.eos-testnet'
        self.nodes = []

        self.test_accounts = (
            'hello',
            'helloworld11',
            'helloworld12',
            'helloworld13',
            'helloworld14',
            'helloworld15',
            'helloworld33',
        )

        self.producer_accounts = (
            'genesisbp111',
            'genesisbp112',
            'genesisbp113',
            'genesisbp114',
            'genesisbp115'
        )

        self.cur_dir = os.path.dirname(__file__)

        if not os.path.exists(self.tmp_dir):
            os.mkdir(self.tmp_dir)

        wallet.set_dir(self.tmp_dir)
        test_wallet = os.path.join(self.tmp_dir, 'test.wallet')
        if os.path.exists(test_wallet):
            os.remove(test_wallet)
        psw = wallet.create('test')
        print(psw)
        priv_keys = [
            '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3',#EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV
            '5JEcwbckBCdmji5j8ZoMHLEUS8TqQiqBG1DRx1X9DN124GUok9s',#EOS61MgZLN7Frbc2J7giU7JdYjy2TqnfWFjZuLXvpHJoKzWAj7Nst
            '5JbDP55GXN7MLcNYKCnJtfKi9aD2HvHAdY7g8m67zFTAFkY1uBB',#EOS5JuNfuZPATy8oPz9KMZV2asKf9m8fb2bSzftvhW55FKQFakzFL
            '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p',#EOS8Znrtgwt8TfpmbVpTKvA2oB8Nqey625CLN8bCN3TEbgx86Dsvr
            '5KH8vwQkP4QoTwgBtCV5ZYhKmv8mx56WeNrw9AZuhNRXTrPzgYc',#EOS7ent7keWbVgvptfYaMYeF2cenMBiwYKcwEuc11uCbStsFKsrmV
            '5KT26sGXAywAeUSrQjaRiX9uk9uDGNqC1CSojKByLMp7KRp8Ncw',#EOS8Ep2idd8FkvapNfgUwFCjHBG4EVNAjfUsRRqeghvq9E91tkDaj

            '5JRYimgLBrRLCBAcjHUWCYRv3asNedTYYzVgmiU4q2ZVxMBiJXL',#EOS6AjF6hvF7GSuSd4sCgfPKq5uWaXvGM2aQtEUCwmEHygQaqxBSV
            '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo',#EOS7sPDxfw5yx5SZgQcVb57zS1XeSWLNpQKhaGjjy2qe61BrAQ49o
            '5JHRxntHapUryUetZgWdd3cg6BrpZLMJdqhhXnMaZiiT4qdJPhv',#EOS89jesRgvvnFVuNtLg4rkFXcBg2Qq26wjzppssdHj2a8PSoWMhx
            '5Jbh1Dn57DKPUHQ6F6eExX55S2nSFNxZhpZUxNYFjJ1arKGK9Q3',#EOS73ECcVHVWvuxJVm5ATnqBTCFMtA6WUsdDovdWH5NFHaXNq1hw1
            '5JJYrXzjt47UjHyo3ud5rVnNEPTCqWvf73yWHtVHtB1gsxtComG',#EOS8h8TmXCU7Pzo5XQKqyWwXAqLpPj4DPZCv5Wx9Y4yjRrB6R64ok
            '5J9PozRVudGYf2D4b8JzvGxPBswYbtJioiuvYaiXWDYaihNFGKP',#EOS65jj8NPh2EzLwje3YRy4utVAATthteZyhQabpQubxHNJ44mem9
            '5K9AZWR2wEwtZii52vHigrxcSwCzLhhJbNpdXpVFKHP5fgFG5Tx',#EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1
        ]

        for priv_key in priv_keys:
            wallet.import_key('test', priv_key, False)

    def start_nodes(self, wait=False):
        self.nodes = []
        if self.log_config:
            configs = f'--data-dir ./{self.tmp_dir}/dd --config-dir ./{self.tmp_dir}/cd -l {self.log_config} {self.extra}'
        else:
            configs = f'--data-dir ./{self.tmp_dir}/dd --config-dir ./{self.tmp_dir}/cd {self.extra}'
        args = f'nodeos --verbose-http-errors  --http-max-response-time-ms 100 --p2p-listen-endpoint {self.host}:9100 {configs} -p eosio --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::producer_api_plugin --plugin eosio::history_api_plugin -e --resource-monitor-space-threshold 99 --http-server-address {self.host}:9000 --contracts-console --access-control-allow-origin="*"' # --backing-store rocksdb'
        logger.info(args)
        args = shlex.split(args)
        # if self.show_log:
        #     f = sys.stdout
        # else:
        #     f = open('log.txt', 'a')
        # f = sys.stdout
        if self.show_log:
            p = subprocess.Popen(args)
        else:
            f = open('log.txt', 'a')
            p = subprocess.Popen(args, stdout=f, stderr=f)

        self.nodes.append(p)

        eosapi.set_node(f'http://{self.host}:9000')
        while True:
            time.sleep(0.5)
            try:
                info = eosapi.get_info()
                # logger.info(info)
                break
            except Exception as e:
                logger.info(e)
        if self.single_node:
            return
        self.producer_keys = [
            {
                "public": "EOS7haGjz9YTepY31iZNfP13dzVXvsU5D2VHeJNZZjhxwMVyCrCFL",
                "private": "5Jyj1Scuwu47yTBbQoYojrvw5xbMoUUGHoV4DzEFsKDjAVrvEhB"
            },
            {
                "public": "EOS5g4kCpZDYHLrbmkGh3cvnbt9KZs9kK3j95LKjRTT8pYR4dkKE3",
                "private": "5JrfTriycVJHxnAw2gBEuLXjU2HAqZMwyzw18dNMVfXhkN4vQ4D"
            },
            {
                "public": "EOS8GGk6a2RU8JCGLEQ4LVhFtMH9PLvcPYrwxviCKr842amwvBWdD",
                "private": "5Hxz7hbHK9nJg1kV4W2ScMGFCX6Ks4B8MQ5kt1AdmRNRzxymP5X"
            },
            {
                "public": "EOS56KkFcZ5rtkSQmM9ZbBRV8fmGzdC3GTGrZi7KuQEhJmHSpiMHg",
                "private": "5KLBi386dgBDHunmoqrEbj6MaydYwEXgx1Awqk4a78rZ7b9S7iN"
            },
            {
                "public": "EOS5cv6rQ1okdvqktfX8R2SKeyMFZAnFHCc1jAXerbpzUtsu4A9F9",
                "private": "5JaoiGqLBQ9ASsB946anLJa8hPAm7yaLn4gY1adU7vw9LX8UTtJ"
            }
        ]

        start_port = 9001
        http_ports = [port for port in range(start_port, start_port+5)]
        p2p_ports = [9100,]
        for http_port in http_ports:
            p2p_listen_port = http_port+100
            index = http_port-start_port
            http_ports_copy = copy.copy(http_ports)
            del http_ports_copy[index]

            bp = f'genesisbp11{index+1}'
            logfile = f'{self.tmp_dir}/{bp}.log'
            pub = self.producer_keys[index]['public']
            priv = self.producer_keys[index]['private']

            signature_provider = f'--signature-provider={pub}=KEY:{priv}'
            http_server_address = f'--http-server-address {self.host}:{http_port}'
            p2p_listen_endpoint = f'--p2p-listen-endpoint {self.host}:{p2p_listen_port}'

            p2p_peer_address = ''
            for port in p2p_ports:
                p2p_peer_address += f'--p2p-peer-address {self.host}:{port} '

            dirs = f'--data-dir {self.tmp_dir}/dd-{bp} --config-dir {self.tmp_dir}/cd-{bp} -p {bp}'
            if http_port == 9001:
                args = f'nodeos -e {dirs} {signature_provider} {http_server_address} {p2p_listen_endpoint} {p2p_peer_address} --verbose-http-errors  --http-max-response-time-ms 100 --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::producer_api_plugin --plugin eosio::history_api_plugin --resource-monitor-space-threshold 99 --contracts-console --access-control-allow-origin="*"' # --backing-store rocksdb'
            else:
                args = f'nodeos {dirs} {signature_provider} {http_server_address} {p2p_listen_endpoint} {p2p_peer_address} --verbose-http-errors  --http-max-response-time-ms 100 --plugin eosio::producer_plugin --plugin eosio::chain_api_plugin --plugin eosio::producer_api_plugin --plugin eosio::history_api_plugin --resource-monitor-space-threshold 99 --contracts-console --access-control-allow-origin="*"' # --backing-store rocksdb'

            logger.info(args)
            args = shlex.split(args)

            f = open(logfile, 'a')
            p = subprocess.Popen(args, stdout=f, stderr=f)
            self.nodes.append(p)

            p2p_ports.append(p2p_listen_port)

        if wait:
            p.wait()
        return p

    def start(self):
        return self.run()

    def run(self):
        p = self.start_nodes()
        # p.wait()
        # return
        try:
            self.init_testnet()
        except Exception as e:
            logger.exception(e)
        # p.wait()
        # print('done!')

    def stop(self):
        for p in self.nodes:
            p.send_signal(signal.SIGINT)
        self.wait()
        self.nodes = []
        print('done!')

    def cleanup(self):
        self.stop()
        import shutil
        if os.path.exists(self.tmp_dir):
            shutil.rmtree(self.tmp_dir)

    def wait(self):
        for p in self.nodes:
            p.wait()

    def deploy_contract(self, account_name, contract_name, contracts_path=None):
        logger.info('++++deploy_contract %s %s', account_name, contract_name)
        if not contracts_path:
            contracts_path = os.path.dirname(__file__)
            # contracts_path = '../../../build/externals/eosio.contracts'
            # contracts_path = '.'
            contracts_path = os.path.join(contracts_path, f'contracts/{contract_name}')

        code_path = os.path.join(contracts_path, f'{contract_name}.wasm')
        abi_path = os.path.join(contracts_path, f'{contract_name}.abi')

        logger.info(code_path)
        code = open(code_path, 'rb').read()
        abi = open(abi_path, 'rb').read()

        m = hashlib.sha256()
        m.update(code)
        code_hash = m.hexdigest()

        r = eosapi.get_raw_code(account_name)
        logger.info((code_hash, r['code_hash']))
        if code_hash == r['code_hash']:
            logger.info('contract already running this version of code')
            return True

        logger.info(f"++++++++++set contract: {account_name}")
        r = eosapi.deploy_contract(account_name, code, abi, vm_type=0, compress=True)
        return True

    def deploy_micropython_contract(self):
        logger.info("++++++++deploy_micropython_contract")
        code_path = os.path.join(self.cur_dir, './contracts/micropython/micropython_uuos.wasm')
        code_path = os.path.join(self.cur_dir, './contracts/micropython/micropython.wasm')
        abi_path = os.path.join(self.cur_dir, './contracts/micropython/micropython.abi')

        code = open(code_path, 'rb').read()
        abi = open(abi_path, 'rb').read()

        try:
            pass
            #r = eosapi.deploy_contract('hello', code, abi, vm_type=0, compress=True)
            #r = eosapi.deploy_contract('eosio.mpy', code, abi, vm_type=0, compress=True)
        except Exception as e:
            logger.exception(e)
        return
        code = '''
def apply(a, b, c):
    pass
        '''
        account = 'hello'

        code = eosapi.mp_compile(account, code)

        account = 'hello'
        args = eosapi.s2b(account) + code
        eosapi.push_action(account, 'setcode', args, {account:'active'})

        account = 'eosio.mpy'
        args = eosapi.s2b(account) + code
        eosapi.push_action(account, 'setcode', args, {account:'active'})

    def create_account(self, account, key1, key2):
        newaccount = {
            'creator': 'eosio',
            'name': '',
            'owner': 
            {
                'threshold': 1,
                'keys': [
                    {
                        'key': key1,
                        'weight': 1
                    }
                ],
                'accounts': [],
                'waits': []
            },
            'active': 
            {
                'threshold': 1,
                'keys': [
                    {
                        'key': key2,
                        'weight': 1
                    }
                ],
                'accounts': [],
                'waits': []
            }
        }
        actions = []
        # logger.info(('+++++++++create account', account))
        newaccount['name'] = account
        act = ['eosio', 'newaccount', newaccount, {'eosio':'active'}]
        actions.append(act)
        r = eosapi.push_actions(actions)

    def init_testnet(self):
        self.init_accounts()
        self.init_producer()

    def init_accounts(self):
        if eosapi.get_account('helloworld11'):
            return
        # formatter = logging.Formatter('%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s')
        # handler = logging.StreamHandler()
        # handler.setFormatter(formatter)

        # config.setup_eos_network()

        # if len(sys.argv) == 2:
        #     print(sys.argv)
        #     eosapi.set_nodes([sys.argv[1]])

        key1 = 'EOS7ent7keWbVgvptfYaMYeF2cenMBiwYKcwEuc11uCbStsFKsrmV'
        key2 = 'EOS7ent7keWbVgvptfYaMYeF2cenMBiwYKcwEuc11uCbStsFKsrmV'

        system_accounts = [
            'eosio.mpy',
            'eosio.bpay',
            'eosio.msig',
            'eosio.names',
            'eosio.ram',
            'eosio.ramfee',
            'eosio.saving',
            'eosio.stake',
            'eosio.token',
            'eosio.vpay',
            'eosio.rex',
            'eosio.reserv'
        ]
        for a in system_accounts:
            self.create_account(a, key1, key2)

        pub_keys = (
            'EOS6AjF6hvF7GSuSd4sCgfPKq5uWaXvGM2aQtEUCwmEHygQaqxBSV',
            'EOS7sPDxfw5yx5SZgQcVb57zS1XeSWLNpQKhaGjjy2qe61BrAQ49o',
            'EOS89jesRgvvnFVuNtLg4rkFXcBg2Qq26wjzppssdHj2a8PSoWMhx',
            'EOS73ECcVHVWvuxJVm5ATnqBTCFMtA6WUsdDovdWH5NFHaXNq1hw1',
            'EOS8h8TmXCU7Pzo5XQKqyWwXAqLpPj4DPZCv5Wx9Y4yjRrB6R64ok',
            'EOS65jj8NPh2EzLwje3YRy4utVAATthteZyhQabpQubxHNJ44mem9',
            'EOS65jj8NPh2EzLwje3YRy4utVAATthteZyhQabpQubxHNJ44mem9',
            'EOS65jj8NPh2EzLwje3YRy4utVAATthteZyhQabpQubxHNJ44mem9',
        )

        producer_pub_keys = (
            'EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1',
            'EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1',
            'EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1',
            'EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1',
            'EOS5fVw435RSwW3YYWAX9qz548JFTWuFiBcHT3PGLryWaAMmxgjp1',
        )

        i = 0
        for a in self.test_accounts:
            key = pub_keys[i]
            self.create_account(a, key, key)
            i += 1

        i = 0
        for a in self.producer_accounts:
            key = producer_pub_keys[i]
            self.create_account(a, key, key)
            i += 1

        try:
            eosapi.schedule_protocol_feature_activations(['0ec7e080177b2c02b278d5088611686b49d739925a92d9bfcacd7fc6b74053bd']) #PREACTIVATE_FEATURE
            time.sleep(1.0)
            logger.info('set PREACTIVATE_FEATURE done!')
        except Exception as e:
            logger.exception(e)

        # try:
        #     eosapi.update_runtime_options(max_transaction_time=230)
        #     time.sleep(2.0)
        # except Exception as e:
        #     logger.exception(e)

        contracts_path = os.path.dirname(__file__)
        contracts_path = os.path.join(contracts_path, 'contracts')

        if not eosapi.get_raw_code_and_abi('eosio')['wasm']:
            self.deploy_contract('eosio', 'eosio.bios')
        time.sleep(1.0)
        feature_digests = [
            '1a99a59d87e06e09ec5b028a9cbb7749b4a5ad8819004365d02dc4379a8b7241', #'ONLY_LINK_TO_EXISTING_PERMISSION' 
            '2652f5f96006294109b3dd0bbde63693f55324af452b799ee137a81a905eed25', #'FORWARD_SETCODE' 
            '299dcb6af692324b899b39f16d5a530a33062804e41f09dc97e9f156b4476707', #'WTMSIG_BLOCK_SIGNATURES' 
            'ef43112c6543b88db2283a2e077278c315ae2c84719a8b25f25cc88565fbea99', #'REPLACE_DEFERRED' 
            '4a90c00d55454dc5b059055ca213579c6ea856967712a56017487886a4d4cc0f', #'NO_DUPLICATE_DEFERRED_ID' 
            '4e7bf348da00a945489b2a681749eb56f5de00b900014e137ddae39f48f69d67', #'RAM_RESTRICTIONS' 
            '4fca8bd82bbd181e714e283f83e1b45d95ca5af40fb89ad3977b653c448f78c2', #'WEBAUTHN_KEY'
            '5443fcf88330c586bc0e5f3dee10e7f63c76c00249c87fe4fbf7f38c082006b4', #'BLOCKCHAIN_PARAMETERS'
            '68dcaa34c0517d19666e6b33add67351d8c5f69e999ca1e37931bc410a297428', #'DISALLOW_EMPTY_PRODUCER_SCHEDULE'
            '825ee6288fb1373eab1b5187ec2f04f6eacb39cb3a97f356a07c91622dd61d16', #'KV_DATABASE'
            '8ba52fe7a3956c5cd3a656a3174b931d3bb2abb45578befc59f283ecd816a405', #'ONLY_BILL_FIRST_AUTHORIZER'
            'ad9e3d8f650687709fd68f4b90b41f7d825a365b02c23a636cef88ac2ac00c43', #'RESTRICT_ACTION_TO_SELF'
            'bf61537fd21c61a60e542a5d66c3f6a78da0589336868307f94a82bccea84e88', #'CONFIGURABLE_WASM_LIMITS'
            'c3a6138c5061cf291310887c0b5c71fcaffeab90d5deb50d3b9e687cead45071', #'ACTION_RETURN_VALUE'
            'e0fb64b1085cc5538970158d05a009c24e276fb94e1a0bf6a528b48fbc4ff526', #'FIX_LINKAUTH_RESTRICTION'
            'f0af56d2c5a48d60a4a5b5c903edfb7db3a736a94ed589d0b797df33ff9d3e1d', #'GET_SENDER'
        ]

        for digest in feature_digests: 
            try:
                args = {'feature_digest': digest}
                # logger.info(f'activate {digest}')
                eosapi.push_action('eosio', 'activate', args, {'eosio':'active'})
            except Exception as e:
                logger.error(e)

        self.deploy_micropython_contract()

        try:
            self.deploy_contract('eosio.token', 'eosio.token')
        except Exception as e:
            logger.exception(e)

        if not eosapi.get_balance('eosio'):
            logger.info('issue system token...')
            msg = {"issuer":"eosio","maximum_supply":f"11000000000.0000 {config.main_token}"}
            r = eosapi.push_action('eosio.token', 'create', msg, {'eosio.token':'active'})
            assert r
            r = eosapi.push_action('eosio.token','issue',{"to":"eosio","quantity":f"1000000000.0000 {config.main_token}","memo":""},{'eosio':'active'})
            assert r

        try:
            self.deploy_contract('eosio.msig', 'eosio.msig')
        except Exception as e:
            logger.exception(e)

        #wait for protocol activation
        time.sleep(1.0)
        for i in range(3):
            try:
                if self.deploy_contract('eosio', 'eosio.system'):
                    logger.info('deploy eosio.system done!')
                    break
            except Exception as e:
                pass
#                logger.info(e)
        else:
            assert False, 'deploy eosio.system failed!'

        if True:
            args = dict(version = 0,
                        core = '4,EOS',
                        # min_bp_staking_amount = 0,
                        # vote_producer_limit = 100,
                        # mini_voting_requirement = 21
            )

            # args['min_bp_staking_amount'] = 10000000000
            try:
                eosapi.push_action('eosio', 'init', args, {'eosio':'active'})
            except Exception as e:
                logger.exception(e)

        if eosapi.get_balance('helloworld11') <=0:
            r = eosapi.push_action('eosio.token', 'transfer', {"from":"eosio", "to":"helloworld11","quantity":f"10000000.0000 {config.main_token}","memo":""}, {'eosio':'active'})

        if eosapi.get_balance('helloworld12') <=0:
            r = eosapi.push_action('eosio.token', 'transfer', {"from":"eosio", "to":"helloworld12","quantity":f"10000000.0000 {config.main_token}","memo":""}, {'eosio':'active'})

        if eosapi.get_balance('helloworld13') <=0:
            r = eosapi.push_action('eosio.token', 'transfer', {"from":"eosio", "to":"helloworld13","quantity":f"10000000.0000 {config.main_token}","memo":""}, {'eosio':'active'})

        if eosapi.get_balance('helloworld14') <=0:
            r = eosapi.push_action('eosio.token', 'transfer', {"from":"eosio", "to":"helloworld14","quantity":f"10000000.0000 {config.main_token}","memo":""}, {'eosio':'active'})


        if eosapi.get_balance('hello') <=0:
            args = {"from":"eosio", "to":"hello","quantity":f"600000000.0000 {config.main_token}","memo":""}
            r = eosapi.push_action('eosio.token', 'transfer', args, {'eosio':'active'})

        for account in  self.test_accounts:
            eosapi.transfer('eosio', account, 10000.0)
            utils.buyrambytes('eosio', account, 5*1024*1024)
            utils.dbw(account, account, 1.0, 1000)

        utils.dbw('hello', 'hello', 1.0, 5*1e8)

        if 0:
            try:
                args = {'vmtype': 1, 'vmversion':0} #activate vm python
                eosapi.push_action('eosio', 'activatevm', args, {'eosio':'active'})
            except Exception as e:
                logger.info(e)

            try:
                args = {'vmtype': 2, 'vmversion':0} #activate vm python
                eosapi.push_action('eosio', 'activatevm', args, {'eosio':'active'})
            except Exception as e:
                logger.info(e)

        balance = eosapi.get_balance('hello')
        logger.info(f'++++balance: {balance}')
        while False:
            n = random.randint(0,10000000)
            elapsed = 0
            for i in range(n, n+10):
                try:
                    r = eosapi.transfer('hello', 'eosio', 0.0001, str(i))
                    logger.info(r['processed']['elapsed'])
                    elapsed += int(r['processed']['elapsed'])
                except Exception as e:
                    logger.exception(e)

            logger.info(f'AVG: {elapsed/10}')
            logger.info(eosapi.get_balance('hello'))
            time.sleep(2.0)

        for account in self.test_accounts:
            # print('buy ram', account)
            utils.buyrambytes('hello', account, 10*1024*1024)
            # print('buy cpu', account)
            utils.dbw('hello', account, 1.0, 1.0)

        if 0:
            args = {
                'owner': 'helloworld11',
                'amount': '1.0000 EOS'
            }
            eosapi.push_action('eosio', 'deposit', args, {'helloworld11': 'active'})

    def init_producer(self):
        if self.single_node:
            return

        a = eosapi.get_producers(True, '0', 10)
        logger.info(a)
        if len(a['rows']) > 1:
            return

        logger.info('++++++register producers...')


        index = 0
        for p in self.producer_accounts:
            args = {
                "producer": p,
                "producer_key": self.producer_keys[index]['public'],
                "url": '',
                "location": 0
            }
            eosapi.push_action('eosio', 'regproducer', args, {p:'active'})
            index += 1

        logger.info('+++++++vote producers...')
        args = {
            "voter": '',
            "proxy": '',
            "producers": self.producer_accounts
        }
        for account in self.test_accounts:
            args['voter'] = account
            eosapi.push_action('eosio', 'voteproducer', args, {account:'active'})

