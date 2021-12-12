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
from __future__ import print_function
import io
from asn1 import Encoder, Numbers
from datetime import datetime
import struct
import binascii
from base58 import b58decode 
import hashlib

import sys
sys.dont_write_bytecode = True

def parse_bip32_path(path):
    if len(path) == 0:
        return b""
    result = b""
    elements = path.split('/')
    for pathElement in elements:
        element = pathElement.split('\'')
        if len(element) == 1:
            result = result + struct.pack(">I", int(element[0]))
        else:
            result = result + struct.pack(">I", 0x80000000 | int(element[0]))
    return result

class Action:
    def __init__(self):
        pass


class Transaction:
    def __init__(self):
        pass

    @staticmethod
    def char_to_symbol(c):
        if c >= 'a' and c <= 'z':
            return ord(c) - ord('a') + 6
        if c >= '1' and c <= '5':
            return ord(c) - ord('1') + 1
        return 0

    @staticmethod
    def name_to_number(name):
        length = len(name)
        value = 0

        for i in range(0, 13):
            c = 0
            if i < length and i < 13:
                c = Transaction.char_to_symbol(name[i])

            if i < 12:
                c &= 0x1f
                c <<= 64 - 5 * (i + 1)
            else:
                c &= 0x0f

            value |= c

        return struct.pack('Q', value)

    @staticmethod
    def symbol_from_string(p, name):
        length = len(name)
        result = 0
        for i in range(0, length):
            result |= ord(name[i]) << (8 *(i+1))

        result |= p
        return result

    @staticmethod
    def symbol_precision(sym):
        return pow(10, (sym & 0xff))

    @staticmethod
    def asset_to_number(asset):
        amount_str, symol_str = asset.split(' ')
        dot_pos = amount_str.find('.')

        # parse symbol
        if dot_pos != -1:
            precision_digit = len(amount_str) - dot_pos - 1
        else:
            precision_digit = 0

        sym = Transaction.symbol_from_string(precision_digit, symol_str)

        # parse amount
        if dot_pos != -1:
            int_part = int(amount_str[:dot_pos])
            fract_part = int(amount_str[dot_pos+1:])
            if int_part < 0:
                fract_part *= -1
        else:
            int_part = int(amount_str)

        amount = int_part
        amount *= Transaction.symbol_precision(sym)
        amount += fract_part

        data = struct.pack('Q', amount)
        data += struct.pack('Q', sym)
        return data

    @staticmethod
    def parse_transfer(data):
        parameters = Transaction.name_to_number(data['from'])
        parameters += Transaction.name_to_number(data['to'])
        parameters += Transaction.asset_to_number(data['quantity'])
        memo = data['memo']
        parameters += Transaction.pack_fc_uint(len(memo))
        if len(memo) > 0:
            length = '{}s'.format(len(memo))
            parameters += struct.pack(length, data['memo'].encode())

        return parameters

    @staticmethod
    def pack_fc_uint(value):
        out = b''
        val = value
        while True:
            b = val & 0x7f
            val >>= 7
            b |= ((val > 0) << 7)
            out += b.to_bytes(1, 'little')

            if val == 0:
                break

        return out

    @staticmethod
    def unpack_fc_uint(buffer):
        i = 0
        v = 0
        b = 0
        by = 0

        k = 0
        while True:
            b = buffer[k]
            k += 1
            i += 1
            v |= (b & 0x7f) << by
            by += 7

            if (b & 0x80) == 0 or by >= 32:
                break

        return v

    @staticmethod
    def parse_vote_producer(data):
        parameters = Transaction.name_to_number(data['account'])
        parameters += Transaction.name_to_number(data['proxy'])
        parameters += Transaction.pack_fc_uint(len(data['producers']))
        for producer in data['producers']:
            parameters += Transaction.name_to_number(producer)

        return parameters

    @staticmethod
    def parse_buy_ram(data):
        parameters = Transaction.name_to_number(data['buyer'])
        parameters += Transaction.name_to_number(data['receiver'])
        parameters += Transaction.asset_to_number(data['tokens'])
        return parameters

    @staticmethod
    def parse_buy_rambytes(data):
        parameters = Transaction.name_to_number(data['buyer'])
        parameters += Transaction.name_to_number(data['receiver'])
        parameters += struct.pack('I', data['bytes'])
        return parameters

    @staticmethod
    def parse_sell_ram(data):
        parameters = Transaction.name_to_number(data['receiver'])
        parameters += struct.pack('Q', data['bytes'])
        return parameters

    @staticmethod
    def parse_public_key(data):
        data = str(data[3:])
        decoded = b58decode(data)
        decoded = decoded[:-4]
        parameters = struct.pack('B', 0)
        parameters += decoded
        return parameters

    @staticmethod
    def parse_auth(data):
        parameters = struct.pack('I', data['threshold'])
        key_number = len(data['keys'])
        parameters += struct.pack('B', key_number)
        for key in data['keys']:
            parameters += Transaction.parse_public_key(key['key'])
            parameters += struct.pack('H', key['weight'])
        parameters += struct.pack('B', len(data['accounts']))
        for account in data['accounts']:
            parameters += Transaction.name_to_number(account['authorization']['actor'])
            parameters += Transaction.name_to_number(account['authorization']['permission'])
            parameters += struct.pack('H', account['weight'])
        parameters += struct.pack('B', len(data['waits']))
        for wait in data['waits']:
            parameters += struct.pack('I', wait['wait'])
            parameters += struct.pack('H', wait['weight'])
        return parameters
    
    @staticmethod
    def parse_update_auth(data):
        parameters = Transaction.name_to_number(data['account'])
        parameters += Transaction.name_to_number(data['permission'])
        parameters += Transaction.name_to_number(data['parent'])
        parameters += Transaction.parse_auth(data['auth'])
        return parameters

    @staticmethod
    def parse_delete_auth(data):
        parameters = Transaction.name_to_number(data['account'])
        parameters += Transaction.name_to_number(data['permission'])
        return parameters

    @staticmethod
    def parse_refund(data):
        return Transaction.name_to_number(data['account'])

    @staticmethod
    def parse_link_auth(data):
        parameters = Transaction.name_to_number(data['account'])
        parameters += Transaction.name_to_number(data['contract'])
        parameters += Transaction.name_to_number(data['action'])
        parameters += Transaction.name_to_number(data['permission'])
        return parameters

    @staticmethod
    def parse_unlink_auth(data):
        parameters = Transaction.name_to_number(data['account'])
        parameters += Transaction.name_to_number(data['contract'])
        parameters += Transaction.name_to_number(data['action'])
        return parameters

    @staticmethod
    def parse_newaccount(data):
        parameters = Transaction.name_to_number(data['creator'])
        parameters += Transaction.name_to_number(data['newact'])
        parameters += Transaction.parse_auth(data['owner'])
        parameters += Transaction.parse_auth(data['active'])
        return parameters

    @staticmethod
    def parse_delegate(data):
        parameters = Transaction.name_to_number(data['from'])
        parameters += Transaction.name_to_number(data['to'])
        parameters += Transaction.asset_to_number(data['stake_net_quantity'])
        parameters += Transaction.asset_to_number(data['stake_cpu_quantity'])
        parameters += bytes([0x01]) if data['transfer'] else bytes([0x00])
        return parameters

    @staticmethod
    def parse_unknown(data):
        data = data * 1000
        length = '{}s'.format(len(data))
        parameters = struct.pack(length, data.encode())
        return parameters

    @staticmethod
    def parse(json):
        tx = Transaction()
        tx.json = json

        tx.chain_id = binascii.unhexlify(json['chain_id'])

        body = json['transaction']

#        expiration = int(datetime.strptime(body['expiration'], '%Y-%m-%dT%H:%M:%S').strftime("%s"))
        delta = datetime.strptime(body['expiration'], '%Y-%m-%dT%H:%M:%S') - datetime(1970, 1, 1)
        expiration = int(delta.total_seconds())
        tx.expiration = struct.pack('I', expiration)
        tx.ref_block_num = struct.pack('H', body['ref_block_num'])
        tx.ref_block_prefix = struct.pack('I', body['ref_block_prefix'])
        tx.net_usage_words = struct.pack('B', body['max_net_usage_words'])
        tx.max_cpu_usage_ms = struct.pack('B', body['max_cpu_usage_ms'])
        tx.delay_sec = struct.pack('B', body['delay_sec'])

        tx.ctx_free_actions_size = struct.pack('B', len(body['context_free_actions']))
        tx.actions_size = struct.pack('B', len(body['actions']))

        tx.actions = []
        for action in body['actions']:
            act = Action()
            act.account = Transaction.name_to_number(action['account'])
            act.name = Transaction.name_to_number(action['name'])

            act.auth_size = struct.pack('B', len(action['authorization']))
            act.auth = []
            for auth in action['authorization']:
                act.auth.append((Transaction.name_to_number(auth['actor']), Transaction.name_to_number(auth['permission'])))

            data = action['data']
            if isinstance(data, str):
                parameters = bytes.fromhex(data)
            elif action['name'] == 'transfer':
                parameters = Transaction.parse_transfer(data)
            elif action['name'] == 'voteproducer':
                parameters = Transaction.parse_vote_producer(data)
            elif action['name'] == 'buyram':
                parameters = Transaction.parse_buy_ram(data)
            elif action['name'] == 'buyrambytes':
                parameters = Transaction.parse_buy_rambytes(data)
            elif action['name'] == 'sellram':
                parameters = Transaction.parse_sell_ram(data)
            elif action['name'] == 'updateauth':
                parameters = Transaction.parse_update_auth(data)
            elif action['name'] == 'deleteauth':
                parameters = Transaction.parse_delete_auth(data)
            elif action['name'] == 'refund':
                parameters = Transaction.parse_refund(data)
            elif action['name'] == 'linkauth':
                parameters = Transaction.parse_link_auth(data)
            elif action['name'] == 'unlinkauth':
                parameters = Transaction.parse_unlink_auth(data)
            elif action['name'] == 'newaccount':
                parameters = Transaction.parse_newaccount(data)
            elif action['name'] == 'delegatebw':
                parameters = Transaction.parse_delegate(data)
            else:
                parameters = Transaction.parse_unknown(data)

            act.data_size = Transaction.pack_fc_uint(len(parameters))
            act.data = parameters

            tx.actions.append(act)

        tx.tx_ext = struct.pack('B', len(body['transaction_extensions']))
        tx.cfd = binascii.unhexlify('00' * 32)

        for action in tx.actions:
            sha = hashlib.sha256()
            sha.update(action.data_size)
            sha.update(action.data)

        return tx

    def encode(self):
        encoder = Encoder()
        sha = hashlib.sha256()
        buffer = io.BytesIO()
        buffer.write(self.chain_id)
        buffer.write(self.expiration)
        buffer.write(self.ref_block_num)
        buffer.write(self.ref_block_prefix)
        buffer.write(self.net_usage_words)
        buffer.write(self.max_cpu_usage_ms)
        buffer.write(self.delay_sec)
        buffer.write(self.ctx_free_actions_size)
        buffer.write(self.actions_size)
        for action in self.actions:
            buffer.write(action.account)
            buffer.write(action.name)
            buffer.write(action.auth_size)
            for auth in action.auth:
                (auth_actor, permission) = auth
                buffer.write(auth_actor)
                buffer.write(permission)

            buffer.write(action.data_size)
            buffer.write(action.data)
        buffer.write(self.tx_ext)
        buffer.write(self.cfd)
        sha.update(buffer.getvalue())
        print('Signing digest ' + sha.hexdigest())

        chunks = []

        encoder.start()
        encoder.write(self.chain_id, Numbers.OctetString)
        encoder.write(self.expiration, Numbers.OctetString)
        encoder.write(self.ref_block_num, Numbers.OctetString)
        encoder.write(self.ref_block_prefix, Numbers.OctetString)
        encoder.write(self.net_usage_words, Numbers.OctetString)
        encoder.write(self.max_cpu_usage_ms, Numbers.OctetString)
        encoder.write(self.delay_sec, Numbers.OctetString)

        encoder.write(self.ctx_free_actions_size, Numbers.OctetString)
        encoder.write(self.actions_size, Numbers.OctetString)

        chunks.append(encoder.output())

        for action in self.actions:
            encoder.start()

            encoder.write(action.account, Numbers.OctetString)
            encoder.write(action.name, Numbers.OctetString)
            encoder.write(action.auth_size, Numbers.OctetString)
            for auth in action.auth:
                (auth_actor, permission) = auth
                encoder.write(auth_actor, Numbers.OctetString)
                encoder.write(permission, Numbers.OctetString)
            encoder.write(action.data_size, Numbers.OctetString)
            encoder.write(action.data, Numbers.OctetString)

            chunks.append(encoder.output())

        encoder.start()

        encoder.write(self.tx_ext, Numbers.OctetString)
        encoder.write(self.cfd, Numbers.OctetString)

        chunks.append(encoder.output())

        return chunks


    def encode2(self):
        encoder = Encoder()
        sha = hashlib.sha256()
        buffer = io.BytesIO()
        buffer.write(self.chain_id)
        buffer.write(self.expiration)
        buffer.write(self.ref_block_num)
        buffer.write(self.ref_block_prefix)
        buffer.write(self.net_usage_words)
        buffer.write(self.max_cpu_usage_ms)
        buffer.write(self.delay_sec)
        buffer.write(self.ctx_free_actions_size)
        buffer.write(self.actions_size)
        for action in self.actions:
            buffer.write(action.account)
            buffer.write(action.name)
            buffer.write(action.auth_size)
            for auth in action.auth:
                (auth_actor, permission) = auth
                buffer.write(auth_actor)
                buffer.write(permission)

            buffer.write(action.data_size)
            buffer.write(action.data)
        buffer.write(self.tx_ext)
        buffer.write(self.cfd)

        value = buffer.getvalue()
        sha.update(value)
        print('Signing digest ' + sha.hexdigest())

        encoder.start()
        encoder.write(self.chain_id, Numbers.OctetString)
        encoder.write(self.expiration, Numbers.OctetString)
        encoder.write(self.ref_block_num, Numbers.OctetString)
        encoder.write(self.ref_block_prefix, Numbers.OctetString)
        encoder.write(self.net_usage_words, Numbers.OctetString)
        encoder.write(self.max_cpu_usage_ms, Numbers.OctetString)
        encoder.write(self.delay_sec, Numbers.OctetString)

        encoder.write(self.ctx_free_actions_size, Numbers.OctetString)
        encoder.write(self.actions_size, Numbers.OctetString)
        for action in self.actions:
            encoder.write(action.account, Numbers.OctetString)
            encoder.write(action.name, Numbers.OctetString)
            encoder.write(action.auth_size, Numbers.OctetString)
            for auth in action.auth:
                (auth_actor, permission) = auth
                encoder.write(auth_actor, Numbers.OctetString)
                encoder.write(permission, Numbers.OctetString)
            encoder.write(action.data_size, Numbers.OctetString)
            encoder.write(action.data, Numbers.OctetString)
        encoder.write(self.tx_ext, Numbers.OctetString)
        encoder.write(self.cfd, Numbers.OctetString)

        return [encoder.output()]