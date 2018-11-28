```
from pyeoskit import eosapi
```
#eosapi.create_key
创建一个新的密码
```
#在Eos中每个帐户可以拥有有多个key，主要用到的就是owner key和active key.
#创建一个owner key
eosapi.create_key()
#返回值
{
    'public':owner_public_key
    'private':owner_private_key
}
#创建一个active key操作同上
```
#eosapi.create_account
创建一个新的账户
创建账户前，要确定owner key和active key的私钥已经导入钱包，再使用对应的公钥创建账户
```
#需要先导入wallet
#操作前要执行wallet.import_key(wallet_name,private_key)
eosapi.create_account('eosio',account_name,owner_public_key,active_public_key)
```
[更多wallet操作请看这里](https://github.com/learnforpractice/pyeoskit/blob/master/Docs/md/wallet.md)
# eosapi.get_info
请求链的信息
```
eosapi.get_info()
```
# eosapi.get_block
请求块的信息
```
eosapi.get_block(block_num_or_id)
```
#eosapi.get_block_header_state
获取块生产者信息
```
eosapi.get_block_header_state(block_num_or_id)
```
# eosapi.get_account
获取帐户信息
```
eosapi.get_account(account_name)
```

# eosapi.get_abi
获取合约的信息
```
eosapi.get_abi(account_name)
```

#eosapi.get_code
获取智能合约代码
```
eosapi.get_code(account_name)
```

#eosapi.get_raw_code_and_abi
获取智能合约abi
```
eosapi.get_raw_code_and_abi(account_name)
```

#eosapi.get_table_rows
获取智能合约数据信息

取出数据库数据，比如币种余额，合约代码要求存的中间状态等等

其中code是合约账户，scope是合约中设定的（相当于mysql的database），table也是合约中设定的（相当于mysql的table）
```
code="eosio"
scope="eosio"
table=account_name
json="true"
lower_bound=0
upper_bound=4
limit=2

eosapi.get_table_rows(scope,code,table,json,lower_bound,upper_bound,limit)
```

#eosapi.abi_json_to_bin
将json序列化为十六进制

得到的十六进制通常用于push_transaction中的数据字段。
```
code = 'currency'
action = 'transfer'
args = {"from":"initb","to":"initc","quantity":9999}
eosapi.abi_json_to_bin(code,action,args)

#返回值
{
  "binargs": "000000008093dd74000000000094dd74e803000000000000",
  "required_scope": [],
  "required_auth": []
}
```

#eosapi.abi_bin_to_json
将十六进制序列化为json
```
code = 'currency'
action = 'transfer'
binargs = '000000008093dd74000000000094dd74e803000000000000'
eosapi.abi_json_to_bin(code,action,binargs)
```
#eosapi.get_currency_balance
获取账户余额信息（如果没有发布智能合约的话，可能获取不到余额信息）
```
eosapi.get_currency_balance(code='eosio',account=account_name,symbol='SYS')
```

#eosapi.get_required_keys
获取必需的密钥，从密钥列表中签署交易
```

```
# eosapi.gen_transaction
生成一个未签名的transaction
```
reference_block_id = eosapi.get_info().last_irreversible_block_id
eosapi.gen_transaction([['hello', 'sayhello', b'', {'hello':'active'}]], 60, reference_block_id)
```

