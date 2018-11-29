```
from pyeoskit import eosapi
```
# eosapi.create_key

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
# eosapi.create_account

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
# eosapi.get_block_header_state

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

# eosapi.get_code

获取智能合约代码
```
eosapi.get_code(account_name)
```

# eosapi.get_raw_code_and_abi

获取智能合约abi
```
eosapi.get_raw_code_and_abi(account_name)
```

# eosapi.get_table_rows

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

# eosapi.abi_json_to_bin

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

# eosapi.abi_bin_to_json

将十六进制序列化为json
```
code = 'currency'
action = 'transfer'
binargs = '000000008093dd74000000000094dd74e803000000000000'
eosapi.abi_json_to_bin(code,action,binargs)
```
# eosapi.get_currency_balance

获取账户余额信息（如果没有发布智能合约的话，可能获取不到余额信息）
```
eosapi.get_currency_balance(code='eosio',account=account_name,symbol='SYS')
```

# eosapi.get_required_keys

获取必需的密钥，从密钥列表中签署交易
```
available_keys=[
    "EOS5ySgzeHp9G7TqNDGpyzaCtahAeRcTvPRPJbFey5CmySL3vKYgE",
    "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
    "EOS6gXwNz2SKUNAZcyjzVvg6KdNgA1bSuVzCr8c5yWkGij52JKx8V"
    ]
    
transaction={
        "actions": [
            {
                "account": "eosio.token",
                "authorization": [
                    {
                        "actor": "eosio",
                        "permission": "active"
                    }
                ],
                "data": "0000000000ea305500000000487a2b9d102700000000000004454f53000000001163726561746564206279206e6f70726f6d",
                "name": "transfer"
            }
        ],
        "context_free_actions": [
        ],
        "context_free_data": [
        ],
        "delay_sec": 0,
        "expiration": "2018-11-28T17:20:30.500",
        "max_kcpu_usage": 0,
        "max_net_usage_words": 0,
        "ref_block_num": 245107,
        "ref_block_prefix": 801303063,
        "signatures": [
        ]
    }
}

eosapi.get_required_keys(available_keys,transaction)

#返回值
{
    "required_keys": [
        "EOS6gXwNz2SKUNAZcyjzVvg6KdNgA1bSuVzCr8c5yWkGij52JKx8V"
    ]
}

```

# eosapi.get_currency_stats
获取某代币的信息
```
eosapi.get_currency_stats(code='eosio',accountname='your account',symbol='SYS')
```

# eosapi.get_producers
获取产块节点
```
eosapi.get_producers(json,lower_bound)
```

# eosapi.push_block
产生块
```
eosapi.push_block(block)
```

# eosapi.push_transaction
发送交易,此方法预期采用JSON格式的事务，并将尝试将其应用于区块链。
```
signed_transaction={
    "ref_block_num":"101",
    "ref_block_prefix":"4159312339",
    "expiration":"2017-09-25T06:28:49",
    "scope":["initb","initc"],
    "actions":[{
        "code":"currency",
        "type":"transfer",
        "recipients":["initb","initc"],
        "authorization":[{
            "account":"initb","permission":"active"
            }],
        "data":"000000000041934b000000008041934be803000000000000"
        }],
    "signatures":[],"authorizations":[]
    }

eosapi.push_transaction(sign_transaction)
```

# eosapi.push_transactions
该方法一次推送多个事务,实现同时多次交易。
```
操作同eosapi.push_transaction
```

# eosapi.get_actions
获取账户的Actions列表

pos和offset是指：从第pos条记录开始获取offset条Actions
```
eosapi.get_actions(account_name,pos,offset)
```

# eosapi.get_transaction
获取transaction交易细节
```
eosapi.get_transaction(id)
```

# eosapi.get_key_accounts
获取公钥对应的账户
```
eosapi.get_key_accounts(public_key)
```


# eosapi.gen_transaction
生成一个未签名的transaction
```
reference_block_id = eosapi.get_info().last_irreversible_block_id
eosapi.gen_transaction([['hello', 'sayhello', b'', {'hello':'active'}]], 60, reference_block_id)
```

