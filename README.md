Python Toolkit for EOSIO

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

[uuoskit v1.0.1](https://github.com/uuosio/uuoskit/releases)

# Installation

```bash
pip install uuoskit
```

# [Docs](https://uuosio.github.io/UUOSKit)

# Building from Source Code

### Installing Prerequisites

```
python3 -m pip install scikit-build
python3 -m pip install cython
```

For Windows platform

```
python -m pip install scikit-build
python -m pip install cython
```

1. Download and Install gcc compiler from [tdm-gcc](https://jmeubank.github.io/tdm-gcc)
2. Install Go compiler from [download](https://golang.org/doc/install#download)
3. Install cmake from [download](https://cmake.org/download)
4. Install python3 from [downloads](https://www.python.org/downloads/windows/)

Press Win+R to open Run Dialog, input the following command
```
cmd -k /path/to/gcc/mingwvars.bat
```

### Downloading Source Code

```
git clone https://www.github.com/uuosio/uuoskit
cd uuoskit
git submodule update --init --recursive
```

### Build
```
./build.sh
```

For Windows platform
In the cmd dialog, enter the following command:
```
python setup.py sdist bdist_wheel
```

### Installation

```
./install.sh
```

For Windows platform
```
python -m pip uninstall uuoskit -y;python -m pip install .\dist\uuoskit-[SUFFIX].whl
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

### License
[MIT](./LICENSE)
