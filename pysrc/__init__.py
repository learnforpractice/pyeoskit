import os
import sys
from .http_client import HttpClient
from .rpc_interface import RPCInterface, WalletClient
from .chainapi_sync import ChainApi
from uuoskit import _uuoskit

__version__='0.8.5'

_uuoskit.init()

uuosapi = ChainApi()
