import os
import sys
import json
import pickle

from Crypto.Cipher import AES
from .http_client import HttpClient
from .client import Client, WalletClient
from . import _hello as hello
from . import eosapi

wallet = _hello.wallet
eosapi = eosapi.EosApi()

def create_with_password(name, psw):
    psw = psw.ljust(16)
    obj = AES.new(psw, AES.MODE_CBC, 'This is an IV456')
    key = wallet.create(name)
    key = key.ljust(64)
    ciphertext = obj.encrypt(key)
    with open(name+'.psw', 'wb') as f:
        pickle.dump(ciphertext, f)

def unlock_with_password(name, psw):
    psw = psw.ljust(16)
    obj = AES.new(psw, AES.MODE_CBC, 'This is an IV456')
    with open(name+'.psw', 'rb') as f:
        ciphertext = pickle.load(f)
    key = obj.decrypt(ciphertext)
    key = key.strip()
    return wallet.unlock(name, key)

wallet.create_with_password = create_with_password
wallet.unlock_with_password = unlock_with_password

