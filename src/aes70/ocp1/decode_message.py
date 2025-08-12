from aes70.ocp1.command import Command
from aes70.ocp1.commandrrq import CommandRrq
from aes70.ocp1.notification import Notification
from aes70.ocp1.response import Response
from aes70.ocp1.keepalive import KeepAlive

from typing import List

PDU_TYPES = [Command, CommandRrq, Notification, Response, KeepAlive]


def decode_message(data: bytearray, pos: int, ret: List) -> int:
    #print(data)
    #print(len(data))
    #print(data.find(b'\x3b'))
    #print(len(data) < (data.find(b'\x3b') + 10))
    if len(data) < (data.find(b'\x3b', pos) + 10):
        #print('not enough data for header')
        return -1
    #print('parsing')
    pos = pos | 0
    if data[pos] != 0x3b:
        raise ValueError('Bad sync value.')
    startpos = pos
    pos += 1
    # skipping protocol version?
    pos += 2
    message_size = int.from_bytes(data[pos:pos+4], byteorder='big')
    pos += 4
    message_type = data[pos]
    pos += 1
    message_count = int.from_bytes(data[pos:pos+2], byteorder='big')
    pos += 2

    # todo this seems more complicated logically than necessary.
    #print('marker: ' + str(startpos))
    # message size doesn't include the sync byte, so header is 9 bytes long
    message_offset = startpos - 9 + message_size
    #print('message size ' + str(message_size))

    #print('offset ' + str(message_offset))
    #print('pos ' + str(pos))
    #print('len ' + str(len(data)))

    # The message length must be at least message_size + 10 bytes long,
    # which includes the sync byte
    if message_offset > (len(data) - startpos - 10):
        #print('not enough data to parse message length')
        return -1

    ret.clear()
    ret.extend([None] * message_count)

    pdu_type = PDU_TYPES[message_type]

    if pdu_type is None:
        raise ValueError('Bad Message Type')

    if pdu_type is KeepAlive and message_count != 1:
        raise ValueError('Bad KeepAlive message count.')

    for i in range(message_count):
        ret[i] = pdu_type()
        pos = ret[i].decode_from(data, pos, message_offset)

    if pos != (startpos + 10 + message_offset):
        raise ValueError(f'Decode error: {pos} vs {message_offset}')

    return pos


