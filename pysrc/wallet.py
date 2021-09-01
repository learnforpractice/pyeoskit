import json
import json as json_
from typing import List, Dict, Union

from . import _uuoskit
from .exceptions import WalletException

def check_result(result, json=False):
    ret = json_.loads(result)
    if 'error' in ret:
        raise WalletException(ret['error'])
    return ret['data']

def create(name):
    pass

def save(name):
    pass

def open(name):
    pass

def set_dir(path_name):
    pass

def set_timeout(secs):
    pass

def list_wallets() -> List[bytes]:
    pass

def list_keys(name, psw) -> Dict[str, str]:
    pass

def get_public_keys():
    pass

def lock_all():
    pass

def lock(name):
    pass

def unlock(name, password):
    pass

def import_key(name, wif_key, save=True):
    _uuoskit.wallet_import(name, wif_key)

def remove_key(name, password, pub_key):
    pass

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
