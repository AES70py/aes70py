from typing import Tuple, Any

from .createType import create_type, Type
from struct import pack_into, unpack_from


def uint8_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    return  unpack_from('!B', data, pos)[0]


def uint8_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!B', data, pos, value)
    return pos + 1


OcaUint8 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 1,
    encode_to=uint8_encode_to,
    decode_from=uint8_decode_from
)
)
