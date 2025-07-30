import array
from .createType import Type, create_type
from struct import pack_into, unpack_from

def isTypedArray(x):
    return isinstance(x, (bytearray, memoryview, array.array))

def OcaListConstantLength(_type):
    encodedLengthConst = _type.encoded_length(None)
    encodeToFunc = _type.encode_to
    decodeFunc = _type.decode_from

    def encoded_length(value):
        if not (isinstance(value, list) or isTypedArray(value)):
            raise TypeError('Expected array.')
        length = len(value)
        if length > 0xffff:
            raise Exception('Array too long for OcaList OCP.1 encoding')
        return 2 + length * encodedLengthConst

    def encode_to(dataView: bytearray, pos, value):
        length = len(value)
        pack_into('!H', dataView, pos, length)
        pos += 2
        for i in range(length):
            pos = encodeToFunc(dataView, pos, value[i])
        return pos

    def decode_from(dataView: bytearray, pos):
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2
        value = [None] * length
        for i in range(length):
            value[i] = decodeFunc(dataView, pos)
            pos += encodedLengthConst
        return (pos, value)

    def decode_length(dataView: bytearray, pos):
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2 + length * encodedLengthConst
        return pos

    return create_type(Type(
        is_constant_length=False,
        decode_length=decode_length,
        encode_to=encode_to,
        decode_from=decode_from,
        encoded_length=encoded_length
    ))


def OcaListDynamicLength(_type):
    encodedLengthFunc = _type.encoded_length
    encodeToFunc = _type.encode_to
    decodeFromFunc = _type.decode_from
    decodeLengthFunc = _type.decode_length

    def encoded_length(value):
        if not (isinstance(value, list) or isTypedArray(value)):
            raise TypeError('Expected array.')
        length = len(value)
        if length > 0xffff:
            raise Exception('Array too long for OcaList OCP.1 encoding')
        result = 2
        for i in range(length):
            result += encodedLengthFunc(value[i])
        return result

    def encode_to(dataView: bytearray, pos: int, value):
        length = len(value)
        pack_into('!H', dataView, pos, length)
        pos += 2
        for i in range(length):
            pos = encodeToFunc(dataView, pos, value[i])
        return pos

    def decode_from(dataView: bytearray, pos: int):
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2
        value = [None] * length
        for i in range(length):
            pos, tmp = decodeFromFunc(dataView, pos)
            value[i] = tmp
        return (pos, value)

    def decode_length(dataView: bytearray, pos: int):
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2
        for i in range(length):
            pos = decodeLengthFunc(dataView, pos)
        return pos

    return create_type(Type(
        is_constant_length=False,
        decode_length=decode_length,
        encode_to=encode_to,
        decode_from=decode_from,
        encoded_length=encoded_length
    ))


def OcaList(_type):
    return OcaListConstantLength(_type) if _type.is_constant_length else OcaListDynamicLength(_type)
