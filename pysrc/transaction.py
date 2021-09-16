import json
from . import _uuoskit
from .common import check_result

class Transaction(object):
    def __init__(self, expiration=0, ref_block=None, chain_id=None):
        if ref_block is None:
            self.idx = -1
            return
        self.idx = _uuoskit.transaction_new(expiration, ref_block, chain_id)

    @staticmethod
    def from_json(json_str):
        t = Transaction()
        r = _uuoskit.transaction_from_json(json_str)
        idx = check_result(r)
        if idx == -1:
            raise Exception('Invalid transaction idx')
        t.idx = idx
        return t

    def add_action(self, contract, action, args, permissions):
        ret = _uuoskit.transaction_add_action(self.idx, contract, action, args, permissions)
        check_result(ret)

    def sign(self, pub_key):
        r = _uuoskit.transaction_sign(self.idx, pub_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def pack(self, compress=False):
        r = _uuoskit.transaction_pack(self.idx, compress)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def marshal(self):
        r = _uuoskit.transaction_marshal(self.idx)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def json(self):
        return self.marshal()

    def free(self):
        if not self.idx == -1:
            _uuoskit.transaction_free(self.idx)
            self.idx = -1

    def __delete__(self):
        self.free()
