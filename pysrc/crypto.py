from pyeoskit import _pyeoskit
from .common import check_result

def create_key():
    ret = _pyeoskit.crypto_create_key()
    return check_result(ret)
