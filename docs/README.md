# Uuoskit Index

> Auto-generated documentation index.

Python Toolkit for EOSIO

Full Uuoskit project documentation can be found in [Modules](MODULES.md#uuoskit-modules)

- [Uuoskit Index](#uuoskit-index)
- [Latest Release](#latest-release)
- [Building from Source Code](#building-from-source-code)
    - [Installing Prerequirements(macOS X and linux)](#installing-prerequirementsmacos-x-and-linux)
    - [Downloading Source Code](#downloading-source-code)
    - [Building on macOS](#building-on-macos)
    - [Building on Ubuntu](#building-on-ubuntu)
    - [Building on Centos](#building-on-centos)
    - [Installation](#installation)
    - [Example1](#example1)
    - [Async Example](#async-example)
- [wallet module](#wallet-module)
- [ChainNative class](#chainnative-class)
- [ChainApiSync class](#chainapisync-class)
- [ChainApiAsync class](#chainapiasync-class)
- [Client class](#client-class)
    - [License](#license)

<h3>
  <a
    target="_blank"
    href="https://mybinder.org/v2/gh/uuosio/UUOSKit/master?filepath=notebooks%2Fhelloworld.ipynb"
  >
    Quick Start
    <img alt="Binder" valign="bottom" height="25px"
    src="https://mybinder.org/badge_logo.svg"
    />
  </a>
</h3>

# Latest Release

[uuoskit v0.8.3](https://github.com/uuosio/uuoskit/releases)

# Building from Source Code

### Installing Prerequirements(macOS X and linux)

```
python3 -m pip install scikit-build
python3 -m pip install cython==0.28.5
```

### Downloading Source Code

```
git clone https://www.github.com/uuosio/uuoskit
cd uuoskit
git submodule update --init --recursive
```

### Building on macOS
```
./build-mac.sh
```

### Building on Ubuntu
```
./build-linux.sh
```

### Building on Centos
```
CC=gcc CXX=g++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/gcc-pic.cmake -- -j7
```

### Installation

```
ls dist
python3 -m pip install dist/uuoskit-[SUFFIX].whl
```

### Example1
```python
import os
from uuoskit import uuosapi, wallet

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

uuosapi.set_node('https://eos.greymass.com')
info = uuosapi.get_info()
print(info)
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}
uuosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
```

### Async Example
```python
import os
import asyncio
from uuoskit import wallet
from uuoskit.chainapi import ChainApiAsync

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

async def test():
    uuosapi = ChainApiAsync('https://eos.greymass.com')
    info = await uuosapi.get_info()
    print(info)
    args = {
        'from': 'test1',
        'to': 'test2',
        'quantity': '1.0000 EOS',
        'memo': 'hello,world'
    }
    r = await uuosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
    print(r)

asyncio.run(test())
```

# [wallet module](pysrc/chainapi_sync.md)

# [ChainNative class](pysrc/chainnative.md)

# [ChainApiSync class](pysrc/chainapi_sync.md)

# [ChainApiAsync class](pysrc/chainapi_async.md)

# [Client class](pysrc/client.md)

### License
[MIT](./LICENSE)
