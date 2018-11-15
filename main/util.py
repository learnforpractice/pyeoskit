from . import eosapi

def create_account_on_chain(from_account, new_account, balance, public_key):
    assert len(new_account) == 12
    assert balance <= 1.0
    assert len(public_key) == 53 and public_key[:3] == 'EOS'
    memo = '%s-%s'%(new_account, public_key)
    return eosapi.transfer(from_account, 'signupeoseos', balance, memo)

def buyrambytes(payer, receiver, _bytes):
    args = {"payer":payer,"receiver":receiver,"bytes":_bytes}
    return eosapi.push_action('eosio', 'buyrambytes', args, {payer:'active'})

def buyram(payer, receiver, quant):
    args = {'payer':payer, 'receiver':receiver, 'quant':'%.4f EOS'%(quant,)}
    return eosapi.push_action('eosio', 'buyram', args, {payer:'active'})

def sellram(account, _bytes):
    return eosapi.push_action('eosio', 'sellram', {'account':account, 'bytes':_bytes}, {account:'active'})

def dbw(_from, _to, net, cpu):
    args = {'from':_from, 
            'receiver':_to, 
            'stake_net_quantity':'%.4f EOS'%(net,), 
            'stake_cpu_quantity':'%.4f EOS'%(cpu,), 
            'transfer':False
            }
    return eosapi.push_action('eosio', 'delegatebw', args, {_from:'active'})

def undbw(_from, _to, net, cpu):
    args = {'from':_from, 
            'receiver':_to, 
            'unstake_net_quantity':'%.4f EOS'%(net,), 
            'unstake_cpu_quantity':'%.4f EOS'%(cpu,), 
            'transfer':False
            }
    return eosapi.push_action('eosio', 'undelegatebw', args, {_from:'active'})
