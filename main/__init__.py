import sys
from .http_client import HttpClient
from .client import Client, WalletClient
from . import _hello as hello
__version__='0.7.0'

__all__ = (
    'eosapi',
    'wallet',
)

class CustomImporter(object):
    def find_module(self, fullname, mpath=None):
        if fullname in ['_eosapi', 'pyobject', 'wallet']:
            return self
        return

    def load_module(self, module_name):
        mod = sys.modules.get(module_name)
        if mod is None:
            hello_module = sys.modules.get('pyeoskit._hello')
            if not hello_module:
                return
            hello_so = hello_module.__file__
            from importlib import util
            spec = util.spec_from_file_location(module_name, hello_so)
            mod = util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            sys.modules[module_name] = mod
        return mod

sys.meta_path.append(CustomImporter())

import pyobject
import wallet
import _eosapi

from . import eosapi
eosapi = eosapi.EosApi()

