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

_db = {'accounts':{}, 'abis':{}}

if os.path.exists(db_path):
    _db = pickle.load(open(db_path, 'rb'))
else:
    pickle.dump(_db, open(db_path, 'wb'))

def get_abi(account):
    try:
        return _db['abis'][account]
    except:
        ret = client.get_code(account)
        abi = ret['abi']
        abi = json.dumps(abi)
        set_abi(account, abi)
        return abi

def set_abi(account, abi):
    if isinstance(abi, dict):
        abi = json.dumps(abi)
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

def get_active_key(account):
    if not account in _db['accounts']:
        return None
    permissions = _db['accounts'][account]['permissions']
    for per in permissions:
        if per['perm_name'] == 'active':
            keys = []
            for key in per['required_auth']['keys']:
                keys.append(key['key'])
            return keys
