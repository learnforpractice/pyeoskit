import os
import sys
import json
import pickle
from .client import Client

client = Client()


db_path = os.path.expanduser('~')
db_path = os.path.join(db_path, '.pyeoskit')
if not os.path.exists(db_path):
    os.mkdir(db_path)
db_path = os.path.join(db_path, 'db.pkl')

_db = {'accounts':{}, 'abis':{}, 'codes':{}}

if os.path.exists(db_path):
    try:
        with open(db_path, 'rb') as f:
            _db = pickle.load(f)
    except:
        with open(db_path, 'wb') as f:
            pickle.dump(_db, f)
else:
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def reset():
    global _db
    _db = {'accounts':{}, 'abis':{}, 'codes':{}}
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def set_info(info):
    _db['chain_info'] = info
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def get_info():
    try:
        return _db['chain_info']
    except:
        info = client.get_info()
        set_info(info)
        return info

def get_code(account):
    if account in _db['codes']:
        return _db['codes'][account]
    return None

def set_code(account, code):
    _db['codes'][account] = code
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def remove_code(account):
    if account in _db['codes']:
        del _db['codes'][account]

def get_abi(account):
    if account in _db['abis']:
        return _db['abis'][account]
    return None

def set_abi(account, abi):
    _db['abis'][account] = abi
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def remove_abi(account):
    if account in _db['abis']:
        del _db['abis'][account]

def set_account(account, info):
    if not isinstance(info, dict):
        info = json.loads(info)
    _db['accounts'][account] = info
    with open(db_path, 'wb') as f:
        pickle.dump(_db, f)

def get_account(account):
    try:
        return _db['accounts'][account]
    except KeyError:
        try:
            ret = client.get_account(account)
            set_account(account, ret)
            return ret
        except Exception as e:
            print(e)
            return None

def get_public_keys(account, key_type):
    account_info = get_account(account)
    permissions = account_info['permissions']
    for per in permissions:
        if per['perm_name'] == key_type:
            keys = []
            for key in per['required_auth']['keys']:
                keys.append(key['key'])
            return keys
