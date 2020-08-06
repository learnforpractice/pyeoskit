import time
import json
import datetime

from . import config
from . import wallet
from . import _eosapi
from . import defaultabi

from .chaincache import ChainCache
from .client import Client
from .chainnative import ChainNative

class ChainApi(Client, ChainNative):
    def __init__(self, network='EOS', node_url = 'http://127.0.0.1:8888', _async=False):
        super().__init__(_async=_async)

        config.get_abi = self.get_abi
        self.db = ChainCache(self, network)
        self.set_node(node_url)

    def enable_decode(self, json_format):
        super().json_decode = json_format

    def init(self):
        self.get_code('eosio')
        self.get_code('eosio.token')

    def get_chain_id(self):
        return self.get_info()['chain_id']

    def push_transaction(self, trx, compress=0):
        trx = _eosapi.pack_transaction(trx, compress)
        return super().push_transaction(trx)

    def push_action(self, contract, action, args, permissions, compress=0):
        act = [contract, action, args, permissions]
        chain_info = self.get_info()
        reference_block_id = chain_info['last_irreversible_block_id']
        chain_id = chain_info['chain_id']

        trx = _eosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        for account in permissions:
            public_keys = self.get_available_public_keys(account, permissions[account])
            keys.extend(public_keys)
#        print(keys)
        trx = wallet.sign_transaction(trx, keys, chain_id)
        trx = _eosapi.pack_transaction(trx, compress)
        return super().push_transaction(trx)

    def push_actions(self, actions, compress=0):
        chain_info = self.get_info()
        reference_block_id = chain_info['last_irreversible_block_id']
        chain_id = chain_info['chain_id']
        trx = _eosapi.gen_transaction(actions, 60, reference_block_id)
        keys = []
        for a in actions:
            permissions = a[3]
            for account in permissions:
                public_keys = self.get_available_public_keys(account, permissions[account])
                keys.extend(public_keys)
        trx = wallet.sign_transaction(trx, keys, chain_id)
        trx = _eosapi.pack_transaction(trx, compress)

        return super().push_transaction(trx)

    def push_transactions(self, aaa, expiration=60):
        chain_info = self.get_info()
        reference_block_id = chain_info['last_irreversible_block_id']
        chain_id = chain_info['chain_id']

        trxs = []
        for aa in aaa:
            trx = _eosapi.gen_transaction(aa, expiration, reference_block_id)
            keys = []
            for a in aa:
                permissions = a[3]
                for account in permissions:
                    public_keys = self.get_available_public_keys(account, permissions[account])
                    keys.extend(public_keys)
            trx = wallet.sign_transaction(trx, keys, chain_id)
            trx = _eosapi.pack_transaction(trx, 0)
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
        try:
            return super().get_account(account)
        except Exception:
            return None

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
        args = self.pack_args('eosio', 'newaccount', args)
        act = ['eosio', 'newaccount', args, {creator:'active'}]
        actions.append(act)

        if ram_bytes:
            args = {'payer':creator, 'receiver':account, 'bytes':ram_bytes}
            args = self.pack_args('eosio', 'buyrambytes', args)
            act = ['eosio', 'buyrambytes', args, {creator:'active'}]
            actions.append(act)

        if stake_net or stake_cpu:
            args = {
                'from': creator,
                'receiver': account,
                'stake_net_quantity': '%0.4f %s'%(stake_net, config.main_token),
                'stake_cpu_quantity': '%0.4f %s'%(stake_cpu, config.main_token),
                'transfer': 1
            }

        args = self.pack_args('eosio', 'delegatebw', args)
        act = ['eosio', 'delegatebw', args, {creator:'active'}]
        actions.append(act)
        return self.push_actions(actions)

    def get_balance(self, account, token_account='eosio.token', token_name=''):
        if not token_name:
            token_name = config.main_token
        try:
            ret = super().get_currency_balance(token_account, account, token_name)
            if ret:
                return float(ret[0].split(' ')[0])
        except Exception as e:
            return 0.0
        return 0.0

    def transfer(self, _from, _to, _amount, _memo='', token_account='eosio.token', token_name='', permission='active'):
        if not token_name:
            token_name = config.main_token
        args = {"from":_from, "to":_to, "quantity":'%.4f %s'%(_amount,token_name), "memo":_memo}
        return self.push_action(token_account, 'transfer', args, {_from:permission})

    def get_abi(self, account):
        if account == 'eosio.token':
            return defaultabi.eosio_token_abi
        elif account == 'eosio':
            return defaultabi.eosio_system_abi

        abi = self.db.get_abi(account)
        if not abi:
            abi = super().get_abi(account)
            if abi and 'abi' in abi:
                abi = json.dumps(abi['abi'])
                self.db.set_abi(account, abi)
            else:
                abi = ''
                self.db.set_abi(account, abi)
        return abi

    def set_contract(self, account, code, abi, vmtype=1, vmversion=0, sign=True, compress=0):
        actions = []

        setcode = {"account":account,
                "vmtype":vmtype,
                "vmversion":vmversion,
                "code":code.hex()
                }
        setcode = self.pack_args('eosio', 'setcode', setcode)
        setcode = ['eosio', 'setcode', setcode, {account:'active'}]
        actions.append(setcode)

        abi = _eosapi.pack_abi(abi)
        setabi = self.pack_args('eosio', 'setabi', {'account':account, 'abi':abi.hex()})
        setabi = ['eosio', 'setabi', setabi, {account:'active'}]
        actions.append(setabi)

        ret = self.push_actions(actions, compress)
        self.db.remove_code(account)
        self.db.remove_abi(account)
        self.clear_abi_cache(account)
        return ret

    def publish_contract(self, account, code, abi, vmtype=1, vmversion=0, sign=True, compress=0):
        return self.set_contract(account, code, abi, vmtype, vmversion, sign, compress)

    def deploy_contract(self, account, code, abi, vmtype=1, vmversion=0, sign=True, compress=0):
        return self.set_contract(account, code, abi, vmtype, vmversion, sign, compress)

    def deploy_code(self, account, code, vmtype=0, vmversion=0):
        setcode = {"account":account,
                "vmtype":vmtype,
                "vmversion":vmversion,
                "code":code.hex()
                }
        setcode = self.pack_args('eosio', 'setcode', setcode)
        ret = self.push_action('eosio', 'setcode', setcode, {account:'active'})
        self.db.remove_code(account)
        return ret

    def deploy_abi(self, account, abi):
        abi = _eosapi.pack_abi(abi)
        setabi = self.pack_args('eosio', 'setabi', {'account':account, 'abi':abi.hex()})    
        ret = self.push_action('eosio', 'setabi', setabi, {account:'active'})
        self.db.remove_abi(account)
        self.clear_abi_cache(account)
        return ret

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


