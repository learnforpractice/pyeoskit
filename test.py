import time
from pyeoskit import eosapi
from pyeoskit import Client

print(eosapi)
if False:
    info = eosapi.get_info()
    print(info)
    
    block = eosapi.get_block(1)
    print(block)
    
    
    state = eosapi.get_block_header_state(info.last_irreversible_block_num)
    print(state)
    
    account = eosapi.get_account('hello')
    print(account)
    
    code = eosapi.get_code('hello')
    print(code)

    abi = eosapi.get_abi('hello')
    print(abi)

    abi = eosapi.get_raw_code_and_abi('hello')
    print(abi)

    abi = eosapi.get_raw_abi('hello')
    print(abi)

    info = eosapi.get_producers(True, 0)
    print(info)

    info = eosapi.get_producer_schedule()
    print(info)

    args = {"from": 'eosio',
            "to": 'hello',
            "quantity": '0.0001 EOS',
            "memo": 'hello,world'
    }
    
    r = eosapi.abi_json_to_bin('eosio.token', 'transfer', args)
    print(r)
binargs = '0000000000ea305500000000001aa36a010000000000000004454f53000000000b68656c6c6f2c776f726c64'
eosapi.abi_bin_to_json('eosio.token', 'transfer', binargs)

'''
client = Client(['http://127.0.0.1:8888'])
info = client.get_info()
print(info)
'''



