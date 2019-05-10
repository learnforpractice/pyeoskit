default_nodes = [
'https://mainnet.eoscalgary.io',
'https://api.eosnewyork.io',
'https://api.eosdetroit.io',
'http://api.hkeos.com',
'https://bp.cryptolions.io',
'http://dc1.eosemerge.io:8888',
'https://dc1.eosemerge.io:5443',
'https://api1.eosdublin.io',
'https://api2.eosdublin.io',
'https://mainnet.eoscannon.io',
'https://eos-api.privex.io',
'https://eosapi.blockmatrix.network',
'https://user-api.eoseoul.io',
'https://api.eos.bitspace.no',
'https://node.eosflare.io',
'https://api-eos.blckchnd.com',
'https://mainnet.eosimpera.com',
'https://eos.greymass.com',
]

nodes = []
def set_nodes(_nodes):
    global nodes
    nodes = _nodes
#set in eosapi.py:EosApi.__init__
get_abi = None
main_token = 'EOS'
