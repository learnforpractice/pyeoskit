from typing import List
from typing import Dict

from . import _wallet

def create(name) :
    return _wallet.create(name)

def save(name) :
    return _wallet.save(name)

def open(name):
    return _wallet.open(name)

def set_dir(path_name):
    return _wallet.set_dir(path_name)

def set_timeout(secs):
    return _wallet.set_timeout(secs)

def list_wallets() -> List[bytes]:
    return _wallet.list_wallets()

def list_keys(name, psw) -> Dict[str, str]:
    return _wallet.list_keys(name, psw)

def get_public_keys():
    return _wallet.get_public_keys()

def lock_all():
    return _wallet.lock_all()

def lock(name):
    return _wallet.lock(name)

def unlock(name, password):
    return _wallet.unlock(name, password)

def import_key(name, wif_key, save=True):
    return _wallet.import_key(name, wif_key, save)

def remove_key(name, password, pub_key):
    return _wallet.remove_key(name, password, pub_key)

def sign_transaction(trx: str, public_keys: List[str], chain_id: str):
    return _wallet.sign_transaction(trx, public_keys, chain_id)

def sign_digest(_digest, public_key: str):
    return _wallet.sign_digest(digest, public_key)
