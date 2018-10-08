import json
from .http_client import HttpClient
from .client import Client, WalletClient
from . import _hello as hello

wallet = _hello.wallet
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

class EosApi(object):
    def __init__(self):
        self.client = Client()

    def add_nodes(nodes):
        self.client = Client(nodes=nodes)

    def __getattr__(self, attr):
        func = getattr(self.client, attr)
        return Function(func)

eosapi = EosApi()

