```
from pyeoskit import eosapi
```

# eosapi.gen_transaction
生成一个未签名的transaction
```
reference_block_id = eosapi.get_info().last_irreversible_block_id
eosapi.gen_transaction([['hello', 'sayhello', b'', {'hello':'active'}]], 60, reference_block_id)
```

