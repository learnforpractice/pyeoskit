# Testnet

> Auto-generated documentation for [pysrc.testnet](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / Testnet
    - [Testnet](#testnet)
        - [Testnet().cleanup](#testnetcleanup)
        - [Testnet().create_account](#testnetcreate_account)
        - [Testnet().deploy_contract](#testnetdeploy_contract)
        - [Testnet().deploy_micropython_contract](#testnetdeploy_micropython_contract)
        - [Testnet().init_accounts](#testnetinit_accounts)
        - [Testnet().init_producer](#testnetinit_producer)
        - [Testnet().init_testnet](#testnetinit_testnet)
        - [Testnet().run](#testnetrun)
        - [Testnet().start](#testnetstart)
        - [Testnet().start_nodes](#testnetstart_nodes)
        - [Testnet().stop](#testnetstop)
        - [Testnet().wait](#testnetwait)

## Testnet

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L21)

```python
class Testnet(object):
    def __init__(
        host='127.0.0.1',
        single_node=True,
        show_log=False,
        log_config='',
        extra='',
    ):
```

### Testnet().cleanup

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L212)

```python
def cleanup():
```

### Testnet().create_account

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L283)

```python
def create_account(account, key1, key2):
```

### Testnet().deploy_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L222)

```python
def deploy_contract(account_name, contract_name, contracts_path=None):
```

### Testnet().deploy_micropython_contract

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L251)

```python
def deploy_micropython_contract():
```

### Testnet().init_accounts

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L323)

```python
def init_accounts():
```

### Testnet().init_producer

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L546)

```python
def init_producer():
```

### Testnet().init_testnet

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L319)

```python
def init_testnet():
```

### Testnet().run

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L194)

```python
def run():
```

### Testnet().start

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L191)

```python
def start():
```

### Testnet().start_nodes

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L80)

```python
def start_nodes(wait=False):
```

### Testnet().stop

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L205)

```python
def stop():
```

### Testnet().wait

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/testnet.py#L218)

```python
def wait():
```
