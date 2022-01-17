from pyeoskit import eosapi, wallet
eosapi.set_node('https://api.eosn.io')

#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

payer = 'testaccount1'
receiver = 'testaccount2'
args = {"payer":payer,"receiver":receiver,"bytes":10*1024}
eosapi.push_action('eosio', 'buyrambytes', args, {payer:'active'})
