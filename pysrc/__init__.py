import os
import sys
from .http_client import HttpClient
from .rpc_interface import RPCInterface, WalletClient
from .chainapi_sync import ChainApi
from pyeoskit import _pyeoskit

__version__='1.0.6'

_pyeoskit.init()

eosapi = ChainApi()
