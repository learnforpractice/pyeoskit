from pyeoskit import eosapi, wallet
eosapi.set_node('https://api.eosn.io')

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

account = 'testaccount1'
args = {
    'account': account,
    'bytes': 100*1024
}
r = eosapi.push_action('eosio', 'sellram', args, {account: 'active'})
