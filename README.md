Python Toolkit for Eos

# Releases

[v0.3.0 releases](https://github.com/learnforpractice/pyeoskit/releases)

#### Installing Release on macOS

```
python3 -m pip install https://github.com/learnforpractice/pyeoskit/releases/download/v0.3.0/pyeoskit-0.3.0-cp36-cp36m-macosx_10_9_x86_64.whl
```

#### Installing Release on Ubuntu

```
python3 -m pip install https://github.com/learnforpractice/pyeoskit/releases/download/v0.3.0/pyeoskit-0.3.0-cp36-cp36m-linux_x86_64.whl
```

#### Installing Release on Windows

```
python -m pip install https://github.com/learnforpractice/pyeoskit/releases/download/v0.3.0/pyeoskit-0.3.0-cp36-cp36m-win_amd64.whl
```


# Building from Source Code

### Installing Prerequirements(macOS X and linux)

```
python3 -m pip install scikit-build
python3 -m pip install cython==0.28.5
```

### Installing Prerequirements(Windows)

#### Installing Visual Studio
```
https://visualstudio.microsoft.com/zh-hans/thank-you-downloading-visual-studio/?sku=Community&rel=15
```

#### Installing Windows-10-sdk
```
https://developer.microsoft.com/en-us/windows/downloads/windows-10-sdk
```

#### Installing Python

```
https://www.python.org/downloads/
```

#### Installing boost
```
https://sourceforge.net/projects/boost/files/boost-binaries/1.67.0/boost_1_67_0-msvc-14.1-64.exe/download
```

#### Installing Python packages
```
python -m pip install scikit-build
python -m pip install cython==0.28.5
```

### Downloading Source Code

```
git clone https://www.github.com/learnforpractice/pyeoskit
cd pyeoskit
git submodule update --init --recursive
```

### Building on Windows
```
set PATH=%PATH%;"C:\Program Files (x86)\Windows Kits\10\bin\10.0.17763.0\x64"
set LIB=%LIB%;C:\local\boost_1_67_0\lib64-msvc-14.1"
set BOOST_ROOT=C:\local\boost_1_67_0
python setup.py sdist bdist_wheel -G "NMake Makefiles"
```

### Building on macOS
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel --plat-name macosx-10.9-x86_64
```

### Building on Ubuntu
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/clang-fpic.cmake -- -j7
```

### Building on Centos
```
CC=gcc CXX=g++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/gcc-pic.cmake -- -j7
```

### Installation

```
ls dist
python3 -m pip install dist/pyeoskit-[SUFFIX].whl
```

# Tutorials

#### Sneak peek

```python
from pyeoskit import eosapi
from pyeoskit import wallet

mywallet = 'mywallet'
psw = wallet.create(mywallet)
print(psw)
#PW5JwNkkPH7Ji1KfNfKXc4NHYwtEsxAh471YSiUzctwj7kVCD4Bih
```


```python
from pyeoskit import eosapi
from pyeoskit import wallet
psw = 'PW5JwNkkPH7Ji1KfNfKXc4NHYwtEsxAh471YSiUzctwj7kVCD4Bih'
wallet.unlock(mywallet, psw)

#import active key of account hello
wallet.import_key(mywallet, '5JbDP55GXN7MLcNYKCnJtfKi9aD2HvHAdY7g8m67zFTAFkY1uBB')

args = {"from": 'hello',
        "to": 'eosio',
        "quantity": '0.0001 EOS',
        "memo": 'hello,world'
}
eosapi.push_action('eosio.token', 'transfer', args, {'hello':'active'})
```

#### Deploying Contract Example

```python
from pyeoskit import eosapi
from pyeoskit import wallet
import os
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

def apply(receiver, code, action):
    if action == N('sayhello'):
        sayHello()
'''
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
eosapi.set_contract('hello', code, abi, 1)
eosapi.push_action('hello', 'sayhello', b'hello,world', {'hello':'active'})
```

More examples in [Docs](https://github.com/learnforpractice/pyeoskit/tree/master/Docs)


# Acknowledgments
[https://github.com/Netherdrake/py-eos-api](https://github.com/Netherdrake/py-eos-api)

[https://github.com/eosio/eos](https://github.com/eosio/eos)
