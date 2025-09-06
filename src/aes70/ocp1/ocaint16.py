from typing import Tuple, Any

from .createtype import Type, create_type
from struct import pack_into, unpack_from


def int16_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!h', data, pos)[0]
    print("unpacked int16 as ", val)
    return val


def int16_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!h', data, pos, value)
    return pos + 2



OcaInt16 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 2,
    encode_to=int16_encode_to,
    decode_from=int16_decode_from
)
)
