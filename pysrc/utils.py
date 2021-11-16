import json
from . import eosapi
from . import config

def create_account_on_chain(from_account, new_account, balance, public_key):
    assert len(new_account) == 12
    assert balance <= 1.0
    assert len(public_key) == 53 and public_key[:3] == 'EOS'
    memo = '%s-%s'%(new_account, public_key)
    return eosapi.transfer(from_account, 'signupeoseos', balance, memo)

def buyrambytes(payer, receiver, _bytes):
    args = {"payer":payer,"receiver":receiver,"bytes":_bytes}
    return eosapi.push_action(config.system_contract, 'buyrambytes', args, {payer:'active'})

def buyram(payer, receiver, quant):
    args = {'payer':payer, 'receiver':receiver, 'quant':'%.4f %s'%(quant, config.main_token)}
    return eosapi.push_action(config.system_contract, 'buyram', args, {payer:'active'})

def sellram(account, _bytes):
    return eosapi.push_action(config.system_contract, 'sellram', {'account':account, 'bytes':_bytes}, {account:'active'})

def dbw(_from, _to, net, cpu, transfer=False):
    args = {'from':_from, 
            'receiver':_to, 
            'stake_net_quantity':'%.4f %s'%(net, config.main_token), 
            'stake_cpu_quantity':'%.4f %s'%(cpu, config.main_token), 
            'transfer':transfer
            }
    return eosapi.push_action(config.system_contract, 'delegatebw', args, {_from:'active'})

def undbw(_from, _to, net, cpu, transfer=False):
    args = {'from':_from, 
            'receiver':_to, 
            'unstake_net_quantity':'%.4f %s'%(net, config.main_token), 
            'unstake_cpu_quantity':'%.4f %s'%(cpu, config.main_token), 
            'transfer':transfer
            }
    return eosapi.push_action(config.system_contract, 'undelegatebw', args, {_from:'active'})
