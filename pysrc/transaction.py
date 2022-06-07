import json
from . import _pyeoskit
from .common import check_result

class Transaction(object):
    def __init__(self, chain_index, expiration=0, ref_block=None, chain_id=None):
        self.chain_index = chain_index
        if ref_block is None:
            self.idx = -1
            return
        self.idx = _pyeoskit.transaction_new(chain_index, expiration, ref_block, chain_id)
        if self.idx == -1:
            raise Exception("too many transactions has been created!")

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.free()

    @staticmethod
    def from_json(chain_index, tx, chain_id=None):
        t = Transaction(chain_index)
        if isinstance(tx, dict):
            tx = json.dumps(tx)
        if chain_id is None:
            chain_id = '00'*32
        r = _pyeoskit.transaction_from_json(chain_index, tx, chain_id)
        idx = check_result(r)
        if idx == -1:
            raise Exception('Invalid transaction idx')
        t.idx = idx
        return t

    def set_chain_id(self, chain_id):
        ret = _pyeoskit.transaction_set_chain_id(self.chain_index, self.idx, chain_id)
        return check_result(ret)

    def add_action(self, contract, action, args, permissions):
        ret = _pyeoskit.transaction_add_action(self.chain_index, self.idx, contract, action, args, permissions)
        check_result(ret)

    def sign(self, pub_key):
        r = _pyeoskit.transaction_sign(self.chain_index, self.idx, pub_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def digest(self, chainId):
        r = _pyeoskit.transaction_digest(self.chain_index, self.idx, chainId)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def sign_by_private_key(self, priv_key):
        r = _pyeoskit.transaction_sign_by_private_key(self.chain_index, self.idx, priv_key)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        return r['data']

    def pack(self, compress=False, load=False):
        r = _pyeoskit.transaction_pack(self.chain_index, self.idx, compress)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        data = r['data']
        if load:
            data = json.loads(r['data'])
        return data

    @staticmethod
    def unpack(chain_index, tx):
        ret = _pyeoskit.transaction_unpack(tx)
        ret = check_result(ret)
        return Transaction.from_json(chain_index, ret)

    def marshal(self):
        r = _pyeoskit.transaction_marshal(self.chain_index, self.idx)
        r = json.loads(r)
        if 'error' in r:
            raise Exception(r['error'])
        r = json.loads(r['data'])
        return r

    def json(self):
        return self.marshal()

    def free(self):
        if self.idx == -1:
            return
        ret = _pyeoskit.transaction_free(self.chain_index, self.idx)
        ret = check_result(ret)
        self.idx = -1

    def __delete__(self):
        self.free()
