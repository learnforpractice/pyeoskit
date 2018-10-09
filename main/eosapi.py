import json

from . import _hello
from . import db
from .client import Client, WalletClient
from . import _hello as hello

_eosapi = _hello._eosapi

class JsonStruct(object):
    def __init__(self, js):
        if isinstance(js, bytes):
            js = js.decode('utf8')
            js = json.loads(js)
        if isinstance(js, str):
            js = json.loads(js)
        self._dict = js

    def __getattr__(self, attr):
        if attr in self._dict:
            ret = self._dict[attr]
            if isinstance(ret, dict):
                ret = JsonStruct(ret)
            return ret
        super(JsonStruct, self).__getattr__(attr)

    def __str__(self):
        return json.dumps(self, default=lambda x: x._dict, sort_keys=False, indent=4, separators=(',', ': '))

    def __repr__(self):
        return json.dumps(self, default=lambda x: x._dict, sort_keys=False, indent=4, separators=(',', ': '))

    def __getitem__(self, o):
        return self._dict[o]

    def __contains__(self, o):
        return o in self._dict

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

class EosApi(object):
    def __init__(self):
        self.client = Client()

    def set_nodes(nodes):
        self.client.set_nodes(nodes)

    def clear_nodes(self):
        self.client.set_nodes([])

    def __getattr__(self, attr):
        if hasattr(self.client, attr):
            func = getattr(self.client, attr)
            if attr == 'get_account':
                return GetAccountFunction(func)
            elif attr == 'get_code':
                return GetCodeFunction(func)

            return Function(func)
        elif hasattr(_eosapi, attr):
            func = getattr(_eosapi, attr)
            return func
        raise Exception(f"{attr} not found")
