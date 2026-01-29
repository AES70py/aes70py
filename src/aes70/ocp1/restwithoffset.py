import typing
from sys import excepthook

from .createtype import create_type, Type


def RestWithOffset(offset: int) -> Type:

    def type_decode_from(data: bytearray, pos: int):
        length = len(data) - pos - offset
        return pos + length, bytearray(data[pos:pos+length])

    def type_encode_to(data: bytearray, pos: int, value):
        length = len(value)
        # Create source bytes from the memoryview
        src = bytes(value)
        # Get destination slice starting at pos
        dst = data[pos:pos + length]
        # Copy source data to destination
        dst[:] = src
        return pos + length

    def type_encoded_length(value):
        if not isinstance(value, bytearray):
            raise TypeError("expected bytearray, got {}".format(type(value)))
        return len(value) - offset

    def type_can_encode(value):
        if isinstance(value, bytearray) or isinstance(value, memoryview):
            return True
        else:
            return False

    def type_decode_length(data, pos: int):
        length = len(data) - pos - offset
        return pos + length

    type_def = Type(
        is_constant_length=False,
        can_encode=type_can_encode,
        encoded_length=type_encoded_length,
        encode_to=type_encode_to,
        decode_from=type_decode_from,
        decode_length=type_decode_length
    )
    type_obj = create_type(type_def)


    return type_obj