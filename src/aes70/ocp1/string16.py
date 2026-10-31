from .createtype import Type, create_type
from struct import pack_into, unpack_from

# String16 is a Uint16 count of UTF-16 code units followed by the
# code units, big-endian (what aes70.js writes with charCodeAt). Upstream packed
# ord(char) as '!H', which raises struct.error for any character above U+FFFF;
# those are now written as a surrogate pair and the count includes both halves.
# Upstream also registered encoded_length as decode_length and gave the type no
# encoded_length at all, so EncodedArguments could not size a String16 argument.


def _utf16(value):
    if not isinstance(value, str):
        raise TypeError('Expected string.')
    return value.encode('utf-16-be', 'surrogatepass')


def encoded_length(value):
    # TODO: we could support more than strings
    units = len(_utf16(value)) // 2

    if units > 0xffff:
        raise Exception('Array too long for String16 OCP.1 encoding.')

    return 2 + 2 * units


def encode_to(dataView: bytearray, pos, value):
    data = _utf16(value)
    units = len(data) // 2

    if units > 0xffff:
        raise Exception('Array too long for String16 OCP.1 encoding.')

    pack_into('!H', dataView, pos, units)
    pos += 2

    dataView[pos:pos + len(data)] = data
    return pos + len(data)


def decode_from(dataView: bytearray, pos: int):
    units = unpack_from('!H', dataView, pos)[0]
    pos += 2

    data = bytes(dataView[pos:pos + 2 * units])
    if len(data) != 2 * units:
        raise ValueError('String16 truncated.')

    return pos + 2 * units, data.decode('utf-16-be', 'surrogatepass')


def decode_length(dataView: bytearray, pos):
    units = unpack_from('!H', dataView, pos)[0]

    return pos + 2 + 2 * units


String16 = create_type(Type(
    is_constant_length= False,
    encoded_length = encoded_length,
    decode_length = decode_length,
    encode_to =  encode_to,
    decode_from = decode_from,
))
