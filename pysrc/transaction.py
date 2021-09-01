import json
from uuoskit import _uuoskit

class Transaction(object):
    def __init__(self, expiration, ref_block, chain_id):
        self.idx = _uuoskit.transaction_new(expiration, ref_block, chain_id)

    def add_action(self, contract, action, args, permissions):
        _uuoskit.transaction_add_action(self.idx, contract, action, args, permissions)

    def sign(self, pub_key):
        r = _uuoskit.transaction_sign(self.idx, pub_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def json(self):
        r = _uuoskit.transaction_pack(self.idx)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def free(self):
        if not self.idx == -1:
            _uuoskit.transaction_free(self.idx)
            self.idx = -1

    def __delete__(self):
        self.free()
