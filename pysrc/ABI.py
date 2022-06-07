import json
import logging
from pyeoskit import _pyeoskit

logger=logging.getLogger(__name__)

def set_contract_abi(chain_index, account, abi):
    ret = _pyeoskit.abiserializer_set_contract_abi(chain_index, account, abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return True

def pack_action_args(chain_index, contractName, actionName, args):
    ret = _pyeoskit.abiserializer_pack_action_args(chain_index, contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def unpack_action_args(chain_index, contractName, actionName, args):
    ret = _pyeoskit.abiserializer_unpack_action_args(chain_index, contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def pack_abi_type(chain_index, contractName, actionName, args):
    ret = _pyeoskit.abiserializer_pack_abi_type(chain_index, contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

#args: hex string or bytes
def unpack_abi_type(chain_index, contractName, actionName, args):
    assert isinstance(args, str), 'not a hex string'
    ret = _pyeoskit.abiserializer_unpack_abi_type(chain_index, contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def is_abi_cached(chain_index, contractName):
    return _pyeoskit.abiserializer_is_abi_cached(chain_index, contractName)

def pack_abi(chain_index, abi):
    ret = _pyeoskit.abiserializer_pack_abi(chain_index, abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return bytes.fromhex(ret['data'])

def unpack_abi(chain_index, abi):
    if isinstance(abi, str):
        abi = bytes.fromhex(abi)
    assert isinstance(abi, bytes)

    ret = _pyeoskit.abiserializer_unpack_abi(chain_index, abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

