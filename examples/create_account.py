#create account example

from pyeoskit import eosapi, wallet

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

#account to update authorization
account = 'testaccount'
#new permission key to add
pub_key = 'EOS6wJhZLfAjG9F9nXJL3x5EJRpEBximZqmoST7hskqQ3AYBVv9bm'

creator = 'helloworld11'
new_account = 'helloworld12'
#ram for new account in bytes
ram_bytes = 3500

actions = []
args = {
    'creator': creator,
    'name': new_account,
    'owner': {
        'threshold': 1,
        'keys': [{'key': pub_key, 'weight': 1}],
        'accounts': [],
        'waits': []
    },
    'active': {
        'threshold': 1,
        'keys': [{'key': pub_key, 'weight': 1}],
        'accounts': [],
        'waits': []
    }
}
act = ['eosio', 'newaccount', args, {creator:'active'}]
actions.append(act)

args = {'payer':creator, 'receiver':new_account, 'bytes':ram_bytes}
act = ['eosio', 'buyrambytes', args, {creator:'active'}]
actions.append(act)
eosapi.push_actions(actions)
