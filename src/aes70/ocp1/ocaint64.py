from typing import Any

from aes70.ocp1.createtype import create_type, Type
from struct import pack_into, unpack_from


def int64_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!q', data, pos)[0]
    print("int32_decode_from, ", val)
    return val


def int64_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!q', data, pos, value)
    return pos + 4


OcaInt64 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 8,
    encode_to=int64_encode_to,
    decode_from=int64_decode_from
)
)
