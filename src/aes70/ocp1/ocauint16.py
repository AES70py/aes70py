from typing import Tuple, Any

from .createtype import Type, create_type
from struct import pack_into, unpack_from


def uint16_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!H', data, pos)[0]
    #print("unpacked uint16 as ", val)
    return val


def uint16_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!H', data, pos, value)
    return pos + 2



OcaUint16 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 2,
    encode_to=uint16_encode_to,
    decode_from=uint16_decode_from
)
)
