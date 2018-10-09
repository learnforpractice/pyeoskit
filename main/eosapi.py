import json

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
        raise Exception(f"{attr} not found")

    def push_action(self, contract, action, args, permissions):
        act = [contract, action, args, permissions]
        reference_block_id = db.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction([act], 60, reference_block_id)

        keys = []
        for account in permissions:
            keys.extend(db.get_public_keys(account, permissions[account]))

        trx = wallet.sign_transaction(trx, keys, db.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, 0)
        return self.client.push_transaction(trx)

    def push_actions(self, actions):
        reference_block_id = db.get_info().last_irreversible_block_id
        trx = _eosapi.gen_transaction(actions, 60, reference_block_id)
        keys = []
        for a in actions:
            permissions = a[3]
            for account in permissions:
                keys.extend(db.get_public_keys(account, permissions[account]))
        trx = wallet.sign_transaction(trx, keys, db.get_info().chain_id)
        trx = _eosapi.pack_transaction(trx, 0)

        return self.client.push_transaction(trx)

    def push_transactions(self, aaa):
        reference_block_id = db.get_info().last_irreversible_block_id
        trxs = []
        for aa in aaa:
            trx = _eosapi.gen_transaction(aa, 60, reference_block_id)
            keys = []
            for a in aa:
                permissions = a[3]
                for account in permissions:
                    keys.extend(db.get_public_keys(account, permissions[account]))
            trx = wallet.sign_transaction(trx, keys, db.get_info().chain_id)
            trx = _eosapi.pack_transaction(trx, 0)
            trxs.append(trx)
        return self.client.push_transactions(trxs)

