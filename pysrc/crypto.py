from pyeoskit import _pyeoskit
from .common import check_result

def create_key(old_format=True):
    ret = _pyeoskit.crypto_create_key(old_format)
    return check_result(ret)
