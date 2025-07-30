from struct import pack_into, unpack_from

from ..OCP1.createType import create_type, Type

def toByteLength(length):
    return (length + 7) >> 3

def bitstring_decode_from(data: bytearray, pos: int):
    length = unpack_from('!H', data, pos)[0]
    pos += 2
    return [pos + toByteLength(length), decodeBitstring(data, pos, length)]


def bitstring_encode_to(data: bytearray, pos: int, value):
    pack_into('!H', data, pos, len(value))
    pos+=2
    return encodeBitstring(data, pos, value)

def bitstring_encoded_length(value):
    if not isinstance(value, list):
        raise TypeError('Expected Array.')

    length = len(value)

    if length > 0xffff:
        raise TypeError('Array too long for OcaBlob OCP.1 encoding.')

    return 2 + ((length + 7) >> 3)

def bitstring_decode_length(data: bytearray, pos: int):
    return  pos + 2 + toByteLength(unpack_from('!H', data, pos)[0])


# Function to decode a bitstring from the dataView starting at pos with a given length (number of bits)
def decodeBitstring(data: bytearray, pos: int, length: int):
    # Create a result list of booleans with the same length as the number of bits to decode
    result = [None] * length
    byteLength = toByteLength(length)
    # Create a view (slice) on the underlying buffer from the correct offset for byteLength bytes
    start = pos
    a8 = data[start : start + byteLength]
    for i in range(length):
        # For each bit, determine its boolean value using bitwise operations
        result[i:i] = bool((a8[i >> 3] & (128 >> (i & 7))))
    return result

# Function to encode a bitstring (provided as a list of booleans) into the dataView starting at pos.
# Note: The parameter 'source' is used instead of the reserved word 'from'
def encodeBitstring(data: bytearray, pos: int, source: list):
    length = len(source)
    byteLength = toByteLength(length)
    start =  pos
    i = 0
    for j in range(byteLength):
        tmp = 0
        for k in range(8):
            if i < length:
                if source[i]:
                    tmp |= 128 >> k
                i += 1
        data[start + j:start + j] = tmp
    return pos + byteLength


OcaBitstring = create_type(Type(
    is_constant_length = False,
    encoded_length = bitstring_encoded_length,
    encode_to = bitstring_encode_to,
    decode_from = bitstring_decode_from,
    decode_length = bitstring_decode_length,
))
