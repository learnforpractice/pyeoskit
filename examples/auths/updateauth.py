#add public key as permission to account example

from pyeoskit import eosapi, wallet
eosapi.set_node('https://api.eosn.io')

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

#account to update authorization
account = 'testaccount'
#new permission key to add
pub_key = 'EOS6wJhZLfAjG9F9nXJL3x5EJRpEBximZqmoST7hskqQ3AYBVv9bm'

args = {
    "account": account,
    "permission": "active",
    "parent": "owner",
    "auth": {
        "threshold": 1,
        "keys": [{'key': pub_key, 'weight': 1}],
        "accounts": [
        ],
        "waits": []
    }
}

eosapi.push_action('eosio', 'updateauth', args, {account: 'active'})
