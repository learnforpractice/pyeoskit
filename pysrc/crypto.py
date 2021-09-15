from uuoskit import _uuoskit
from .common import check_result

def create_key():
    ret = _uuoskit.crypto_create_key()
    return check_result(ret)
