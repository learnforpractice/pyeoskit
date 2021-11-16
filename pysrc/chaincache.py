import os
import sys
import json
import time
import pickle

default_db = {
    'EOS':  {'chain_info': None, 'accounts':{}, 'abis':{}, 'codes':{}},
}

class ChainCache(object):
    def __init__(self, client, network):
        self.network = network
        self.client = client
        self.db = default_db

    def reset(self):
        self.db = default_db

    def save(self):
        pass

    def get_value(self, key):
        try:
            return self.db[self.network][key]
        except Exception:
            return None

    def set_value(self, key, value):
        self.db[self.network][key] = value
        self.save()

    def set_info(self, info):
        self.set_value('chain_info',info)

    def get_info(self, info):
        self.set_value('chain_info',info)

    def get_code(self, account):
        if account in self.db[self.network]['codes']:
            return self.db[self.network]['codes'][account]
        return None

    def set_code(self, account, code):
        self.db[self.network]['codes'][account] = code

    def remove_code(self, account):
        if account in self.db[self.network]['codes']:
            del self.db[self.network]['codes'][account]

    def get_abi(self, account):
        if account in self.db[self.network]['abis']:
            return self.db[self.network]['abis'][account]
        return None

    def set_abi(self, account, abi):
        self.db[self.network]['abis'][account] = abi

    def remove_abi(self, account):
        if account in self.db[self.network]['abis']:
            del self.db[self.network]['abis'][account]

    def set_account(self, account, info):
        if not isinstance(info, dict):
            info = json.loads(info)
        self.db[self.network]['accounts'][account] = info

    def get_account(self, account):
        try:
            return self.db[self.network]['accounts'][account]
        except KeyError:
            try:
                ret = self.client.get_account(account)
                self.set_account(account, ret)
                return ret
            except Exception as e:
                print(e)
                return None

    def get_public_keys(self, account, key_type):
        account_info = self.get_account(account)
        permissions = account_info['permissions']
        for per in permissions:
            if per['perm_name'] == key_type:
                keys = []
                for key in per['required_auth']['keys']:
                    keys.append(key['key'])
                return keys
