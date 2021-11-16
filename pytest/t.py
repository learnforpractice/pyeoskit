#!/Users/newworld/opt/anaconda3/bin/python3
import os
import sys
import json
import subprocess
import logging
from pyeoskit import wallet, eosapi

import httpx

#eosapi.set_node('https://node.eosflare.io')
#eosapi.set_node('https://user-api.eoseoul.io')
#eosapi.set_node('eos.eoscafeblock.com')
#eosapi.set_node('api.hkeos.com')
#eosapi.set_node('https://eos.greymass.com')
eosapi.set_node('api.hkeos.com')
eosapi.set_node('api.eosn.io')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(module)s %(lineno)d %(message)s')
logger=logging.getLogger(__name__)


class JsonStore(object):
    """Replacement of shelve using json, needed for support python 2 and 3.
    """

    def __init__(self, filename):
        super(JsonStore, self).__init__()
        self.filename = filename
        self.data = {}
        if os.path.exists(filename):
            try:
                with open(filename, 'r', encoding='utf8') as fd:
                    self.data = json.load(fd)
            except ValueError:
                logger.warning("Unable to read the state.db, content will be replaced.")

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value
        self.sync()

    def __delitem__(self, key):
        del self.data[key]
        self.sync()

    def __contains__(self, item):
        return item in self.data

    def get(self, item, default=None):
        return self.data.get(item, default)

    def keys(self):
        return self.data.keys()

    def remove_all(self, prefix):
        for key in tuple(self.data.keys()):
            if not key.startswith(prefix):
                continue
            del self.data[key]
        self.sync()

    def sync(self):
        with open(self.filename, 'w', encoding='utf8') as fd:
            json.dump(self.data, fd, ensure_ascii=False)

def get_last_commit():
    id = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    id = id.decode('utf8').strip()
    return id

def commit(commit_id=None):
    user_path = os.path.expanduser('~')
    user_path = os.path.join(user_path, '.cm')
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    wallet.set_dir(user_path)
    properties_path = os.path.join(user_path, '.properties')
    commit_path = os.path.join(user_path, '.commit')

    js = JsonStore(properties_path)

    psw = js.get('psw')
    if not psw:
        psw = wallet.create('.commit')
        if not psw:
            raise Exception('create wallet failed!')
#        print('+++psw:', psw)
        wallet.import_key('.commit', '5JkRtzuX6JBbfnxkf9iRrqYonhQEaqqCMgRThJpxMsSnAxqBzkJ')
        js['psw'] = psw
    else:
#        print(psw)
        wallet.unlock('.commit', psw)
    wallet.import_key('.commit', '5JkRtzuX6JBbfnxkf9iRrqYonhQEaqqCMgRThJpxMsSnAxqBzkJ')

    try:
        id = 'aabbccdd'
#        eosapi.set_node('https://user-api.eoseoul.io')
#        eosapi.set_node('https://node.eosflare.io')
        try:
            r = eosapi.push_action('learnforever', 'sayhello', bytes.fromhex(id), {'learnforever':'sayhello'})
            print(r)
        except Exception as e:
            import time;time.sleep(3.0)
            r = httpx.get('https://api.eospowerup.io/freePowerup/learnforever')
            print(e)
    except subprocess.CalledProcessError as e:
        print(e.output.decode('utf8'))

if __name__ == '__main__':
    commit()
