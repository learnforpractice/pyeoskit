import json
import json as json_
from typing import List, Dict, Union

from . import _wallet
from . import _uuosapi
from .exceptions import WalletException

def raise_last_error():
    raise WalletException(_uuosapi.get_last_error())

def check_result(result, json=False):
    if not result:
        raise_last_error()
    if json:
        return json_.loads(result)
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
    if ret:
        return json.loads(ret)
    return []

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

def sign_transaction(trx: Union[str, dict], public_keys: List[str], chain_id: str, json=False):
    if isinstance(trx, dict):
        trx = json_.dumps(trx)
    trx = _wallet.sign_transaction(trx, public_keys, chain_id)
    return check_result(trx, json)

def sign_transaction_ex(trx: str, public_keys: List[str], chain_id: str, json=False):
    if isinstance(trx, dict):
        trx = json_.dumps(trx)
    tx_id, signatures = _wallet.sign_transaction_ex(trx, public_keys, chain_id)

    if tx_id and signatures:
        return tx_id, json_.loads(signatures)
    raise_last_error()

def sign_raw_transaction(trx: bytes, public_keys: List[str], chain_id: str, json=False):
    assert isinstance(trx, bytes)
    ret = _wallet.sign_raw_transaction(trx, public_keys, chain_id)
    return check_result(ret, json)

def sign_digest(digest, public_key: str):
    return _wallet.sign_digest(digest, public_key)
