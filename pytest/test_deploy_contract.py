from pyeoskit import eosapi
from pyeoskit import wallet

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
wallet.unlock('mywallet', psw)
wallet.import_key('mywallet', '5JbDP55GXN7MLcNYKCnJtfKi9aD2HvHAdY7g8m67zFTAFkY1uBB')

code = b'''
import db
from eoslib import N, read_action, send_inline, transfer_inline

def sayHello():
    n = N('hello')
    id = N('name')

    name = read_action()
    print('hello', name)
    code = n
    scope = n
    table = n
    payer = n
    itr = db.find_i64(code, scope, table, id)
    if itr >= 0: # value exist, update it
        old_name = db.get_i64(itr)
        print('hello,', old_name)
        db.update_i64(itr, payer, name)
    else:
        db.store_i64(scope, table, payer, id, name)

def play():
    from backyard import garden
    garden.play()

def apply(receiver, code, action):
    if action == N('sayhello'):
        sayHello()
    elif action == N('play'):
        transfer_inline('eosio', 100)
#        send_inline('hello', 'sayhello', b'hello,world', {'hello':'active'})
#        play()
'''
print(type(code))
abi = b'''
{
  "version": "eosio::abi/1.0",
  "structs": [{
     "name": "message",
     "base": "",
     "fields": [
        {"name":"msg", "type":"string"}
     ]
  }
  ],
  "actions": [{
      "name": "sayhello",
      "type": "raw"
    }
  ]
}
'''
r = eosapi.pack_abi(abi)
print(r)
#import sys;sys.exit(0)

eosapi.deploy_contract('hello', code, abi, 1)
r = eosapi.push_action('hello', 'sayhello', b'hello,world', {'hello':'active'})
print(r)



