```
from pyeoskit import wallet
```
# wallet.create
创建一个新的钱包
```
wallet.create('mywallet')
```
如果创建成功会返回钱包的密码字符串，如果创建失败，例如钱包已经存在等原因，则返回空字符串

# wallet.open
如果在创建钱包后程序退出，则在程序再次运行时需要先打开钱包 
```
wallet.open('mywallet')
```
# wallet.unlock
打开钱包后，在需要使用wallet的私钥时，需要先将其unlock
```
psw = 'password return from wallet.create'
wallet.unlock('mywallet', psw)
```
# wallet.lock
锁住钱包,例如
```
wallet.lock('mywallet')
```

# wallet.set_timeout
用于设置钱包wallet.unlock后自动lock的时间，单位为秒，默认为不超时，例如：
```
wallet.set_timeout(60)
```
将在wallet.unlock成功后60秒重新lock钱包

# wallet.save
保存钱包
```
wallet.save('mywallet')
```
# wallet.set_dir
设置钱包所在的目录

# wallet.list_keys
列出所有的公钥/私钥对
```
wallet.list_keys('mywallet', psw)
```
psw为wallet.create时所返回的密码

# wallet.list_wallets()
列出目录下的所有钱包

# wallet.get_public_keys
获取所有已经打开的钱包的公钥
```
wallet.get_public_keys()
```
# wallet.lock_all
锁住所有已经打开的钱包
```
wallet.lock_all()
```

# wallet.import_key
导入私钥
```
wallet.import_key('mywallet', priv_key)
```
# sign_transaction
对transaction进行签名

