from .pdu import PDU
from struct import pack_into,unpack_from

class KeepAlive(PDU):
    """
    Keepalive packet.
    """
    message_type = 4

    def __init__(self, time: int = 0):
        super().__init__()
        self.time = time

    def decode_from(self, data: bytearray, pos: int = 0, len: int = 0) -> int:
        #print(data)
        if len == 4:
            self.time = unpack_from('!I', data[pos:pos+4])[0]
            pos += 4
        elif len == 2:
            self.time = unpack_from('!H', data[pos:pos+2])[0] * 1000
            pos += 2
        else:
            raise ValueError('Bad keepalive timeout length.')
        return pos

    def encode_to(self, dst: bytearray, pos: int = 0) -> int:
        #print('keepalive.encode_to')
        #print(self.time)
        if self.time % 1000:
            #print('1')
            pack_into('!I', dst, pos, self.time)
            pos += 4
        else:
            #print('2')
            pack_into('!H', dst, pos, self.time // 1000)
            pos += 2
        return pos

    def encoded_length(self) -> int:
        if self.time % 1000:
            return 4
        else:
            return 2


