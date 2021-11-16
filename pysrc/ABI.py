import json
import logging
from pyeoskit import _pyeoskit

logger=logging.getLogger(__name__)

def set_contract_abi(account, abi):
    ret = _pyeoskit.abiserializer_set_contract_abi(account, abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return True

def pack_action_args(contractName, actionName, args):
    ret = _pyeoskit.abiserializer_pack_action_args(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def unpack_action_args(contractName, actionName, args):
    ret = _pyeoskit.abiserializer_unpack_action_args(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def pack_abi_type(contractName, actionName, args):
    ret = _pyeoskit.abiserializer_pack_abi_type(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def unpack_abi_type(contractName, actionName, args):
    ret = _pyeoskit.abiserializer_unpack_abi_type(contractName, actionName, args)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

def is_abi_cached(contractName):
    return _pyeoskit.abiserializer_is_abi_cached(contractName)

def pack_abi(abi):
    ret = _pyeoskit.abiserializer_pack_abi(abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return bytes.fromhex(ret['data'])

def unpack_abi(abi):
    if isinstance(abi, str):
        abi = bytes.fromhex(abi)
    assert isinstance(abi, bytes)

    ret = _pyeoskit.abiserializer_unpack_abi(abi)
    ret = json.loads(ret)
    if 'error' in ret:
        raise Exception(ret['error'])
    return ret['data']

