from typing import Any

from aes70.OCP1.createType import create_type, Type
from struct import pack_into, unpack_from


def uint64_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!Q', data, pos)[0]
    print("uint32_decode_from, ", val)
    return val


def uint64_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!Q', data, pos, value)
    return pos + 8


OcaUint64 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 8,
    encode_to=uint64_encode_to,
    decode_from=uint64_decode_from
)
)
