from .createtype import create_type, Type
from .is_typed_array import is_typed_array

def OcaList2DConstantLength(_type):
    encoded_length = _type.encoded_length(None)
    encode_to = _type.encode_to
    decode = _type.decode_from

    def encoded_length_func(value):
        if not (isinstance(value, list) or is_typed_array(value)):
            raise TypeError('Expected array.')

        rows = len(value)

        if rows == 0:
            return 4

        if not (isinstance(value[0], list) or is_typed_array(value[0])):
            raise TypeError('Expected array.')

        columns = len(value[0])

        if rows > 0xffff or columns > 0xffff:
            raise ValueError('Array too long for OcaList2D OCP.1 encoding')

        return 4 + rows * columns * encoded_length

    def encode_to_func(data_view, pos, value):
        rows = len(value)
        columns = 0 if rows == 0 else len(value[0])

        data_view.set_uint16(pos, rows)
        pos += 2
        data_view.set_uint16(pos, columns)
        pos += 2

        for i in range(rows):
            row = value[i]

            for j in range(columns):
                pos = encode_to(data_view, pos, row[j])

        return pos

    def decode_from_func(data_view, pos):
        rows = data_view.get_uint16(pos)
        pos += 2
        columns = data_view.get_uint16(pos)
        pos += 2

        value = [[None for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            row = value[i]

            for j in range(columns):
                row[j] = decode(data_view, pos)
                pos += encoded_length

        return [pos, value]

    def decode_length_func(data_view, pos):
        rows = data_view.get_uint16(pos)
        pos += 2
        columns = data_view.get_uint16(pos)
        pos += 2

        pos += rows * columns * encoded_length

        return pos

    return create_type(Type(
        is_constant_length= False,
        encoded_length= encoded_length_func,
        encode_to= encode_to_func,
        decode_from= decode_from_func,
        decode_length= decode_length_func,
    ))

def OcaList2DDynamicLength(Type):
    encoded_length = Type.encoded_length
    encode_to = Type.encode_to
    decode_from = Type.decode_from
    decode_length = Type.decode_length

    def encoded_length_func(value):
        if not (isinstance(value, list) or is_typed_array(value)):
            raise TypeError('Expected array.')

        rows = len(value)

        if rows == 0:
            return 4

        if not (isinstance(value[0], list) or is_typed_array(value[0])):
            raise TypeError('Expected array.')

        columns = len(value[0])

        if rows > 0xffff or columns > 0xffff:
            raise ValueError('Array too long for OcaList2D OCP.1 encoding')

        result = 4

        for i in range(rows):
            row = value[i]

            for j in range(columns):
                result += encoded_length(row[j])

        return result

    def encode_to_func(data_view, pos, value):
        rows = len(value)
        columns = 0 if rows == 0 else len(value[0])

        data_view.set_uint16(pos, rows)
        pos += 2
        data_view.set_uint16(pos, columns)
        pos += 2

        for i in range(rows):
            row = value[i]

            for j in range(columns):
                pos = encode_to(data_view, pos, row[j])

        return pos

    def decode_from_func(data_view, pos):
        rows = data_view.get_uint16(pos)
        pos += 2
        columns = data_view.get_uint16(pos)
        pos += 2

        value = [[None for _ in range(columns)] for _ in range(rows)]

        for i in range(rows):
            row = value[i]

            for j in range(columns):
                pos, tmp = decode_from(data_view, pos)
                row[j] = tmp

        return [pos, value]

    def decode_length_func(data_view, pos):
        rows = data_view.get_uint16(pos)
        pos += 2
        columns = data_view.get_uint16(pos)
        pos += 2

        for i in range(rows):
            for j in range(columns):
                pos = decode_length(data_view, pos)

        return pos

    return create_type(Type(
        is_constant_length= False,
        encoded_length= encoded_length_func,
        encode_to= encode_to_func,
        decode_from= decode_from_func,
        decode_length= decode_length_func,
    ))

def OcaList2D(_type):
    return OcaList2DConstantLength(_type) if _type.is_constant_length else OcaList2DDynamicLength(_type)
