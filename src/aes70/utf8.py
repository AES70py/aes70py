import codecs

def buffer_to_utf8(a8):
    """
    Decodes a UTF8 encoded string from a bytes object.
    """
    return a8.decode('utf-8')

def utf8_to_buffer(str):
    """
    Encodes a string as UTF8.
    
    Returns:
        bytes: The UTF-8 encoded bytes.
    """
    return str.encode('utf-8')

def utf8_encoded_length(str):
    """
    Returns the number of bytes of the UTF8 encoding of a string.
    """
    return len(utf8_to_buffer(str))


def utf8_codepoint_length(dataView : bytearray, pos, codepoints):
    # Calculate the total number of bytes required to encode the given number of UTF-8 codepoints
    # starting from the current position in the DataView.

    index = pos
    bytes_count = 0
    remaining = codepoints
    # Iterate through the bytes counting the UTF-8 encoded characters.
    while remaining > 0:
        if index >= len(dataView):
            raise ValueError("Buffer ended unexpectedly while decoding UTF-8 codepoints.")
        first_byte = dataView[index]
        # Determine the length of the UTF-8 sequence by inspecting the first byte.
        if first_byte >> 7 == 0:
            char_length = 1
        elif (first_byte >> 5) == 0b110:
            char_length = 2
        elif (first_byte >> 4) == 0b1110:
            char_length = 3
        elif (first_byte >> 3) == 0b11110:
            char_length = 4
        else:
            raise ValueError("Invalid UTF-8 starting byte encountered.")
        # Ensure there are enough bytes in the buffer.
        if index + char_length > len(dataView):
            raise ValueError("Incomplete UTF-8 sequence in buffer.")
        index += char_length
        bytes_count += char_length
        remaining -= 1
    return bytes_count

#
# def utf8_codepoint_length(buf, pos, codepoints):
#     """
#     Counts the number of bytes occupied by a UTF8 encoded string
#     of given number of codepoints.
#
#     Args:
#         buf (memoryview): The input buffer.
#         pos (int): The buffer position.
#         codepoints (int): The number of unicode codepoints in the buffer.
#
#     Returns:
#         int: The number of bytes.
#     """
#     start = pos
#
#     # From table 3-6 in the Unicode standard 4.0: Well-Formed UTF-8
#     # Byte Sequences
#     #
#     #  Code Points   1st Byte  2nd Byte  3rd Byte  4th Byte
#     # 000000-00007f   00-7f
#     # 000080-0007ff   c2-df     80-bf
#     # 000800-000fff    e0       a0-bf     80-bf
#     # 001000-00cfff   e1-ec     80-bf     80-bf
#     # 00d000-00d7ff    ed       80-9f     80-bf
#     # 00e000-00ffff   ee-ef     80-bf     80-bf
#     # 010000-03ffff    f0       90-bf     80-bf     80-bf
#     # 040000-0fffff   f1-f3     80-bf     80-bf     80-bf
#     # 100000-10ffff    f4       80-8f     80-bf     80-bf
#
#     while codepoints > 0:
#         c = buf[pos]
#         pos += 1
#         if c <= 0x7f:
#             continue
#         if c < 0xc2:
#             raise ValueError("Invalid UTF8 sequence.")
#         pos += 1
#         if c <= 0xdf:
#             continue
#         pos += 1
#         if c <= 0xef:
#             continue
#         pos += 1
#         if c <= 0xf4:
#             continue
#
#         raise ValueError("Invalid UTF8 sequence.")
#
#         codepoints -= 1
#
#     return pos - start

def count_codepoints(s):
    """
    Counts the number of Unicode code points in a string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The number of code points.
    """
    n = 0
    
    for i in range(len(s)):
        c = ord(s[i])
        n += 1
        if 0xD800 <= c <= 0xDBFF:
            i += 1
            c = ord(s[i])
            if not 0xDC00 <= c <= 0xDFFF:
                raise TypeError("Expected valid unicode string.")
    
    return n


