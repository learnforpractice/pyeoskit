#asyncio example
import asyncio
from pyeoskit import wallet
from pyeoskit.chainapi import ChainApiAsync

#import your account private key here
#wallet.import_key('mywallet', '')

async def test():
    eosapi = ChainApiAsync('https://api.eosn.io')
    info = await eosapi.get_info()
    print(info)
    args = {
        'from': 'test1',
        'to': 'test2',
        'quantity': '1.0000 EOS',
        'memo': 'hello,world'
    }
    r = await eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
    print(r)

asyncio.run(test())
