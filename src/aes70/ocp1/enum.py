import typing
from typing import Any, Callable, Dict
from .createtype import create_type, Type

def Enum(data_type: typing.Type, base: Type) -> Type:
    encode_to = base.encode_to
    decode_from = base.decode_from

    def encode_to_wrapper(data: bytearray, pos: int, value: Any) -> int:
        if isinstance(value, data_type):
            value = value.value
        elif isinstance(value, str):
            value = data_type.getValue(value)
        elif isinstance(value, (int, float)):
            data_type.getName(value)
        else:
            raise TypeError('Unsupported type.')
        return encode_to(data, pos, value)

    def decode_wrapper(data: bytearray, pos: int):
        value = decode_from(data, pos)
        return data_type(value[1])

    type_def = Type(
        is_constant_length =True,
        encoded_length = base.encoded_length,
        encode_to = encode_to_wrapper,
        decode_from = decode_wrapper,
    )
    type_obj = create_type(type_def)

    for name, value in data_type.values().items():
        setattr(type_obj, name, value)

    return type_obj
