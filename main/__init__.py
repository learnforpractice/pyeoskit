import os
import sys
import json
import pickle

from .http_client import HttpClient
from .client import Client, WalletClient
from . import _hello as hello
from . import eosapi
__version__='0.6.0'
wallet = _hello.wallet
block_log = _hello.block_log

eosapi = eosapi.EosApi()
