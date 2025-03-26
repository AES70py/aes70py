from typing import Callable, Tuple

class Type():
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

    def __repr__(self):
        return 'literal(%s)' % ', '.join('%s = %r' % i for i in sorted(iter(self.__dict__.items())))

    def __str__(self):
        return repr(self)


# if we call this with a constant length type, we don't have to worry about returning tuples
# or the decoded length. otherwise, we have to return a tuple from decode_from and calculate the decoded length
def create_type(type):
    if not type.is_constant_length:
        return type

    encoded_length = type.encoded_length()
    decode_from = type.decode_from
    encode_to = type.encode_to

    def type_decode_from(data: bytearray, pos: int):
        #print("fixed length decode from")
        return pos + encoded_length, decode_from(data, pos)

    def type_decode_length(data: bytearray, pos: int) -> int:
        return pos + encoded_length

    return Type(
        is_constant_length = True,
        encoded_length = type.encoded_length,
        encode_to = encode_to,
        decode_from = type_decode_from,
        decode_length = type_decode_length
    )

