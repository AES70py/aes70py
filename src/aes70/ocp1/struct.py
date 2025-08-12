from typing import Any, Dict
from aes70.OCP1.createType import create_type, Type


def Struct(types: Dict[str, Any], data_type: Any = None) -> Any:
    def struct_decode_from(data: bytearray, pos: int):
        #print("Struct decode_from")
        vals = []
        for name in types.keys():
            decoder = types[name]
            #print("name: ", name, " decoder: ", decoder)
            pos, d = decoder.decode_from(data, pos)
            #print("decoded ", name, " to ", d)
            vals.append(d)
        #print("vals: ", vals)
        #print("Datatype: ", DataType)
        s = DataType(*vals)
        #print("decoded object: ", s)
        #for x in s.__dict__:
            #print(x, ": ", s.__dict__[x])
        return pos, s

    def struct_decode_length(data: bytearray, pos: int) -> int:
        return sum(types[name]['decode_length'](data, pos) for name in types)

    def struct_encode_to(data: bytearray, pos: int, value) -> int:
        return sum(types[name]['encode_to'](data, pos, value[name]) for name in types)

    def struct_encoded_length(value) -> int:
        return sum(types[name]['encode_length'](value[name]) for name in types)

    count_types = len(types)

    if not data_type:
        class DataType:
            def __init__(self, *args):
                if len(args) == count_types:
                    for i, name in enumerate(types):
                        setattr(self, name, args[i])
                elif len(args) == 1 and isinstance(args[0], dict):
                    for name in types:
                        setattr(self, name, args[0][name])
                else:
                    raise TypeError('Unexpected arguments.')
    else:
        DataType = data_type

    return create_type(Type(
        type=DataType,
        is_constant_length=False,
        encoded_length=struct_encoded_length,
        encode_to=struct_encode_to,
        decode_from=struct_decode_from,
        decode_length=struct_decode_length)
        )
