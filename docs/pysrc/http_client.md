# HttpClient

> Auto-generated documentation for [pysrc.http_client](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py) module.

- [Pyeoskit](../README.md#pyeoskit-index) / [Modules](../MODULES.md#pyeoskit-modules) / [Pysrc](index.md#pysrc) / HttpClient
    - [HttpClient](#httpclient)
        - [HttpClient().add_node](#httpclientadd_node)
        - [HttpClient().async_exec](#httpclientasync_exec)
        - [HttpClient().get_nodes](#httpclientget_nodes)
        - [HttpClient().hostname](#httpclienthostname)
        - [HttpClient().next_node](#httpclientnext_node)
        - [HttpClient().rpc_request](#httpclientrpc_request)
        - [HttpClient().set_node](#httpclientset_node)
        - [HttpClient().set_nodes](#httpclientset_nodes)
        - [HttpClient().sync_exec](#httpclientsync_exec)

## HttpClient

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L30)

```python
class HttpClient(object):
    def __init__(nodes, _async=False, **kwargs):
```

Http client for handling eosd connections.

This class serves as an abstraction layer for underlying HTTP requests.

#### Arguments

- `nodes` *list* - A list of Eos HTTP RPC nodes to connect to.

- `..` *code-block:* - python

from eosapi.http_client import HttpClient
rpc = HttpClient(['https://eosnode.com'])

any call available to that port can be issued using the instance
via the syntax ``rpc.exec('command', *parameters)``.

### HttpClient().add_node

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L104)

```python
def add_node(url):
```

### HttpClient().async_exec

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L171)

```python
async def async_exec(api, endpoint, body=None):
```

### HttpClient().get_nodes

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L101)

```python
def get_nodes():
```

### HttpClient().hostname

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L119)

```python
@property
def hostname():
```

### HttpClient().next_node

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L108)

```python
def next_node():
```

Switch to the next available node.

This method will change base URL of our requests.
Use it when the current node goes down to change to a fallback node.

### HttpClient().rpc_request

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L123)

```python
def rpc_request(api, endpoint, body=None):
```

### HttpClient().set_node

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L115)

```python
def set_node(node_url):
```

Change current node to provided node URL.

### HttpClient().set_nodes

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L95)

```python
def set_nodes(nodes):
```

### HttpClient().sync_exec

[[find in source code]](https://github.com/learnforpractice/pyeoskit/blob/master/pysrc/http_client.py#L129)

```python
def sync_exec(api, endpoint, body=None):
```

Execute a method against eosd RPC.

#### Warnings

This command will auto-retry in case of node failure, as well as handle
node fail-over, unless we are broadcasting a transaction.
In latter case, the exception is **re-raised**.
