import json
import json as json_
from typing import List, Dict, Union

from . import _pyeoskit
from .exceptions import WalletException
from .transaction import Transaction

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
    ret = _pyeoskit.wallet_get_public_keys()
    ret = json.loads(ret)
    return ret['data']

def lock_all():
    pass

def lock(name):
    pass

def unlock(name, password):
    pass

def import_key(name, wif_key, save=True):
    ret = _pyeoskit.wallet_import(name, wif_key)
    return check_result(ret)

def remove_key(name, password, pub_key):
    pass

def sign_transaction(trx: Union[str, dict], public_keys: List[str], chain_id: str, json=False):
    if isinstance(trx, dict):
        trx = json_.dumps(trx)
    t = Transaction.from_json(trx, chain_id)
    for pub in public_keys:
        t.sign(pub)
    return t.pack()

def sign_digest(digest: Union[bytes, str], public_key: str):
    if isinstance(digest, bytes):
        digest = digest.hex()
    ret = _pyeoskit.wallet_sign_digest(digest, public_key)
    return check_result(ret)

