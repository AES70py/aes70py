from typing import Tuple, Any
from .createType import create_type, Type
from struct import pack_into, unpack_from


def float32_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!f', data, pos)[0]
    #print("uint32_decode_from, ", val)
    return val


def float32_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!f', data, pos, value)
    return pos + 4


OcaFloat32 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 4,
    encode_to=float32_encode_to,
    decode_from=float32_decode_from
)
)
