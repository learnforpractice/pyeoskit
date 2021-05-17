default_nodes = [
'https://public.eosinfra.io',
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
'https://uuosapi.blockmatrix.network',
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
#set in uuosapi.py:uuosapi.__init__

main_token = 'EOS'
system_contract = 'eosio'
main_token_contract = 'eosio.token'
python_contract = 'uuoscontract'
contract_deploy_type = 0
network_url = ''

code_permission_name = 'eosio.code'

network = 'EOS_TESTNET'

def config_network(_system_contract, _main_token_contract, _main_token):
    global system_contract
    global main_token
    global main_token_contract
    global code_permission_name

    system_contract = _system_contract
    main_token_contract = _main_token_contract
    main_token = _main_token

def setup_uuos_network():
    global main_token
    global system_contract
    global main_token_contract
    global code_permission_name
    main_token = 'UUOS'
    system_contract = 'eosio'
    main_token_contract = 'eosio.token'
    network_url = 'http://127.0.0.1:8888'
    code_permission_name = 'eosio.code'
    from uuoskit import uuosapi
    uuosapi.set_public_key_prefix(main_token)

def setup_uuos_test_network(url = 'http://127.0.0.1:8888', deploy_type=1):
    global main_token
    global system_contract
    global main_token_contract
    global python_contract
    global network_url
    global code_permission_name
    global contract_deploy_type

    contract_deploy_type = deploy_type
    network_url = url

    main_token = 'UUOS'
    system_contract = 'eosio'
    main_token_contract = 'eosio.token'
    code_permission_name = 'eosio.code'

    python_contract = 'hello'
    from uuoskit import uuosapi
    uuosapi.set_public_key_prefix(main_token)

def setup_eos_network():
    global main_token
    global system_contract
    global main_token_contract
    global code_permission_name
    global network_url

    main_token = 'EOS'
    system_contract = 'eosio'
    main_token_contract = 'eosio.token'
    network_url = 'https://eos.greymass.com'
    code_permission_name = 'eosio.code'
    from uuoskit import uuosapi
    uuosapi.set_public_key_prefix(main_token)

def setup_eos_test_network(url = 'https://api.testnet.eos.io', deploy_type=1):
    global main_token
    global system_contract
    global main_token_contract
    global python_contract
    global network_url
    global code_permission_name
    global contract_deploy_type

    import os
    from uuoskit import uuosapi, wallet

    contract_deploy_type = deploy_type
    network_url = url

    main_token = 'TNT'
    system_contract = 'eosio'
    main_token_contract = 'eosio.token'
    python_contract = 'ceyelqpjeeia'
    code_permission_name = 'eosio.code'
    uuosapi.set_public_key_prefix('EOS')

    if os.path.exists('test.wallet'):
        os.remove('test.wallet')
    wallet.create('test')
    # import active key for hello
    wallet.import_key('test', '5JRYimgLBrRLCBAcjHUWCYRv3asNedTYYzVgmiU4q2ZVxMBiJXL')
    # import active key for helloworld11
    wallet.import_key('test', '5Jbb4wuwz8MAzTB9FJNmrVYGXo4ABb7wqPVoWGcZ6x8V2FwNeDo')
    # active key of ceyelqpjeeia
    wallet.import_key('test', '5JfZz1kXF8TXsxQgwfsvZCUBeTQefYSsCLDSbSPmnbKQfFmtBny')

    # active key of ebvjmdibybgq
    wallet.import_key('test', '5KiVDjfHMHXzxrcLqZxGENrhCcCXBMSXP7paPbJWiMCDRMbStsF')
