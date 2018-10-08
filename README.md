

```python
from pyeoskit import eosapi
```


```python
eosapi.get_info()
```




    {
        "server_version": "502085b2",
        "chain_id": "cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f",
        "head_block_num": 12209,
        "last_irreversible_block_num": 12208,
        "last_irreversible_block_id": "00002fb0873231d5354f3dbd729e60283aec725a9b8f71bcc037ac76dc98cd02",
        "head_block_id": "00002fb115ef6a212ef2ebfafe33b8e26c21ece57e81d667adf4984e22f1237c",
        "head_block_time": "2018-10-08T00:00:28.500",
        "head_block_producer": "eosio",
        "virtual_block_cpu_limit": 200000000,
        "virtual_block_net_limit": 1048576000,
        "block_cpu_limit": 199900,
        "block_net_limit": 1048576,
        "server_version_string": "pre-release-1.0-101-g502085b21-dirty"
    }




```python
eosapi.get_block(1)
```




    {
        "timestamp": "2018-06-01T12:00:00.000",
        "producer": "",
        "confirmed": 1,
        "previous": "0000000000000000000000000000000000000000000000000000000000000000",
        "transaction_mroot": "0000000000000000000000000000000000000000000000000000000000000000",
        "action_mroot": "cf057bbfb72640471fd910bcb67639c22df9f92470936cddc1ade0e2f2e7dc4f",
        "schedule_version": 0,
        "new_producers": null,
        "header_extensions": [],
        "producer_signature": "SIG_K1_111111111111111111111111111111111111111111111111111111111111111116uk5ne",
        "transactions": [],
        "block_extensions": [],
        "id": "00000001bcf2f448225d099685f14da76803028926af04d2607eafcf609c265c",
        "block_num": 1,
        "ref_block_prefix": 2517196066
    }




```python
info = eosapi.get_info()
eosapi.get_block_header_state(info.last_irreversible_block_num)
```




    {
        "id": "0000305d5a9e223aea1a5ac7ba91d8f3ea2e706e9f8c978fd414889abefcd6b6",
        "block_num": 12381,
        "header": {
            "timestamp": "2018-10-08T00:01:54.500",
            "producer": "eosio",
            "confirmed": 0,
            "previous": "0000305c011c91b47ac75b73e41ece05ece0ad413790275604fed14bc6e1f8fc",
            "transaction_mroot": "0000000000000000000000000000000000000000000000000000000000000000",
            "action_mroot": "e99006973b66c96cec0d506808542a3b066dd02535987822e49e2c1e40ce0928",
            "schedule_version": 0,
            "header_extensions": [],
            "producer_signature": "SIG_K1_KbKiq4JnoJS2Vi26TfTgFFM3jSp8pJdW64qhe5nnTG9NjMSXZKKysd3Mq2BTjYnPdqVgKDdeQJoYX26EmzvAbTcXMb6WbS"
        },
        "dpos_proposed_irreversible_blocknum": 12381,
        "dpos_irreversible_blocknum": 12380,
        "bft_irreversible_blocknum": 0,
        "pending_schedule_lib_num": 0,
        "pending_schedule_hash": "828135c21a947b15cdbf4941ba09e1c9e0a80e88a157b0989e9b476b71a21c6b",
        "pending_schedule": {
            "version": 0,
            "producers": []
        },
        "active_schedule": {
            "version": 0,
            "producers": [
                {
                    "producer_name": "eosio",
                    "block_signing_key": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
                }
            ]
        },
        "blockroot_merkle": {
            "_active_nodes": [
                "02a268b77f4d6d4a0185bcb86b4373bfce568dfcff85b3195fbb4c12002e500d",
                "43ebe9a5570a2274af700859dc1420b1c6ad87cc9b29a5de7be2485c234c9886",
                "4923455dacd3ec0df00cdcc8cf81715768716d816430ab8e4a5da0201ea8429a",
                "dafe25101bb685c22ba812d144fbcd5f7ec49ab429ac46109f4ee083c0c675d6",
                "b1e87599c90273f33f003a5548ee87bc57c8b4cbcedfe5a0be2d0b75006c61ed",
                "1477d6f18bd7218dfdb4e6c13de14d23518adbc28ee45f44793400e9a4890365",
                "8b0ae2e207e7787f10c835e3244b30b54b49863824014950f04b4421b75cca1d"
            ],
            "_node_count": 12380
        },
        "producer_to_last_produced": [
            [
                "eosio",
                12381
            ]
        ],
        "producer_to_last_implied_irb": [
            [
                "eosio",
                12380
            ]
        ],
        "block_signing_key": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
        "confirm_count": [],
        "confirmations": []
    }




```python
eosapi.get_account('hello')
```




    {
        "account_name": "hello",
        "head_block_num": 12453,
        "head_block_time": "2018-10-08T00:02:30.500",
        "privileged": false,
        "last_code_update": "2018-10-07T15:48:57.500",
        "created": "2018-10-07T15:48:57.500",
        "ram_quota": -1,
        "net_weight": -1,
        "cpu_weight": -1,
        "net_limit": {
            "used": -1,
            "available": -1,
            "max": -1
        },
        "cpu_limit": {
            "used": -1,
            "available": -1,
            "max": -1
        },
        "ram_usage": 12359,
        "permissions": [
            {
                "perm_name": "active",
                "parent": "owner",
                "required_auth": {
                    "threshold": 1,
                    "keys": [
                        {
                            "key": "EOS5JuNfuZPATy8oPz9KMZV2asKf9m8fb2bSzftvhW55FKQFakzFL",
                            "weight": 1
                        }
                    ],
                    "accounts": [],
                    "waits": []
                }
            },
            {
                "perm_name": "owner",
                "parent": "",
                "required_auth": {
                    "threshold": 1,
                    "keys": [
                        {
                            "key": "EOS61MgZLN7Frbc2J7giU7JdYjy2TqnfWFjZuLXvpHJoKzWAj7Nst",
                            "weight": 1
                        }
                    ],
                    "accounts": [],
                    "waits": []
                }
            }
        ],
        "total_resources": null,
        "self_delegated_bandwidth": null,
        "refund_request": null,
        "voter_info": null
    }




```python
eosapi.get_code('hello')
```




    {
        "account_name": "hello",
        "code_hash": "66067f4f6ddb3acd43709dc270b7d4956311fb8ddc3f98efb754ba465e63b62e",
        "wast": "",
        "wasm": "630000000000000000000000000200000040000000733c000000640064016c005a00640064026c016d025a026d035a036d045a046d055a0501006403640484005a066405640684005a076407640884005a08640153002909e9000000004e2904da014eda0b726561645f616374696f6eda0b73656e645f696e6c696e65da0f7472616e736665725f696e6c696e6563000000000000000009000000070000004300000073820000007400640183017d007400640283017d01740183007d02740264017c02830201007c007d037c007d047c007d057c007d067403a0047c037c047c057c01a1047d077c0764036b05726c7403a0057c07a1017d08740264047c08830201007403a0067c077c067c02a10301006e127403a0077c047c057c067c017c02a10501006400530029054eda0568656c6c6fda046e616d6572000000007a0668656c6c6f2c290872010000007202000000da057072696e74da026462da0866696e645f693634da076765745f693634da0a7570646174655f693634da0973746f72655f6936342909da016eda0269647206000000da04636f6465da0573636f7065da057461626c65da057061796572da03697472da086f6c645f6e616d65a9007215000000fa0568656c6c6fda0873617948656c6c6f04000000731c00000000010801080206010a010401040104010401100108010a010a01100272170000006300000000000000000100000002000000430000007318000000640164026c006d017d0001007c00a002a10001006400530029034e72000000002901da0667617264656e2903da086261636b796172647218000000da04706c617929017218000000721500000072150000007216000000721a00000016000000730400000000010c01721a000000630300000000000000030000000300000043000000732e0000007c027400640183016b0272147401830001006e167c027400640283016b02722a740264036404830201006400530029054eda0873617968656c6c6f721a000000da05656f73696fe96400000029037201000000721700000072040000002903da087265636569766572720f000000da06616374696f6e721500000072150000007216000000da056170706c791a000000730800000000010c0108010c01722000000029097208000000da06656f736c696272010000007202000000720300000072040000007217000000721a00000072200000007215000000721500000072150000007216000000da083c6d6f64756c653e0100000073080000000801180208120804",
        "abi": {
            "version": "eosio::abi/1.0",
            "types": [],
            "structs": [
                {
                    "name": "message",
                    "base": "",
                    "fields": [
                        {
                            "name": "msg",
                            "type": "string"
                        }
                    ]
                }
            ],
            "actions": [
                {
                    "name": "sayhello",
                    "type": "raw",
                    "ricardian_contract": ""
                }
            ],
            "tables": [],
            "ricardian_clauses": [],
            "error_messages": [],
            "abi_extensions": [],
            "variants": []
        }
    }




```python
 eosapi.get_producer_schedule()
```




    {
        "active": {
            "version": 0,
            "producers": [
                {
                    "producer_name": "eosio",
                    "block_signing_key": "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV"
                }
            ]
        },
        "pending": null,
        "proposed": null
    }




```python
args = {"from": 'eosio',
        "to": 'hello',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}

eosapi.abi_json_to_bin('eosio.token', 'transfer', args)
```




    {
        "binargs": "0000000000ea305500000000001aa36a010000000000000004454f53000000000b68656c6c6f2c776f726c64"
    }




```python
binargs = '0000000000ea305500000000001aa36a010000000000000004454f53000000000b68656c6c6f2c776f726c64'
eosapi.abi_bin_to_json('eosio.token', 'transfer', binargs)
```




    {
        "args": {
            "from": "eosio",
            "to": "hello",
            "quantity": "0.0001 EOS",
            "memo": "hello,world"
        }
    }




```python
from pyeoskit import eosapi
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
eosapi.set_abi('eosio.token', abi)

```


```python


args = {"from": 'eosio',
        "to": 'hello',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}

r = eosapi.pack_args(abi, 'transfer', args)
print(r)
eosapi.unpack_args(abi, 'transfer', r)

```

    b'\x00\x00\x00\x00\x00\xea0U\x00\x00\x00\x00\x00\x1a\xa3j\x01\x00\x00\x00\x00\x00\x00\x00\x04EOS\x00\x00\x00\x00\x0bhello,world'





    {'from': 'eosio',
     'memo': 'hello,world',
     'quantity': '0.0001 EOS',
     'to': 'hello'}




```python
from pyeoskit import eosapi
args = {"from": 'eosio',
        "to": 'hello',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}
action = ['eosio.token', 'transfer', args, {'eosio':'active'}]
reference_block_id = eosapi.get_info().last_irreversible_block_id
r = eosapi.gen_transaction([action], 60*60, reference_block_id)
print(r)
```

    {"expiration":"2018-10-08T07:24:44","ref_block_num":1882,"ref_block_prefix":2758495376,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"eosio","permission":"active"}],"data":"00000000"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}



```python
args = {"from": 'eosio',
        "to": 'hello',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}

r = eosapi.pack_args(abi, 'transfer', args)
print(r)

args = {"from": 'hello',
        "to": 'eosio',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}
action = ['eosio.token', 'transfer', args, {'hello':'active'}]
reference_block_id = eosapi.get_info().last_irreversible_block_id
trx = eosapi.gen_transaction([action], 60, reference_block_id)
print(trx)

info = eosapi.get_info()
trx = eosapi.sign_transaction(trx, '5JbDP55GXN7MLcNYKCnJtfKi9aD2HvHAdY7g8m67zFTAFkY1uBB', info.chain_id)
print(trx)

trx = eosapi.pack_transaction(trx, 0)
print(trx)
eosapi.push_transaction(trx)

```

    b'\x00\x00\x00\x00\x00\xea0U\x00\x00\x00\x00\x00\x1a\xa3j\x01\x00\x00\x00\x00\x00\x00\x00\x04EOS\x00\x00\x00\x00\x0bhello,world'
    {"expiration":"2018-10-08T08:48:37","ref_block_num":17758,"ref_block_prefix":3201477851,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"hello","permission":"active"}],"data":"00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c64"}],"transaction_extensions":[],"signatures":[],"context_free_data":[]}
    {"expiration":"2018-10-08T08:48:37","ref_block_num":17758,"ref_block_prefix":3201477851,"max_net_usage_words":0,"max_cpu_usage_ms":0,"delay_sec":0,"context_free_actions":[],"actions":[{"account":"eosio.token","name":"transfer","authorization":[{"actor":"hello","permission":"active"}],"data":"00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c64"}],"transaction_extensions":[],"signatures":["SIG_K1_KaEThmV6KYAPgdrZZ1CiaSmFGu7cqC7d4FV5LtHkB3wb4eMvoqUFzrSyxpYWnTBbKaQteEFHH5PXmVAYqVGY461VtMpZwm"],"context_free_data":[]}
    {"signatures":["SIG_K1_KaEThmV6KYAPgdrZZ1CiaSmFGu7cqC7d4FV5LtHkB3wb4eMvoqUFzrSyxpYWnTBbKaQteEFHH5PXmVAYqVGY461VtMpZwm"],"compression":"none","packed_context_free_data":"","packed_trx":"e519bb5b5e45dbacd2be000000000100a6823403ea3055000000572d3ccdcd0100000000001aa36a00000000a8ed32322c00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c6400"}





    {
        "transaction_id": "d48cb009f2332edf8340959ad92f3a05ce6daf954d45be7302b607c8b33b7381",
        "processed": {
            "id": "d48cb009f2332edf8340959ad92f3a05ce6daf954d45be7302b607c8b33b7381",
            "block_num": 17760,
            "block_time": "2018-10-08T08:47:38.000",
            "producer_block_id": null,
            "receipt": {
                "status": "executed",
                "cpu_usage_us": 2092,
                "net_usage_words": 17
            },
            "elapsed": 2092,
            "net_usage": 136,
            "scheduled": false,
            "action_traces": [
                {
                    "receipt": {
                        "receiver": "eosio.token",
                        "act_digest": "78a51d36e7ab6541056487422bfc6e9e519a4e99dc35d91633b85233f90ae530",
                        "global_sequence": 17834,
                        "recv_sequence": 20,
                        "auth_sequence": [
                            [
                                "hello",
                                46
                            ]
                        ],
                        "code_sequence": 1,
                        "abi_sequence": 1
                    },
                    "act": {
                        "account": "eosio.token",
                        "name": "transfer",
                        "authorization": [
                            {
                                "actor": "hello",
                                "permission": "active"
                            }
                        ],
                        "data": {
                            "from": "hello",
                            "to": "eosio",
                            "quantity": "0.0001 EOS",
                            "memo": "hello,world"
                        },
                        "hex_data": "00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c64"
                    },
                    "context_free": false,
                    "elapsed": 246,
                    "cpu_usage": 0,
                    "console": "",
                    "total_cpu_usage": 0,
                    "trx_id": "d48cb009f2332edf8340959ad92f3a05ce6daf954d45be7302b607c8b33b7381",
                    "block_num": 17760,
                    "block_time": "2018-10-08T08:47:38.000",
                    "producer_block_id": null,
                    "account_ram_deltas": [],
                    "inline_traces": [
                        {
                            "receipt": {
                                "receiver": "hello",
                                "act_digest": "78a51d36e7ab6541056487422bfc6e9e519a4e99dc35d91633b85233f90ae530",
                                "global_sequence": 17835,
                                "recv_sequence": 19,
                                "auth_sequence": [
                                    [
                                        "hello",
                                        47
                                    ]
                                ],
                                "code_sequence": 1,
                                "abi_sequence": 1
                            },
                            "act": {
                                "account": "eosio.token",
                                "name": "transfer",
                                "authorization": [
                                    {
                                        "actor": "hello",
                                        "permission": "active"
                                    }
                                ],
                                "data": {
                                    "from": "hello",
                                    "to": "eosio",
                                    "quantity": "0.0001 EOS",
                                    "memo": "hello,world"
                                },
                                "hex_data": "00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c64"
                            },
                            "context_free": false,
                            "elapsed": 780,
                            "cpu_usage": 0,
                            "console": "",
                            "total_cpu_usage": 0,
                            "trx_id": "d48cb009f2332edf8340959ad92f3a05ce6daf954d45be7302b607c8b33b7381",
                            "block_num": 17760,
                            "block_time": "2018-10-08T08:47:38.000",
                            "producer_block_id": null,
                            "account_ram_deltas": [],
                            "inline_traces": []
                        },
                        {
                            "receipt": {
                                "receiver": "eosio",
                                "act_digest": "78a51d36e7ab6541056487422bfc6e9e519a4e99dc35d91633b85233f90ae530",
                                "global_sequence": 17836,
                                "recv_sequence": 17797,
                                "auth_sequence": [
                                    [
                                        "hello",
                                        48
                                    ]
                                ],
                                "code_sequence": 1,
                                "abi_sequence": 1
                            },
                            "act": {
                                "account": "eosio.token",
                                "name": "transfer",
                                "authorization": [
                                    {
                                        "actor": "hello",
                                        "permission": "active"
                                    }
                                ],
                                "data": {
                                    "from": "hello",
                                    "to": "eosio",
                                    "quantity": "0.0001 EOS",
                                    "memo": "hello,world"
                                },
                                "hex_data": "00000000001aa36a0000000000ea3055010000000000000004454f53000000000b68656c6c6f2c776f726c64"
                            },
                            "context_free": false,
                            "elapsed": 164,
                            "cpu_usage": 0,
                            "console": "",
                            "total_cpu_usage": 0,
                            "trx_id": "d48cb009f2332edf8340959ad92f3a05ce6daf954d45be7302b607c8b33b7381",
                            "block_num": 17760,
                            "block_time": "2018-10-08T08:47:38.000",
                            "producer_block_id": null,
                            "account_ram_deltas": [],
                            "inline_traces": []
                        }
                    ]
                }
            ],
            "except": null
        }
    }


