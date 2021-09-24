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
    def from_json(tx, chain_id=None):
        t = Transaction()
        if isinstance(tx, dict):
            tx = json.dumps(tx)
        if chain_id is None:
            chain_id = '00'*32
        r = _uuoskit.transaction_from_json(tx, chain_id)
        idx = check_result(r)
        if idx == -1:
            raise Exception('Invalid transaction idx')
        t.idx = idx
        return t

    def set_chain_id(self, chain_id):
        ret = _uuoskit.transaction_set_chain_id(self.idx, chain_id)
        return check_result(ret)

    def add_action(self, contract, action, args, permissions):
        ret = _uuoskit.transaction_add_action(self.idx, contract, action, args, permissions)
        check_result(ret)

    def sign(self, pub_key):
        r = _uuoskit.transaction_sign(self.idx, pub_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def sign_by_private_key(self, priv_key):
        r = _uuoskit.transaction_sign_by_private_key(self.idx, priv_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def pack(self, compress=False):
        r = _uuoskit.transaction_pack(self.idx, compress)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return json.loads(r['data'])

    @staticmethod
    def unpack(tx):
        ret = _uuoskit.transaction_unpack(tx)
        return check_result(ret)

    def marshal(self):
        r = _uuoskit.transaction_marshal(self.idx)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def json(self):
        return self.marshal()

    def free(self):
        if self.idx == -1:
            return
        ret = _uuoskit.transaction_free(self.idx)
        ret = check_result(ret)
        self.idx = -1

    def __delete__(self):
        self.free()
