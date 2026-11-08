from .createtype import Type, create_type
from functools import lru_cache
from struct import pack_into, unpack_from

# String16 is a Uint16 count of UTF-16 code units followed by the
# code units, big-endian.

@lru_cache(maxsize=256)
def _utf16_encode(value: str) -> bytes:
    return value.encode('utf-16-be', 'surrogatepass')


def _utf16(value):
    if not isinstance(value, str):
        raise TypeError('Expected string.')
    return _utf16_encode(value)


def _utf16_unit_count(value):
    # Number of UTF-16 code units value would encode to, without actually
    # encoding it. BMP code points (<= U+FFFF) take one unit; the rest need
    # a surrogate pair (two units). Callers only need this count to size a
    # buffer, so this avoids a redundant _utf16_encode() call (and cache
    # lookup/lock) for every value that also gets passed to encode_to().
    if not isinstance(value, str):
        raise TypeError('Expected string.')
    return len(value) + sum(1 for ch in value if ord(ch) > 0xffff)


def encoded_length(value):
    # TODO: we could support more than strings
    units = _utf16_unit_count(value)

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

    pack_into(f'{len(data)}s', dataView, pos, data)
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

    end = pos + 2 + 2 * units
    if end > len(dataView):
        raise ValueError('String16 truncated.')

    return end


String16 = create_type(Type(
    is_constant_length= False,
    encoded_length = encoded_length,
    decode_length = decode_length,
    encode_to =  encode_to,
    decode_from = decode_from,
))
