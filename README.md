Python Toolkit for Eos

# Building & Installation
### Installing Prerequirements
```
python3 -m pip install scikit-build
python3 -m pip install cython
```
### Downloading Source Code

```
git clone https://www.github.com/learnforpractice/pyeoskit
cd pyeoskit
git submodule update --init --recursive
```

### Building on macOS
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel --plat-name macosx-10.9-x86_64
```

### Building on Ubuntu
```
CC=clang CXX=clang++ python3 setup.py sdist bdist_wheel  -- -DCMAKE_TOOLCHAIN_FILE=$(pwd)/cmake/polly/clang-fpic.cmake -- -j7
```

### Installation

```
ls dist
python3 -m pip install dist/pyeoskit-[SUFFIX].whl
```

# Tutorials

Sneak peek

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

More examples in [Docs](https://github.com/learnforpractice/pyeoskit/tree/master/Docs)


# Acknowledgments
[https://github.com/Netherdrake/py-eos-api](https://github.com/Netherdrake/py-eos-api)

[https://github.com/eosio/eos](https://github.com/eosio/eos)
