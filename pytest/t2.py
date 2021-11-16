import json
from pyeoskit import ABI
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(lineno)d %(module)s %(message)s')
logger=logging.getLogger(__name__)

from pyeoskit import _pyeoskit
_pyeoskit.init()

with open('data/eosio.token.abi', 'rb') as f:
    abi = f.read()
r = ABI.add_contract_abi("hello", abi)
logger.info(r)
transfer = {
    'from': 'helloworld11',
    'to': 'eosio',
    'quantity': '1.0000 EOS',
    'memo': 'transfer 1.0000 EOS from helloworld11 to eosio',
}
transfer = json.dumps(transfer)
logger.info(transfer)

