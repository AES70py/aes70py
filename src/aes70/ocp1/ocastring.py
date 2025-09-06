# Required dependencies and imports
from aes70.utf8 import utf8_encoded_length, utf8_codepoint_length, buffer_to_utf8, utf8_to_buffer
from .createtype import Type, create_type
from struct import pack_into, unpack_from

def count_codepoints(value):
    # Return the number of Unicode codepoints in the string.
    return len(value)


def _encoded_length(value):
    if not isinstance(value, str):
        raise TypeError('Expected string.')
    return 2 + utf8_encoded_length(value)

def _encode_to(dataView: bytearray, pos, value):
    length = count_codepoints(value)
    if length > 0xffff:
        raise Exception('String too long for OcaString OCP.1 encoding.')
    pack_into('!H', dataView, pos, length)
    pos += 2

    utf8_data = bytearray(utf8_to_buffer(value))
    # Set the utf8_data into the underlying buffer at position (dataView.byteOffset + pos)
    pack_into(str(len(utf8_data)) + 's', dataView, pos, utf8_data)
    return pos + len(utf8_data)

def _decode_from(dataView: bytearray, pos):
    codepoints = unpack_from('!H', dataView, pos)[0]
    pos += 2
    length = utf8_codepoint_length(dataView, pos, codepoints)
    utf8_data = dataView[pos: pos + length]
    return [pos + length, buffer_to_utf8(utf8_data)]

def _decode_length(dataView: bytearray, pos):
    codepoints = unpack_from('!H', dataView, pos)[0]
    pos += 2
    length = utf8_codepoint_length(dataView, pos, codepoints)
    return pos + length

OcaString = create_type(Type(
    is_constant_length= False,
    decode_length = _decode_length,
    encode_to =  _encode_to,
    decode_from = _decode_from,
    encoded_length = _encoded_length
))
