from typing import Tuple, Any
from .createtype import create_type, Type
from struct import pack_into, unpack_from


def float64_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!d', data, pos)[0]
    print("uint32_decode_from, ", val)
    return val


def float64_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!d', data, pos, value)
    return pos + 8


OcaFloat64 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 8,
    encode_to=float64_encode_to,
    decode_from=float64_decode_from
)
)
