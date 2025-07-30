# Required dependencies and imports
from .createType import Type, create_type
from struct import pack_into, unpack_from

def count_codepoints(value):
    # Return the number of Unicode codepoints in the string.
    return len(value)


def _encoded_length(value):
    if not isinstance(value, bytes):
        raise TypeError('Expected bytes.')
    return 2 + len(value)

def _encode_to(dataView: bytearray, pos, value):
    length = len(value)
    if length > 0xffff:
        raise Exception('String too long for OcaString OCP.1 encoding.')
    pack_into('!H', dataView, pos, length)
    pos += 2

    # set the bytes into the underlying buffer at position (dataView.byteOffset + pos)
    dataView.append(value)
    return pos + length

def _decode_from(dataView: bytearray, pos):
    length = unpack_from('!H', dataView, pos)[0]
    pos += 2
    # convert the bytearray slice to bytes (maybe we could just return bytarray instead?)
    byte_data = bytes(dataView[pos: pos + length])
    return [pos + length, byte_data]

def _decode_length(dataView: bytearray, pos):
    length = unpack_from('!H', dataView, pos)[0]
    pos += 2
    return pos + length

OcaString = create_type(Type(
    is_constant_length= False,
    decode_length = _decode_length,
    encode_to =  _encode_to,
    decode_from = _decode_from,
    encoded_length = _encoded_length
))
