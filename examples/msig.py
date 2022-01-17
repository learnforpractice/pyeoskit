#multisig example

from pyeoskit import eosapi, wallet
#account to update authorization
account = 'testaccount'
#new permission key to add
pub_key = 'EOS6wJhZLfAjG9F9nXJL3x5EJRpEBximZqmoST7hskqQ3AYBVv9bm'
#propser account, can not be the same as account to update authorization
proposer = 'proposer'

#import your account private key here
# wallet.import_key('mywallet', '')

eosapi.set_node('https://api.eosn.io')

info = eosapi.get_info()
chain_id = info['chain_id']
ref_block = info['last_irreversible_block_id']

#+++++++++++++++++generate updateauth transaction+++++++++++++++++
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

action = ['eosio', 'updateauth', args, {account: 'active'}]
tx = eosapi.gen_transaction([action], 10*60, ref_block, chain_id)

##++++++++++++propose++++++++++++++
args = {
    "proposer": proposer,
    "proposal_name": 'hello',
    "requested": [
        {'actor': account, 'permission': 'active'}
    ],
    "trx": tx
}
a1 = 'eosio.msig', 'propose', args, {proposer: 'active'}

##++++++++++++approve++++++++++++++
args = {
    'proposer': proposer,
    'proposal_name': 'hello',
    'level': {'actor': account, 'permission': 'active'},
}
a2 = ['eosio.msig', 'approve', args, {account: 'active'}]

##++++++++++++exec++++++++++++++
args = {
    'proposer': proposer,
    'proposal_name': 'hello',
    'executer': proposer
}
a3 = ['eosio.msig', 'exec', args, {proposer: 'active'}]
eosapi.push_actions([a1, a2, a3])
