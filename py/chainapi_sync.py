from . import config
from . import wallet
from . import _uuosapi
from . import defaultabi
from . import wasmcompiler
from . import log

from .chaincache import ChainCache
from .client import Client
from .chainnative import ChainNative
from .exceptions import ChainException

logger = log.get_logger(__name__)


class ChainApi(Client, ChainNative):
    def __init__(self, node_url = 'http://127.0.0.1:8888', network='EOS'):
        super().__init__(_async=False)

        config.get_abi = self.get_abi
        self.db = ChainCache(self, network)
        self.set_node(node_url)

    def enable_decode(self, json_format):
        super().json_decode = json_format

    def init(self):
        self.get_code(config.system_contract)
        self.get_code(config.main_token_contract)

    def get_chain_id(self):
        return self.get_info()['chain_id']

    def push_transaction(self, trx, compress=0):
        trx = _uuosapi.pack_transaction(trx, compress)
        return super().push_transaction(trx)

    def push_action(self, contract, action, args, permissions=None, compress=0):
        if not permissions:
            permissions = {contract:'active'}
        act = [contract, action, args, permissions]
        chain_info = self.get_info()
        reference_block_id = chain_info['head_block_id']
        chain_id = chain_info['chain_id']

        trx = _uuosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        if isinstance(permissions, dict):
            for account in permissions:
                public_keys = self.get_available_public_keys(account, permissions[account])
                keys.extend(public_keys)
        elif isinstance(permissions, list):
            for perm in permissions:
                assert len(perm) == 1
                for account in perm:
                    public_keys = self.get_available_public_keys(account, perm[account])
                    keys.extend(public_keys)
        else:
            assert 0, 'bad permission type'
#        print(keys)
        trx = wallet.sign_transaction(trx, keys, chain_id)
        trx = _uuosapi.pack_transaction(trx, compress)
        return super().push_transaction(trx)

    def push_actions(self, actions, compress=0):
        chain_info = self.get_info()
        reference_block_id = chain_info['last_irreversible_block_id']
        chain_id = chain_info['chain_id']
        trx = _uuosapi.gen_transaction(actions, 60, reference_block_id)
        keys = []
        fetched_keys = {}
        for a in actions:
            permissions = a[3]
            for account in permissions:
                key =  account + permissions[account]
                if not key in fetched_keys:
                    public_keys = self.get_available_public_keys(account, permissions[account])
                    keys.extend(public_keys)
                    fetched_keys[key] = True
        trx = wallet.sign_transaction(trx, keys, chain_id)
        trx = _uuosapi.pack_transaction(trx, compress)

        return super().push_transaction(trx)

    def push_transactions(self, aaa, expiration=60):
        chain_info = self.get_info()
        reference_block_id = chain_info['last_irreversible_block_id']
        chain_id = chain_info['chain_id']

        trxs = []
        for aa in aaa:
            trx = _uuosapi.gen_transaction(aa, expiration, reference_block_id)
            keys = []
            for a in aa:
                permissions = a[3]
                for account in permissions:
                    public_keys = self.get_available_public_keys(account, permissions[account])
                    keys.extend(public_keys)
            trx = wallet.sign_transaction(trx, keys, chain_id)
            trx = _uuosapi.pack_transaction(trx, 0)
            trxs.append(trx)
        return super().push_transactions(trxs)

    def strip_prefix(self, pub_key):
        if pub_key.startswith('EOS'):
            return pub_key[3:]
        elif pub_key.startswith('UUOS'):
            return pub_key[4:]
        else:
            return pub_key

    def get_available_public_keys(self, account, permission):
        wallet_public_keys = wallet.get_public_keys()
        for i in range(len(wallet_public_keys)):
            pub_key = wallet_public_keys[i]
            wallet_public_keys[i] = self.strip_prefix(pub_key)

        threshold, account_public_keys = self.get_keys(account, permission)
        keys = []
        for key in account_public_keys:
            _key = key['key']
            if self.strip_prefix(_key) in wallet_public_keys:
                keys.append(_key)
                threshold -= key['weight']
                if threshold <= 0:
                    break
        return keys

    def get_account(self, account):
        return super().get_account(account)

    def create_account(self, creator, account, owner_key, active_key, ram_bytes=0, stake_net=0.0, stake_cpu=0.0, sign=True):
        actions = []
        args = {
            'creator': creator,
            'name': account,
            'owner': {
                'threshold': 1,
                'keys': [{'key': owner_key, 'weight': 1}],
                'accounts': [],
                'waits': []
            },
            'active': {
                'threshold': 1,
                'keys': [{'key': active_key, 'weight': 1}],
                'accounts': [],
                'waits': []
            }
        }
        args = self.pack_args(config.system_contract, 'newaccount', args)
        act = [config.system_contract, 'newaccount', args, {creator:'active'}]
        actions.append(act)

        if ram_bytes:
            args = {'payer':creator, 'receiver':account, 'bytes':ram_bytes}
            args = self.pack_args(config.system_contract, 'buyrambytes', args)
            act = [config.system_contract, 'buyrambytes', args, {creator:'active'}]
            actions.append(act)

        if stake_net or stake_cpu:
            args = {
                'from': creator,
                'receiver': account,
                'stake_net_quantity': '%0.4f %s'%(stake_net, config.main_token),
                'stake_cpu_quantity': '%0.4f %s'%(stake_cpu, config.main_token),
                'transfer': 1
            }
            args = self.pack_args(config.system_contract, 'delegatebw', args)
            act = [config.system_contract, 'delegatebw', args, {creator:'active'}]
            actions.append(act)
        return self.push_actions(actions)

    def get_balance(self, account, token_account=None, token_name=None):
        if not token_account:
            token_account = config.main_token_contract
        if not token_name:
            token_name = config.main_token            
        try:
            ret = super().get_currency_balance(token_account, account, token_name)
            if ret:
                return float(ret[0].split(' ')[0])
        except Exception as e:
            return 0.0
        return 0.0

    def transfer(self, _from, to, amount, memo='', token_account=None, token_name=None, permission='active'):
        if not token_account:
            token_account = config.main_token_contract
        if not token_name:
            token_name = config.main_token
        args = {"from":_from, "to": to, "quantity":'%.4f %s'%(amount, token_name), "memo":memo}
        return self.push_action(token_account, 'transfer', args, {_from:permission})

    def get_code(self, account):
        code = self.db.get_code(account)
        if code:
            return code

        try:
            code = super().get_code(account)
            code = base64.b64decode(code['wasm'])
            self.db.set_code(account, code)
            return code
        except Exception as e:
            return None

    def get_raw_code(self, account):
        try:
            code = super().get_code(account)
            return code
        except Exception as e:
            return None

    def set_code(self, account, code):
        self.db.set_code(account, code)

    def set_abi(self, account, abi):
        super().set_abi(account, abi)
        self.db.set_abi(account, abi)

    def get_abi(self, account):
        if account == config.main_token_contract:
            return defaultabi.eosio_token_abi
        elif account == config.system_contract:
            if config.main_token in defaultabi.eosio_system_abi:
                return defaultabi.eosio_system_abi[config.main_token]
            else:
                return defaultabi.eosio_system_abi['EOS']

        abi = self.db.get_abi(account)
        if abi:
            return abi

        abi = super().get_abi(account)
        if abi and 'abi' in abi:
            abi = json.dumps(abi['abi'])
            self.db.set_abi(account, abi)
        else:
            abi = ''
            self.db.set_abi(account, abi)
        return abi

    def get_packed_abi(self, account):
        abi = self.db.get_abi(account)
        if isinstance(abi, bytes):
            return abi

        abi = super().get_abi(account)
        if abi and 'abi' in abi:
            abi = json.dumps(abi['abi'])
            self.db.set_abi(account, abi)
        else:
            abi = ''
            self.db.set_abi(account, abi)
        return eosapi.pack_abi(abi)

    def deploy_contract(self, account, code, abi, vm_type=0, vm_version=0, sign=True, compress=0):
        origin_abi = abi
        actions = []
        setcode = {"account":account,
                "vmtype":vm_type,
                "vmversion":vm_version,
                "code":code.hex()
        }
        setcode = self.pack_args(config.system_contract, 'setcode', setcode)
        setcode = [config.system_contract, 'setcode', setcode, {account:'active'}]
        actions.append(setcode)

        if abi:
            if isinstance(abi, dict):
                abi = json.dumps(abi)
            abi = _uuosapi.pack_abi(abi)
            assert abi
        else:
            abi = b''
        setabi = self.pack_args(config.system_contract, 'setabi', {'account':account, 'abi':abi.hex()})
        setabi = [config.system_contract, 'setabi', setabi, {account:'active'}]
        actions.append(setabi)

        ret = self.push_actions(actions, compress)
        if 'error' in ret:
            raise Exception(ret['error'])

        self.set_abi(account, origin_abi)

        return ret

    def deploy_code(self, account, code, vm_type=0, vm_version=0):
        setcode = {"account":account,
                "vmtype":vm_type,
                "vmversion":vm_version,
                "code":code.hex()
                }
        setcode = self.pack_args(config.system_contract, 'setcode', setcode)
        ret = self.push_action(config.system_contract, 'setcode', setcode, {account:'active'})
        self.db.remove_code(account)
        return ret

    def deploy_abi(self, account, abi):
        if isinstance(abi, dict):
            abi = json.dumps(abi)

        abi = _uuosapi.pack_abi(abi)
        setabi = self.pack_args(config.system_contract, 'setabi', {'account':account, 'abi':abi.hex()})    
        ret = self.push_action(config.system_contract, 'setabi', setabi, {account:'active'})
        self.db.remove_abi(account)
        self.clear_abi_cache(account)
        return ret


    def deploy_python_contract(self, account, code, abi, deploy_type=0):
        actions = []
        origin_abi = abi
        if config.contract_deploy_type == 0:
            setcode = {"account": account,
                    "vmtype": 1,
                    "vmversion": 0,
                    "code":code.hex()
            }
            setcode = self.pack_args(config.system_contract, 'setcode', setcode)
            setcode = [config.system_contract, 'setcode', setcode, {account:'active'}]
            actions.append(setcode)

            abi = _uuosapi.pack_abi(abi)
            if abi:
                setabi = self.pack_args(config.system_contract, 'setabi', {'account':account, 'abi':abi.hex()})
                setabi = [config.system_contract, 'setabi', setabi, {account:'active'}]
                actions.append(setabi)

        elif config.contract_deploy_type in (1, 2):
            if config.contract_deploy_type == 2:
                python_contract = account
            else:
                python_contract = config.python_contract

            args = self.s2b(account) + code
            setcode = [python_contract, 'setcode', args, {account:'active'}]
            actions.append(setcode)

            abi = _uuosapi.pack_abi(abi)
            if abi:
                setabi = self.s2b(account) + abi
                setabi = [python_contract, 'setabi', setabi, {account:'active'}]
                actions.append(setabi)
        else:
            assert 0

        ret = None
        if actions:
            ret = self.push_actions(actions)

        self.set_abi(account, origin_abi)
        return ret

    def deploy_python_code(self, account, code, deploy_type=0):
        actions = []
        if deploy_type == 0:
            setcode = {"account":account,
                    "vmtype": 1,
                    "vmversion": 0,
                    "code":code.hex()
            }
            setcode = self.pack_args(config.system_contract, 'setcode', setcode)
            setcode = [config.system_contract, 'setcode', setcode, {account:'active'}]
            actions.append(setcode)

        elif deploy_type == 1:
            args = self.s2b(account) + code
            setcode = [config.python_contract, 'setcode', args, {account:'active'}]
            actions.append(setcode)
        else:
            assert 0

        ret = None
        if actions:
            ret = self.push_actions(actions)
        return ret

    def deploy_module(self, account, module_name, code, deploy_type=1):
        args = self.s2b(account) + self.s2b(module_name) + code
        if deploy_type == 0:
            contract = account
        else:
            contract = config.python_contract

        return self.push_action(contract, 'setmodule', args, {account:'active'})

    def exec(self, account, args, permissions = {}):
        if isinstance(args, str):
            args = args.encode('utf8')

        if not isinstance(args, bytes):
            args = str(args)
            args = args.encode('utf8')
        
        if not permissions:
            permissions = {account: 'active'}

        args = self.s2b(account) + args
        if config.contract_deploy_type == 1:
            return self.push_action(config.python_contract, 'exec', args, permissions)
        else:
            return self.push_action(account, 'exec', args, permissions)

    def get_public_keys(self, account_name, perm_name):
        keys = []
        for public_key in self.get_keys(account_name, perm_name):
            keys.append(public_key['key'])
        return keys

    def get_keys(self, account_name, perm_name):
        keys = []
        threshold = self._get_keys(account_name, perm_name, keys, 3)
        return (threshold, keys)

    def _get_keys(self, account_name, perm_name, keys, depth):
        threshold = 1
        if depth <= 0:
            return threshold
        info = self.get_account(account_name)
        if not info:
            raise Exception(f'account {account_name} does not exists!')
        for per in info['permissions']:
            if perm_name != per['perm_name']:
                continue
            for key in per['required_auth']['keys']:
                keys.append(key)
            threshold = per['required_auth']['threshold']
            for account in per['required_auth']['accounts']:
               actor = account['permission']['actor']
               per = account['permission']['permission']
               weight = account['weight']
               self._get_keys(actor, per, keys, depth-1)
        return threshold
