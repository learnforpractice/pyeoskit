from pyeoskit import eosapi
eosapi.set_node('https://eos.greymass.com')
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}

#indexes is an array of ledger signing key indexes
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'}, indexes=[0])
