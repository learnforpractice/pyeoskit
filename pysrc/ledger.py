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
import argparse
import base58
import hashlib

from .eosBase import Transaction, parse_bip32_path
from ledgerblue.comm import getDongle

dongle = None
def get_dongle():
    global dongle
    if dongle is None:
        dongle = getDongle(True)
    return dongle

def close_dongle():
    global dongle
    if not dongle:
        return
    dongle.close()
    dongle = None

def sign_by_index(obj, index):
    donglePath = parse_bip32_path(f"44'/194'/0'/0/{index}")
    pathSize = len(donglePath) // 4

    tx = Transaction.parse(obj)
    tx_chunks = tx.encode2()
    first = True
    dongle = get_dongle()
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
            if not result:
                continue
            h = hashlib.new('ripemd160')
            h.update(result + b'K1')
            result += h.digest()[:4]
            result = 'SIG_K1_' + base58.b58encode(result).decode()
            return result

def sign(tx, indexes, chain_id):
    if isinstance(tx, str):
        tx = json.loads(tx)
    #TODO: verify public keys with indexes
    obj = {
        "chain_id": chain_id,
        "transaction": tx
    }
    signatures = []
    for index in indexes:
        signature = sign_by_index(obj, index)
        signatures.append(signature)
    signatures.sort()
    return signatures

def get_public_keys(indexes):
    public_keys = []
    for index in indexes:
        public_key = get_public_key(index)
        public_keys.append(public_key)
    return public_keys

def get_public_key(index):
    donglePath = parse_bip32_path(f"44'/194'/0'/0/{index}")
    apdu = bytearray.fromhex("D4020001") + bytes([len(donglePath) + 1, len(donglePath) // 4]) + donglePath

    dongle = get_dongle()
    result = dongle.exchange(bytes(apdu))
    offset = 1 + result[0]
    address = result[offset + 1: offset + 1 + result[offset]]

    public_key = result[1: 1 + result[0]]
    head = 0x03 if (public_key[64] & 0x01) == 1 else 0x02
    public_key_compressed = bytearray([head]) + public_key[1:33]

    ripemd = hashlib.new('ripemd160')
    ripemd.update(public_key_compressed)
    check = ripemd.digest()[:4]

    buff = public_key_compressed + check
    pub1 = "EOS" + base58.b58encode(buff).decode()
    pub2 = address.decode()
    assert pub1 == pub2
    return pub1
