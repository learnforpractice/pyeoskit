# sign with ledger example

from pyeoskit import eosapi
from pyeoskit import ledger
eosapi.set_node('https://api.eosn.io')
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}
pub_key = ledger.get_public_key(0)
print('++++public key:', pub_key)
#indices is an array of ledger signing key indices
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'}, indices=[0])
