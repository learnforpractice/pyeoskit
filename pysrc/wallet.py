import json
from typing import List
from typing import Dict

from . import _wallet
from . import _uuosapi
from .exceptions import WalletException

def raise_last_error():
    raise WalletException(_uuosapi.get_last_error())

def check_result(result):
    if not result:
        raise_last_error()
    return result

def create(name):
    psw = _wallet.create(name)
    return check_result(psw)

def save(name):
    return _wallet.save(name)

def open(name):
    return _wallet.open(name)

def set_dir(path_name):
    return _wallet.set_dir(path_name)

def set_timeout(secs):
    return _wallet.set_timeout(secs)

def list_wallets() -> List[bytes]:
    ret = _wallet.list_wallets()
    if not ret:
        raise_last_error()
    return json.loads(ret)

def list_keys(name, psw) -> Dict[str, str]:
    ret = _wallet.list_keys(name, psw)
    if not ret:
        raise_last_error()
    return json.loads(ret)

def get_public_keys():
    ret = _wallet.get_public_keys()
    return json.loads(ret)

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
    ret = _wallet.sign_transaction(trx, public_keys, chain_id)
    return check_result(ret)

def sign_raw_transaction(trx: bytes, public_keys: List[str], chain_id: str):
    assert isinstance(trx, bytes)
    ret = _wallet.sign_raw_transaction(trx, public_keys, chain_id)
    return check_result(ret)

def sign_digest(digest, public_key: str):
    return _wallet.sign_digest(digest, public_key)