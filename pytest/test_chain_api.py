from pyeoskit import eosapi

info = eosapi.get_info()

info = eosapi.get_info()
print(info)

block = eosapi.get_block(1)
print(block)


# state = eosapi.get_block_header_state(info['last_irreversible_block_num'])
# print(state)

contract_name = 'hello'

account = eosapi.get_account(contract_name)
print(account)

code = eosapi.get_code(contract_name)
print(code)

abi = eosapi.get_abi(contract_name)
print(abi)

abi = eosapi.get_raw_code_and_abi(contract_name)
print(abi)

abi = eosapi.get_raw_abi(contract_name)
print(abi)

info = eosapi.get_producers(True, 0)
print(info)

info = eosapi.get_producer_schedule()
print(info)

args = {"from": config.system_contract,
        "to": contract_name,
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}

r = eosapi.abi_json_to_bin(config.main_token_contract, 'transfer', args)
print(r)
binargs = '0000000000ea305500000000001aa36a010000000000000004454f53000000000b68656c6c6f2c776f726c64'
eosapi.abi_bin_to_json(config.main_token_contract, 'transfer', binargs)

abi = '''
{
    "version": "eosio::abi/1.0",
    "types": [{
        "new_type_name": "account_name",
        "type": "name"
    }],
    "structs": [{
        "name": "transfer",
        "base": "",
        "fields": [
        {"name":"from", "type":"account_name"},
        {"name":"to", "type":"account_name"},
        {"name":"quantity", "type":"asset"},
        {"name":"memo", "type":"string"}
        ]
    }
    ],
    "actions": [{
        "name": "transfer",
        "type": "transfer",
        "ricardian_contract": ""
    }],
    "tables": [],
    "ricardian_clauses": [],
    "abi_extensions": []
}
'''

eosapi.set_abi(config.main_token_contract, abi)

args = {"from": config.system_contract,
        "to": contract_name,
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}

r = eosapi.pack_args(abi, 'transfer', args)
print(r)

args = {"from": contract_name,
        "to": config.system_contract,
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}
action = [config.main_token_contract, 'transfer', args, {contract_name:'active'}]

info = eosapi.get_info()
reference_block_id = info['last_irreversible_block_id']
trx = eosapi.generate_transaction([action], 60, reference_block_id)
print(trx)

trx = eosapi.sign_transaction(trx, '5JbDP55GXN7MLcNYKCnJtfKi9aD2HvHAdY7g8m67zFTAFkY1uBB', info.chain_id)
print(trx)

trx = eosapi.pack_transaction(trx, 0)
print(trx)
eosapi.push_transaction(trx)

info = eosapi.get_code(contract_name)
print(info)


