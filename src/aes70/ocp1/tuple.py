import array
from .createtype import Type, create_type

# Encode an array in which each element may be independently typed.

def isTypedArray(x):
    return isinstance(x, (bytearray, memoryview, array.array))

def Tuple(*Types):
    Length = len(Types)

    def encodedLength(value):
        if not (isinstance(value, list) or isTypedArray(value)):
            raise TypeError('Expected array.')

        if len(value) != Length:
            raise ValueError('Length mismatch.')

        length = 0

        for i in range(Length):
            length += Types[i].encodedLength(value[i])

        return length

    def encodeTo(dataView, pos, value):
        for i in range(Length):
            pos = Types[i].encodeTo(dataView, pos, value[i])
        return pos

    def decodeFrom(dataView, pos):
        result = [None] * Length

        for i in range(Length):
            pos, tmp = Types[i].decodeFrom(dataView, pos)
            result[i] = tmp

        return pos, result

    def decodeLength(dataView, pos):
        for i in range(Length):
            pos = Types[i].decodeLength(dataView, pos)

        return pos

    return create_type(Type(
        is_constant_length= False,
        encoded_length= encodedLength,
        encode_to= encodeTo,
        decode_from= decodeFrom,
        decode_length= decodeLength,
    ))
