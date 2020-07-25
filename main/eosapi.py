import json
import datetime

from . import _hello
from . import db
from .client import Client, WalletClient
from . import _hello as hello
from . import config
from . import defaultabi

from . import wallet
from . import _eosapi

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

    def __call__(self, *args, **kwargs):
        ret = self.function(*args, **kwargs)
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
        return code

class GetAbiFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetAbiFunction, self).__init__()

    def __call__(self, *args):
        account = args[0]
        if account == 'eosio.token':
            return defaultabi.eosio_token_abi
        elif account == 'eosio':
            return defaultabi.eosio_system_abi

        abi =  db.get_abi(account)
        if abi:
            return abi
        ret = self.function(*args)
        db.set_abi(account, json.dumps(ret))
        return ret

class EosApi(object):
    def __init__(self):
        self.client = db.client
        config.get_abi = self.get_abi

    def set_nodes(self, nodes):
        self.client.set_nodes(nodes)

    def set_node(self, node_url):
        self.client.set_nodes([node_url])

    def enable_decode(self, json_format):
        self.client.json_decode = json_format

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

    def push_transaction(self, trx, compress=0):
        trx = _eosapi.pack_transaction(trx, compress)
        return self.client.push_transaction(trx)

    def pack_transaction(self, trx, compress=0):
        return _eosapi.pack_transaction(trx, compress)

    def unpack_transaction(self, trx):
        return _eosapi.unpack_transaction(trx)

    def push_action(self, contract, action, args, permissions, compress=0):
        act = [contract, action, args, permissions]
        reference_block_id = self.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        for account in permissions:
            public_keys = self.get_available_public_keys(account, permissions[account])
            keys.extend(public_keys)
#        print(keys)
        trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, compress)
        return self.client.push_transaction(trx)

    def push_actions(self, actions, compress=0):
        reference_block_id = self.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction(actions, 60, reference_block_id)
        keys = []
        for a in actions:
            permissions = a[3]
            for account in permissions:
                public_keys = self.get_available_public_keys(account, permissions[account])
                keys.extend(public_keys)
        trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, compress)

        return self.client.push_transaction(trx)

    def push_transactions(self, aaa, expiration=60):
        reference_block_id = self.get_info().last_irreversible_block_id
        trxs = []
        for aa in aaa:
            trx = _eosapi.gen_transaction(aa, expiration, reference_block_id)
            keys = []
            for a in aa:
                permissions = a[3]
                for account in permissions:
                    public_keys = self.get_available_public_keys(account, permissions[account])
                    keys.extend(public_keys)
            trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
            trx = _eosapi.pack_transaction(trx, 0)
            trxs.append(trx)
        return self.client.push_transactions(trxs)

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

    def create_account(self, creator, account, owner_key, active_key, ram_bytes=0, stake_net=0.0, stake_cpu=0.0, sign=True):
        actions = []
        args = {
        'creator': creator,
        'name': account,
        'owner': {'threshold': 1,
                   'keys': [{'key': owner_key, 'weight': 1}],
                   'accounts': [],
                   'waits': []
                },
        'active': {'threshold': 1,
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
            ret = self.client.get_currency_balance(token_account, account, token_name)
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

        abi = db.get_abi(account)
        if not abi:
            abi = self.client.get_abi(account)
            if abi and 'abi' in abi:
                abi = json.dumps(abi['abi'])
                db.set_abi(account, abi)
            else:
                abi = ''
                db.set_abi(account, abi)
        return abi

    def pack_args(self, account, action, args):
        abi = self.get_abi(account)
        return _eosapi.pack_args(account, action, args)

    def unpack_args(self, account, action, binargs):
        abi = self.get_abi(account)
        return _eosapi.unpack_args(account, action, binargs)

    def clear_abi_cache(self, account):
        return _eosapi.clear_abi_cache(account)

    def set_contract(self, account, code, abi, vmtype=1, vmversion=0, sign=True, compress=0):
        actions = []
        if code:
            setcode = {"account":account,
                    "vmtype":vmtype,
                    "vmversion":vmversion,
                    "code":code.hex()
                    }
            setcode = self.pack_args('eosio', 'setcode', setcode)
            setcode = ['eosio', 'setcode', setcode, {account:'active'}]
            actions.append(setcode)

        if abi:
            abi = _eosapi.pack_abi(abi)
            setabi = self.pack_args('eosio', 'setabi', {'account':account, 'abi':abi.hex()})
            setabi = ['eosio', 'setabi', setabi, {account:'active'}]
            actions.append(setabi)
    
        ret = self.push_actions(actions, compress)
        db.remove_code(account)
        db.remove_abi(account)
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
        db.remove_code(account)
        return ret

    def deploy_abi(self, account, abi):
        abi = _eosapi.pack_abi(abi)
        setabi = self.pack_args('eosio', 'setabi', {'account':account, 'abi':abi.hex()})    
        ret = self.push_action('eosio', 'setabi', setabi, {account:'active'})
        db.remove_abi(account)
        self.clear_abi_cache(account)
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
        threshold = self._get_keys(account_name, perm_name, keys, 3)
        return (threshold, keys)

    def _get_keys(self, account_name, perm_name, keys, depth):
        threshold = 1
        if depth <= 0:
            return threshold
        info = self.get_account(account_name)
        for per in info.permissions:
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

    def recover_key(self, digest, sign):
        return _eosapi.recover_key(digest, sign)

    def pack_cpp_object(self, obj_type, json_str):
        return _eosapi.pack_cpp_object(obj_type, json_str)
    
    def unpack_cpp_object(self, obj_type, raw_data):
        return _eosapi.unpack_cpp_object(obj_type, raw_data)

    def sign_digest(self, priv_key, digest):
        if isinstance(digest, str):
            if not len(digest) == 64:
                raise Exception('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
            digest = bytes.fromhex(digest)
        elif isinstance(digest, bytes):
            if not len(digest) == 32:
                raise Exception('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
        else:
            raise TypeError('digest should be a hex str with 64 charactors or a bytes with a size of 32 long')
        return _eosapi.sign_digest(priv_key, digest)

    def set_public_key_prefix(self, prefix):
        _eosapi.set_public_key_prefix(prefix)

