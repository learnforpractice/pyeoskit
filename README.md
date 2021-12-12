Python Toolkit for EOS

# Latest Release

[pyeoskit v1.0.6](https://github.com/learnforpractice/pyeoskit/releases)

# Installation

```bash
python3 -m pip install --upgrade pip
python3 -m pip install pyeoskit
```

On Windows platform:

```bash
python -m pip install --upgrade pip
python -m pip install pyeoskit
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
git clone https://www.github.com/learnforpractice/pyeoskit
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

### Sign With Ledger Hardware Wallet Example
```python
import os
from pyeoskit import eosapi
eosapi.set_node('https://eos.greymass.com')
args = {
    'from': 'test1',
    'to': 'test2',
    'quantity': '1.0000 EOS',
    'memo': 'hello,world'
}

#indexes is an array of ledger signing key indexes
eosapi.push_action('eosio.token', 'transfer', args, {'test1':'active'}, indexes=[0])
```

### License
[MIT](./LICENSE)
