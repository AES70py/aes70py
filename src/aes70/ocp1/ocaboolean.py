from aes70.ocp1.createtype import create_type, Type
from struct import pack_into, unpack_from

def encode_to(dataView: bytearray, pos: int, value):
    pack_into('?', dataView, pos, value);
    return pos + 1

def decode(dataView: bytearray, pos: int):
    #print("dataview: ", len(dataView))
    return unpack_from('?', dataView, pos)[0]

OcaBoolean = create_type(Type(
    is_constant_length=True,
    encoded_length=lambda x=None: 1,
    encode_to=encode_to,
    decode_from=decode
)
)