#!/usr/bin/env python
"""
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
"""

import binascii
import json
import struct
from eosBase import Transaction, parse_bip32_path
from ledgerblue.comm import getDongle
import argparse
import base58
import hashlib
from pyeoskit import eosapi

eosapi.set_node('http://207.148.89.244:8888')
args = {
    'from': 'a',
    'to': 'b',
    'quantity': '1.0000 EOS',
    'memo': 'hello'
}

action = ['eosio.token', 'transfer', args, {'a': 'active'}]
chain_id = 'aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906'
ref_block = '0d1ddb902aa3a5dc16d88f9da8477a2bfbb1efa85b0706a4453cad5736c71fcb'
tx = eosapi.gen_transaction([action], 60*3, ref_block, chain_id)

parser = argparse.ArgumentParser()
parser.add_argument('--path', help="BIP 32 path to retrieve")
parser.add_argument('--file', help="Transaction in JSON format")
args = parser.parse_args()

if args.path is None:
    args.path = "44'/194'/0'/0/0"

if args.file is None:
    args.file = 'transaction.json'

donglePath = parse_bip32_path(args.path)
pathSize = len(donglePath) // 4

with open(args.file) as f:
    obj = json.load(f)
    tx = json.loads(tx)
    print(json.dumps(tx, indent=4))
    obj = {
        "chain_id": chain_id,
        "transaction": tx
    }
    tx = Transaction.parse(obj)
    tx_chunks = tx.encode2()

    first = True
    dongle = getDongle(True)
    for tx_chunk in tx_chunks:

        offset = 0
        singSize = len(tx_chunk)
        sliceSize = 150
        while offset != singSize:
            if singSize - offset > sliceSize:
                transport_chunk = tx_chunk[offset: offset + sliceSize]
            else:
                transport_chunk = tx_chunk[offset:]

            if first:
                totalSize = len(donglePath) + 1 + len(transport_chunk)
                apdu = bytearray.fromhex("D4040000") + bytes([totalSize, pathSize]) + donglePath + transport_chunk
                first = False
            else:
                totalSize = len(transport_chunk)
                apdu = bytearray.fromhex("D4048000") + bytes([totalSize]) + transport_chunk

            offset += len(transport_chunk)
            result = dongle.exchange(bytes(apdu))
            print('+++++++result:', binascii.hexlify(result))

            h = hashlib.new('ripemd160')
            h.update(result)
            result += h.digest()[:4]
            result = 'SIG_K1_' + base58.b58encode(result).encode()
            print(result)
