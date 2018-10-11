from . import eosapi

def create_account_on_chain(from_account, new_account, balance, public_key):
    assert len(new_account) == 12
    assert balance <= 1.0
    assert len(public_key) == 53 and public_key[:3] == 'EOS'
    memo = '%s-%s'%(new_account, public_key)
    return eosapi.transfer(from_account, 'signupeoseos', balance, memo)

def sellram(account, _bytes):
    r = eosapi.push_action('eosio', 'sellram', {'account':account, 'bytes':_bytes}, {account:'active'})
    print(r)

def dbw(_from, _to, net, cpu):
    args = {'from':_from, 
            'receiver':_to, 
            'stake_net_quantity':'%.4f EOS'%(net,), 
            'stake_cpu_quantity':'%.4f EOS'%(cpu,), 
            'transfer':False
            }
    eosapi.push_action('eosio', 'delegatebw', args, {_from:'active'})

def undbw(_from, _to, net, cpu):
    args = {'from':_from, 
            'receiver':_to, 
            'unstake_net_quantity':'%.4f EOS'%(net,), 
            'unstake_cpu_quantity':'%.4f EOS'%(cpu,), 
            'transfer':False
            }
    eosapi.push_action('eosio', 'undelegatebw', args, {_from:'active'})