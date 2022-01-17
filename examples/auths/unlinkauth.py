#unlink authorization example

from pyeoskit import eosapi, wallet
eosapi.set_node('https://api.eosn.io')

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

account = "testaccount"

args = {
    "account": account,
    "code": "eosio.token",
    "type": "transfer",
    "name": "transfer"
}

eosapi.push_action('eosio', 'unlinkauth', args, {account: 'active'})
