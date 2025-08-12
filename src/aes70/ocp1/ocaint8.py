from typing import Tuple, Any

from .createType import create_type, Type
from struct import pack_into, unpack_from


def int8_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    return  unpack_from('!b', data, pos)[0]


def int8_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!b', data, pos, value)
    return pos + 1


OcaInt8 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 1,
    encode_to=int8_encode_to,
    decode_from=int8_decode_from
)
)
