import os
import sys
import json
import pickle
from .client import Client
from .jsonstruct import JsonStruct

client = Client()


db_path = os.path.expanduser('~')
db_path = os.path.join(db_path, '.pyeoskit')
if not os.path.exists(db_path):
    os.mkdir(db_path)
db_path = os.path.join(db_path, 'db.pkl')

_db = {'accounts':{}, 'abis':{}}

if os.path.exists(db_path):
    _db = pickle.load(open(db_path, 'rb'))
else:
    pickle.dump(_db, open(db_path, 'wb'))

def reset():
    global _db
    _db = {'accounts':{}, 'abis':{}}
    pickle.dump(_db, open(db_path, 'wb'))

def set_info(info):
    _db['chain_info'] = info
    pickle.dump(_db, open(db_path, 'wb'))

def get_info():
    try:
        return JsonStruct(_db['chain_info'])
    except:
        info = client.get_info()
        set_info(info)
        return JsonStruct(info)

def get_abi(account):
    return _db['abis'][account]

def set_abi(account, abi):
    _db['abis'][account] = abi
    pickle.dump(_db, open(db_path, 'wb'))

def set_account(account, info):
    if not isinstance(info, dict):
        info = json.loads(info)
    _db['accounts'][account] = info
    pickle.dump(_db, open(db_path, 'wb'))

def get_account(account):
    try:
        return _db['accounts'][account]
    except:
        ret = client.get_account(account)
        set_account(account, ret)
        return ret

def get_public_keys(account, key_type):
    account_info = get_account(account)
    permissions = account_info['permissions']
    for per in permissions:
        if per['perm_name'] == key_type:
            keys = []
            for key in per['required_auth']['keys']:
                keys.append(key['key'])
            return keys
