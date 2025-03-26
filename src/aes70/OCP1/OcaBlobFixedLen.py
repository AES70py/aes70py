from struct import pack_into

from ..OCP1.createType import create_type, Type

def OcaBlobFixedLen(Length):

    def encoded_length(value):
        return Length

    def encodeTo(dataView: bytearray, pos, value):
        if not (isinstance(value, list) or isinstance(value, (bytearray, bytes))):
            raise TypeError('Expected Array or Uint8Array')

        length = len(value)

        if length != Length:
            raise Exception('Length mismatch.')

        start = pos
        end = start + Length
        if isinstance(value, list):
            value = bytearray(value)
        elif isinstance(value, bytes):
            value = bytearray(value)

        pack_into(str(len) + 's', dataView, pos, length)

        return pos + Length

    def decode(dataView, pos):
        start = pos
        end = start + Length
        return bytearray(dataView[start:end])

    return create_type(Type(
        is_constant_length=False,
        decode_length=encoded_length,
        encode_to=encodeTo,
        decode_from=decode,
    ))
