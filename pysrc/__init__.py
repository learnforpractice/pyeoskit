import os
import sys
from .http_client import HttpClient
from .rpc_interface import RPCInterface, WalletClient
from . import _hello as hello

__version__='0.7.0'

__all__ = (
    'chainapi',
    'wallet',
)

class CustomImporter(object):
    def find_module(self, fullname, mpath=None):
        if fullname in ['_uuosapi', '_block_log', 'pyobject', '_wallet']:
            return self
        return

    def load_module(self, module_name):
        mod = sys.modules.get(module_name)
        if mod is None:
            hello_module = sys.modules.get('uuoskit._hello')
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
import _wallet
import _uuosapi
import _block_log

from . import chainapi
uuosapi = chainapi.ChainApi()
