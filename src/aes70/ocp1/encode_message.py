import struct

MESSAGE_HEADER_SIZE = 10


def calculate_message_length(pdus):
    length = MESSAGE_HEADER_SIZE
    message_type = pdus[0].message_type
    
    for pdu in pdus:
        if pdu.message_type != message_type:
            raise ValueError('Cannot combine different types in one message.')
        length += pdu.encoded_length()
    
    return length


def encode_message_to(dst: bytearray, pos: int, pdus, offset=0, end=None):
    if end is None:
        end = len(pdus)
    
    count = end - offset
    if not (count <= 0xFFFF):
        raise ValueError('Too many PDUs.')
    
    dst[pos] = 0x3B
    pos += 1
    
    start_pos = pos
    struct.pack_into('!H', dst, pos, 1)
    pos += 2
    len_pos = pos
    pos += 4
    #print("offset: " + str(offset))
    #print("msgtype: " + str(pdus[offset].message_type))
    dst[pos] = pdus[offset].message_type
    pos += 1
    struct.pack_into('!H', dst, pos, end - offset)
    pos += 2
    for i in range(offset, end):
        #print("starting offset: " + str(pos))
        pos = pdus[i].encode_to(dst, pos)
        #print("ending offset: " + str(pos))
        struct.pack_into('!I', dst, len_pos, pos - start_pos)

    return pos


def encode_message(a):
    if not isinstance(a, list):
        a = [a]
    
    length = calculate_message_length(a)
    buf = bytearray(length)
    
    pos = encode_message_to(buf, 0, a)
    
    if pos != length:
        raise ValueError('Message length mismatch.')
    
    return buf

