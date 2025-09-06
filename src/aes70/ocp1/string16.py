from .createtype import Type, create_type
from struct import pack_into, unpack_from


def encoded_length(value):
    # TODO: we could support more than strings
    if not isinstance(value, str):
        raise TypeError('Expected string.')

    length = len(value)

    if length > 0xffff:
        raise Exception('Array too long for String16 OCP.1 encoding.')

    return 2 + 2 * length


def encode_to(dataView: bytearray, pos, value):
    length = len(value)

    pack_into('!H', dataView, pos, length)
    pos += 2

    for i in range(length):
        pack_into('!H', dataView, pos, ord(value[i]))
        pos += 2

    return pos


def decode_from(dataView: bytearray, pos: int):

    length = unpack_from('!H', dataView, pos)[0]
    pos += 2

    tmp = [None] * length

    for i in range(length):
        tmp[i] = unpack_from('!H', dataView, pos)[0]
        pos += 2

    return pos, ''.join(chr(code) for code in tmp)


def decode_length(dataView: bytearray, pos):
    length = unpack_from('!H', dataView, pos)[0]

    return pos + 2 + 2 * length


String16 = create_type(Type(
    is_constant_length= False,
    decode_length = encoded_length,
    encode_to =  encode_to,
    decode_from = decode_from,
))
