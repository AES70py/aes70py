from typing import Any

from aes70.ocp1.createType import create_type, Type
from struct import pack_into, unpack_from


def uint32_decode_from(data: bytearray, pos: int) -> tuple[Any, ...]:
    val = unpack_from('!I', data, pos)[0]
    #print("uint32_decode_from, ", val)
    return val


def uint32_encode_to(data: bytearray, pos: int, value) -> int:
    pack_into('!I', data, pos, value)
    return pos + 4


OcaUint32 = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 4,
    encode_to=uint32_encode_to,
    decode_from=uint32_decode_from
)
)
