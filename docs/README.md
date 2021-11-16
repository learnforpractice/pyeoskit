# Pyeoskit Index

> Auto-generated documentation index.

Python Toolkit for EOS

Full Pyeoskit project documentation can be found in [Modules](MODULES.md#pyeoskit-modules)

- [Pyeoskit Index](#pyeoskit-index)
- [Latest Release](#latest-release)
- [Installation](#installation)
- [[Docs](https://learnforpractice.github.io/pyeoskit)](#docshttpslearnforpracticegithubiopyeoskit)
- [Building from Source Code](#building-from-source-code)
        - [Installing Prerequisites](#installing-prerequisites)
        - [Downloading Source Code](#downloading-source-code)
        - [Installation](#installation)
  - [Pyeoskit Modules](MODULES.md#pyeoskit-modules)

# Latest Release

[pyeoskit v1.0.5](https://github.com/learnforpractice/pyeoskit/releases)

# Installation

```bash
pip install pyeoskit
```

# [Docs](https://learnforpractice.github.io/pyeoskit)

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
git clone https://www.github.com/uuosio/pyeoskit
cd pyeoskit
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
python -m pip uninstall pyeoskit -y;python -m pip install .\dist\pyeoskit-[SUFFIX].whl
```

### Example1
```python
import os
from pyeoskit import eosapi, wallet

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

eosapi.set_node('https://eos.greymass.com')
info = eosapi.get_info()
print(info)
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'})
```

### Async Example
```python
import os
import asyncio
from pyeoskit import wallet
from pyeoskit.chainapi import ChainApiAsync

if os.path.exists('mywallet.wallet'):
    os.remove('mywallet.wallet')
psw = wallet.create('mywallet')
#import your account private key here
wallet.import_key('mywallet', '5K463ynhZoCDDa4RDcr63cUwWLTnKqmdcoTKTHBjqoKfv4u5V7p')

async def test():
    eosapi = ChainApiAsync('https://eos.greymass.com')
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
```

### License
[MIT](./LICENSE)
