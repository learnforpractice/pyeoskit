import json
import datetime

from . import _hello
from . import db
from .client import Client, WalletClient
from . import _hello as hello
from .jsonstruct import JsonStruct
from . import config

_eosapi = _hello._eosapi
wallet = _hello.wallet

default_abi = '''
{
   "version": "eosio::abi/1.0",
   "types": [{
      "new_type_name": "account_name",
      "type": "name"
   }],
  "structs": [{
      "name": "transfer",
      "base": "",
      "fields": [
        {"name":"from", "type":"account_name"},
        {"name":"to", "type":"account_name"},
        {"name":"quantity", "type":"asset"},
        {"name":"memo", "type":"string"}
      ]
    },{
     "name": "create",
     "base": "",
     "fields": [
        {"name":"issuer", "type":"account_name"},
        {"name":"maximum_supply", "type":"asset"}
     ]
  },{
     "name": "issue",
     "base": "",
     "fields": [
        {"name":"to", "type":"account_name"},
        {"name":"quantity", "type":"asset"},
        {"name":"memo", "type":"string"}
     ]
  },{
      "name": "account",
      "base": "",
      "fields": [
        {"name":"balance", "type":"asset"}
      ]
    },{
      "name": "currency_stats",
      "base": "",
      "fields": [
        {"name":"supply", "type":"asset"},
        {"name":"max_supply", "type":"asset"},
        {"name":"issuer", "type":"account_name"}
      ]
    }
  ],
  "actions": [{
      "name": "transfer",
      "type": "transfer",
      "ricardian_contract": ""
    },{
      "name": "issue",
      "type": "issue",
      "ricardian_contract": ""
    }, {
      "name": "create",
      "type": "create",
      "ricardian_contract": ""
    }

  ],
  "tables": [{
      "name": "accounts",
      "type": "account",
      "index_type": "i64",
      "key_names" : ["currency"],
      "key_types" : ["uint64"]
    },{
      "name": "stat",
      "type": "currency_stats",
      "index_type": "i64",
      "key_names" : ["currency"],
      "key_types" : ["uint64"]
    }
  ],
  "ricardian_clauses": [],
  "abi_extensions": []
}
'''

class Function(object):
    def __init__(self, function):
        self.function = function
        super(Function, self).__init__()

    def __call__(self, *args):
        ret = self.function(*args)
        try:
            return JsonStruct(ret)
        except json.JSONDecodeError:
            return ret

class GetAccountFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetAccountFunction, self).__init__()

    def __call__(self, *args):
        try:
            ret = self.function(*args)        
            account = args[0]
            db.set_account(account, ret)
            ret = JsonStruct(ret)
            return ret
        except Exception as e:
            pass

class GetCodeFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetCodeFunction, self).__init__()

    def __call__(self, *args):
        account = args[0]
        code = db.get_code(account)
        if not code:
            code = self.function(account)
            if code:
                db.set_code(account, code)
                if 'abi' in code and not db.get_abi(account):
                    db.set_abi(account, json.dumps(code['abi']))
        if code:
            code = JsonStruct(code)
            return code

class GetAbiFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetAbiFunction, self).__init__()

    def __call__(self, *args):
        ret = self.function(*args)
        account = args[0]
        if not db.get_abi(account):
            db.set_abi(account, json.dumps(ret))
        ret = JsonStruct(ret)
        return ret

class EosApi(object):
    def __init__(self):
        self.client = db.client
        config.get_abi = self.get_abi

    def set_nodes(self, nodes):
        self.client.set_nodes(nodes)
    
    def init(self):
        self.get_code('eosio')
        self.get_code('eosio.token')

    def add_node(self, url):
        return self.client.add_node(url)

    def get_nodes(self):
        return self.client.get_nodes()

    def clear_nodes(self):
        self.client.set_nodes([])
        
    def set_default_nodes(self):
        self.set_nodes(config.default_nodes)

    def get_info(self):
        info = self.client.get_info()
        db.set_info(info)
        return db.get_info()
    
    def get_chain_id(self):
        pass

    def __getattr__(self, attr):
        if hasattr(self.client, attr):
            func = getattr(self.client, attr)
            if attr == 'get_account':
                return GetAccountFunction(func)
            elif attr == 'get_code':
                return GetCodeFunction(func)
            elif attr == 'get_abi':
                return GetAbiFunction(func)
            return Function(func)
        elif hasattr(_eosapi, attr):
            func = getattr(_eosapi, attr)
            return func
        raise Exception(attr + " not found")

    def gen_transaction(self, actions, expiration, reference_block_id):
        return _eosapi.gen_transaction(actions, expiration, reference_block_id)

    def push_action(self, contract, action, args, permissions):
        act = [contract, action, args, permissions]
        reference_block_id = self.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        for account in permissions:
            public_keys = self.get_available_public_keys(account, permissions[account])
            keys.extend(public_keys)
#        print(keys)
        trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, 0)
        return self.client.push_transaction(trx)

    def push_actions(self, actions):
        reference_block_id = self.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction(actions, 60, reference_block_id)
        keys = []
        for a in actions:
            permissions = a[3]
            for account in permissions:
                public_keys = self.get_available_public_keys(account, permissions[account])
                keys.extend(public_keys)
        trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, 0)

        return self.client.push_transaction(trx)

    def push_transactions(self, aaa):
        reference_block_id = self.get_info().last_irreversible_block_id
        trxs = []
        for aa in aaa:
            trx = _eosapi.gen_transaction(aa, 60, reference_block_id)
            keys = []
            for a in aa:
                permissions = a[3]
                for account in permissions:
                    public_keys = self.get_available_public_keys(account, permissions[account])
                    keys.extend(key)
            trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
            trx = _eosapi.pack_transaction(trx, 0)
            trxs.append(trx)
        return self.client.push_transactions(trxs)

    def get_available_public_keys(self, account, permission):
        wallet_public_keys = wallet.get_public_keys()
        account_public_keys = self.get_public_keys(account, permission)
        keys = []
        for key in account_public_keys:
            if key in wallet_public_keys:
                keys.append(key)
        return keys

    def create_account(self, creator, account, owner_key, active_key, sign=True):
        actions = []
        args = {'creator': creator,
         'name': account,
         'owner': {'threshold': 1,
                   'keys': [{'key': active_key,
                             'weight': 1}],
                   'accounts': [],
                   'waits': []},
         'active': {'threshold': 1,
                    'keys': [{'key': owner_key,
                              'weight': 1}],
                    'accounts': [],
                    'waits': []}}
        return self.push_action('eosio', 'newaccount', args, {creator:'active'})

    def create_account2(self, creator, account, owner_key, active_key, ram_bytes, stake_net, stake_cpu, sign=True):
        actions = []
        args = {'creator': creator,
         'name': account,
         'owner': {'threshold': 1,
                   'keys': [{'key': active_key,
                             'weight': 1}],
                   'accounts': [],
                   'waits': []},
         'active': {'threshold': 1,
                    'keys': [{'key': owner_key,
                              'weight': 1}],
                    'accounts': [],
                    'waits': []}}
        args = self.pack_args('eosio', 'newaccount', args)
        act = ['eosio', 'newaccount', args, {creator:'active'}]
        actions.append(act)

        args = {'payer':creator, 'receiver':account, 'bytes':ram_bytes}
        args = self.pack_args('eosio', 'buyrambytes', args)
        act = ['eosio', 'buyrambytes', args, {creator:'active'}]
        actions.append(act)

        args = {'from': creator,
         'receiver': account,
         'stake_net_quantity': '%0.4f EOS'%(stake_net,),
         'stake_cpu_quantity': '%0.4f EOS'%(stake_cpu,),
         'transfer': 1}
        args = self.pack_args('eosio', 'delegatebw', args)
        act = ['eosio', 'delegatebw', args, {creator:'active'}]
        actions.append(act)
        self.push_actions(actions)

    def get_balance(self, account, token_account='eosio.token', token_name='EOS'):
        ret = self.client.get_currency_balance(token_account, account, token_name)
        if ret:
            return float(ret[0].split(' ')[0])
        return 0.0

    def transfer(self, _from, _to, _amount, _memo='', token_account='eosio.token', symbol='EOS'):
        args = {"from":_from, "to":_to, "quantity":'%.4f %s'%(_amount,symbol), "memo":_memo}
        return self.push_action(token_account, 'transfer', args, {_from:'active'})

    def get_abi(self, account):
        abi = db.get_abi(account)
        if not abi:
            abi = self.client.get_abi(account)
            if abi and 'abi' in abi:
                abi = json.dumps(abi['abi'])
                db.set_abi(account, abi)
            else:
                abi = ''
                db.set_abi(account, abi)
        if not abi:
            abi = default_abi
        return abi

    def pack_args(self, account, action, args):
        abi = self.get_abi(account)
        return _eosapi.pack_args(abi, action, args)

    def unpack_args(self, account, action, binargs):
        abi = self.get_abi(account)
        return _eosapi.unpack_args(abi, action, binargs)

    def set_contract(self, account, code, abi, vmtype=1, sign=True):
        actions = []
        setcode = {"account":account,
                   "vmtype":vmtype,
                   "vmversion":0,
                   "code":code.hex()
                   }
        setcode = self.pack_args('eosio', 'setcode', setcode)
        setcode = ['eosio', 'setcode', setcode, {account:'active'}]
        actions.append(setcode)

        abi = _eosapi.pack_abi(abi)
        setabi = self.pack_args('eosio', 'setabi', {'account':account, 'abi':abi.hex()})
        setabi = ['eosio', 'setabi', setabi, {account:'active'}]
        actions.append(setabi)
    
        ret = self.push_actions(actions)
        db.remove_code(account)
        db.remove_abi(account)
        return ret

    def create_key(self):
        """ Retrieve a pair of public key / private key. """
        return _eosapi.create_key()

    def get_public_key(self, priv):
        return _eosapi.get_public_key(priv)

    def get_public_keys(self, account_name, perm_name):
        keys = []
        for public_key in self.get_keys(account_name, perm_name):
            keys.append(public_key['key'])
        return keys

    def get_keys(self, account_name, perm_name):
        keys = []
        self._get_keys(account_name, perm_name, keys)
        return keys

    def _get_keys(self, account_name, perm_name, keys):
        """get public keys limited by threshold"""
        for per in self.get_account(account_name).permissions:
            if perm_name != per['perm_name']:
                continue
            for key in per['required_auth']['keys']:
                keys.append(key)
            threshold = per['required_auth']['threshold']
            for account in per['required_auth']['accounts']:
               actor = account['permission']['actor']
               per = account['permission']['permission']
               weight = account['weight']
               self._get_keys(actor, per, keys)

               threshold -= weight
               if threshold <= 0:
                   break



