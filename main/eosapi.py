import json
import datetime

from . import _hello
from . import db
from .client import Client, WalletClient
from . import _hello as hello
from .jsonstruct import JsonStruct

_eosapi = _hello._eosapi
wallet = _hello.wallet

class Function(object):
    def __init__(self, function):
        self.function = function
        super(Function, self).__init__()

    def __call__(self, *args):
        ret = self.function(*args)
        return JsonStruct(ret)

class GetAccountFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetAccountFunction, self).__init__()

    def __call__(self, *args):
        ret = self.function(*args)
        account = args[0]
        db.set_account(account, ret)
        ret = JsonStruct(ret)
        return ret

class GetCodeFunction(object):
    def __init__(self, function):
        self.function = function
        super(GetCodeFunction, self).__init__()

    def __call__(self, *args):
        ret = self.function(*args)
        account = args[0]
        if not db.get_abi(account):
            db.set_abi(account, json.dumps(ret['abi']))

        ret = JsonStruct(ret)
        return ret

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

    def set_nodes(self, nodes):
        self.client.set_nodes(nodes)

    def clear_nodes(self):
        self.client.set_nodes([])
    
    def get_info(self):
        block_time = datetime.datetime.strptime(db.get_info().head_block_time, '%Y-%m-%dT%H:%M:%S.%f')
        elapsed = datetime.datetime.utcnow() - block_time
        if elapsed.total_seconds() >= 60:
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

    def push_action(self, contract, action, args, permissions):
        act = [contract, action, args, permissions]
        reference_block_id = self.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        for account in permissions:
            keys.extend(db.get_public_keys(account, permissions[account]))

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
                keys.extend(db.get_public_keys(account, permissions[account]))
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
                    keys.extend(db.get_public_keys(account, permissions[account]))
            trx = wallet.sign_transaction(trx, keys, self.get_info().chain_id)
            trx = _eosapi.pack_transaction(trx, 0)
            trxs.append(trx)
        return self.client.push_transactions(trxs)

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

    def get_balance(account, token_account='eosio.token'):
        ret = self.client.get_currency_balance(token_account, account, 'EOS')
        if ret:
            return ret[0]/10000.0
        return 0.0

    def transfer(_from, _to, _amount, _memo='', token_account='eosio.token'):
        args = {"from":_from, "to":_to, "quantity":'%.4f EOS'%(_amount,), "memo":_memo}
        return self.push_action(token_account, 'transfer', args, {_from:'active'})

    def get_abi(self, account):
        try:
            return db.get_abi(account)
        except KeyError:
            abi = self.client.get_abi(account)
            abi = json.dumps(abi['abi'])
            db.set_abi(account, abi)
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
        return ret

