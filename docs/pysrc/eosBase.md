# Eosbase

> Auto-generated documentation for [pysrc.eosBase](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py) module.

/*******************************************************************************
*   Taras Shchybovyk
*   (c) 2018 Taras Shchybovyk
*
*  Licensed under the Apache License, Version 2.0 (the "License");
*  you may not use this file except in compliance with the License.
*  You may obtain a copy of the License at
*
*      http://www.apache.org/licenses/LICENSE-2.0
*
*  Unless required by applicable law or agreed to in writing, software
*  distributed under the License is distributed on an "AS IS" BASIS,
*  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
*  See the License for the specific language governing permissions and
*  limitations under the License.
********************************************************************************/

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Eosbase
    - [Action](#action)
    - [Transaction](#transaction)
        - [Transaction.asset_to_number](#transactionasset_to_number)
        - [Transaction.char_to_symbol](#transactionchar_to_symbol)
        - [Transaction().encode](#transactionencode)
        - [Transaction().encode2](#transactionencode2)
        - [Transaction.name_to_number](#transactionname_to_number)
        - [Transaction.pack_fc_uint](#transactionpack_fc_uint)
        - [Transaction.parse](#transactionparse)
        - [Transaction.parse_auth](#transactionparse_auth)
        - [Transaction.parse_buy_ram](#transactionparse_buy_ram)
        - [Transaction.parse_buy_rambytes](#transactionparse_buy_rambytes)
        - [Transaction.parse_delegate](#transactionparse_delegate)
        - [Transaction.parse_delete_auth](#transactionparse_delete_auth)
        - [Transaction.parse_link_auth](#transactionparse_link_auth)
        - [Transaction.parse_newaccount](#transactionparse_newaccount)
        - [Transaction.parse_public_key](#transactionparse_public_key)
        - [Transaction.parse_refund](#transactionparse_refund)
        - [Transaction.parse_sell_ram](#transactionparse_sell_ram)
        - [Transaction.parse_transfer](#transactionparse_transfer)
        - [Transaction.parse_unknown](#transactionparse_unknown)
        - [Transaction.parse_unlink_auth](#transactionparse_unlink_auth)
        - [Transaction.parse_update_auth](#transactionparse_update_auth)
        - [Transaction.parse_vote_producer](#transactionparse_vote_producer)
        - [Transaction.symbol_from_string](#transactionsymbol_from_string)
        - [Transaction.symbol_precision](#transactionsymbol_precision)
        - [Transaction.unpack_fc_uint](#transactionunpack_fc_uint)
    - [parse_bip32_path](#parse_bip32_path)

## Action

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L45)

```python
class Action():
    def __init__():
```

## Transaction

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L50)

```python
class Transaction():
    def __init__():
```

### Transaction.asset_to_number

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L96)

```python
@staticmethod
def asset_to_number(asset):
```

### Transaction.char_to_symbol

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L54)

```python
@staticmethod
def char_to_symbol(c):
```

### Transaction().encode

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L367)

```python
def encode():
```

### Transaction().encode2

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L437)

```python
def encode2():
```

### Transaction.name_to_number

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L62)

```python
@staticmethod
def name_to_number(name):
```

### Transaction.pack_fc_uint

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L139)

```python
@staticmethod
def pack_fc_uint(value):
```

### Transaction.parse

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L289)

```python
@staticmethod
def parse(json):
```

### Transaction.parse_auth

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L213)

```python
@staticmethod
def parse_auth(data):
```

### Transaction.parse_buy_ram

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L184)

```python
@staticmethod
def parse_buy_ram(data):
```

### Transaction.parse_buy_rambytes

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L191)

```python
@staticmethod
def parse_buy_rambytes(data):
```

### Transaction.parse_delegate

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L273)

```python
@staticmethod
def parse_delegate(data):
```

### Transaction.parse_delete_auth

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L240)

```python
@staticmethod
def parse_delete_auth(data):
```

### Transaction.parse_link_auth

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L250)

```python
@staticmethod
def parse_link_auth(data):
```

### Transaction.parse_newaccount

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L265)

```python
@staticmethod
def parse_newaccount(data):
```

### Transaction.parse_public_key

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L204)

```python
@staticmethod
def parse_public_key(data):
```

### Transaction.parse_refund

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L246)

```python
@staticmethod
def parse_refund(data):
```

### Transaction.parse_sell_ram

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L198)

```python
@staticmethod
def parse_sell_ram(data):
```

### Transaction.parse_transfer

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L126)

```python
@staticmethod
def parse_transfer(data):
```

### Transaction.parse_unknown

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L282)

```python
@staticmethod
def parse_unknown(data):
```

### Transaction.parse_unlink_auth

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L258)

```python
@staticmethod
def parse_unlink_auth(data):
```

### Transaction.parse_update_auth

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L232)

```python
@staticmethod
def parse_update_auth(data):
```

### Transaction.parse_vote_producer

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L174)

```python
@staticmethod
def parse_vote_producer(data):
```

### Transaction.symbol_from_string

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L82)

```python
@staticmethod
def symbol_from_string(p, name):
```

### Transaction.symbol_precision

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L92)

```python
@staticmethod
def symbol_precision(sym):
```

### Transaction.unpack_fc_uint

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L154)

```python
@staticmethod
def unpack_fc_uint(buffer):
```

## parse_bip32_path

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/eosBase.py#L32)

```python
def parse_bip32_path(path):
```
