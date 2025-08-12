import weakref

from aes70.ocp1.createtype import create_type, Type
from struct import pack_into, unpack_from
from collections import defaultdict

def OcaMultiMap(KeyType, ValueType):
    kencodedLength = KeyType.encoded_length
    kencodeTo = KeyType.encode_to
    kdecodeFrom = KeyType.decode_from
    kdecodeLength = KeyType.decode_length

    vencodedLength = ValueType.encoded_length
    vencodeTo = ValueType.encode_to
    vdecodeFrom = ValueType.decode_from
    vdecodeLength = ValueType.decode_length

    def encodedLength(value):
        # Check if value is a dict or a WeakKeyDictionary
        if not isinstance(value, (dict, weakref.WeakKeyDictionary)):
            raise TypeError('Expected Map or WeakMap')

        result = 2

        # Iterate over each key-value pair in the map, and create an entry for each value
        for key, val in value.items():
            for vval in val.values():
                result += kencodedLength(key)
                result += vencodedLength(vval)

        return result

    def encodeTo(dataView: bytearray, pos: int, value):
        # Write the size of the map as a 16-bit unsigned integer.

        # TODO consider if there might be a more efficient way to calculate the length
        l = 0
        for key, val in value.items():
            l += len(val)

        pack_into('!H', dataView, pos, l)
        pos += 2

        # Encode each key and value, updating the position accordingly.
        for key, val in value.items():
            for vval in val.values():
                pos = kencodeTo(dataView, pos, key)
                pos = vencodeTo(dataView, pos, vval)

        return pos

    def decodeFrom(dataView: bytearray, pos: int):
        result = defaultdict(list)
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2

        for i in range(length):
            pos, key = kdecodeFrom(dataView, pos)
            pos, val = vdecodeFrom(dataView, pos)
            result[key].append(val)

        if len(result) != length:
            raise Exception('Incorrect length provided for MultiMap')

        return pos, result

    def decodeLength(dataView: bytearray, pos: int):
        length = unpack_from('!H', dataView, pos)[0]
        pos += 2

        for i in range(length):
            pos = kdecodeLength(dataView, pos)
            pos = vdecodeLength(dataView, pos)

        return pos

    OcaMultiMap = create_type(Type(
        is_constant_length = False,
        encoded_length = encodedLength,
        encode_to =  encodeTo,
        decode_from = decodeFrom,
        decode_lendth = decodeLength,
    ))

