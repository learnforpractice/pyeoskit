## Update Authorization Example
```python
from uuoskit import uuosapi
uuosapi.set_node('http://127.0.0.1:8888')

test_account1 = 'helloworld11'
args = {
    "account": test_account1,
    "permission": "active",
    "parent": "owner",
    "auth": {
        "threshold": 1,
        "keys": [
            {
                "key": "EOS6AjF6hvF7GSuSd4sCgfPKq5uWaXvGM2aQtEUCwmEHygQaqxBSV",
                "weight": 1
            },
        ],
        "accounts": [
            {
                "permission":
                {
                    "actor":test_account1,
                    "permission": "eosio.code"
                },
                "weight":1
            }
        ],
        "waits": []
    }
}

return uuosapi.push_action('eosio', 'updateauth', args, {test_account1:'active'})
```
