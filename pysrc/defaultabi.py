import os

cur_dir = os.path.dirname(__file__)

eosio_token_abi = None
with open(os.path.join(cur_dir, 'data/eosio.token.abi'), 'rb') as f:
    eosio_token_abi = f.read()

with open(os.path.join(cur_dir, 'data/eosio.system_eosio.abi'), 'rb') as f:
    eosio_system_abi_eosio = f.read()

eosio_system_abi = dict(
    EOS = eosio_system_abi_eosio,
)