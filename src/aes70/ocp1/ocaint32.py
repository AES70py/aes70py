from typing import Any

from aes70.ocp1.createType import create_type, Type
from struct import pack_into, unpack_from


def int32_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!i', data, pos)[0]
    print("int32_decode_from, ", val)
    return val


def int32_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!i', data, pos, value)
    return pos + 4


OcaInt32 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 4,
    encode_to=int32_encode_to,
    decode_from=int32_decode_from
)
)
