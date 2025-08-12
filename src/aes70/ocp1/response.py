from typing import Optional
from dataclasses import dataclass
from aes70.ocp1.pdu import PDU
from aes70.ocp1.encoded_arguments import EncodedArguments
from struct import  pack_into, unpack_from

@dataclass
class Response(PDU):
    handle: int
    status_code: int
    param_count: int
    parameters: Optional[bytes]

    message_type: int = 3

    def __init__(self, handle: int = 0, status_code: int = 0, param_count: int = 0, parameters: Optional[bytes] = None) -> None:
        self.handle = handle
        self.status_code = status_code
        self.param_count = param_count
        self.parameters = parameters or None

    def encoded_length(self):
        return 10 + (self.param_count * len(self.parameters) if self.parameters else 0)

    def decode_from(self, data: bytearray, pos, data_len):
        len = unpack_from('!I', data, pos)[0]
        pos += 4
        self.handle = unpack_from('!I', data, pos)[0]
        pos += 4
        self.status_code = unpack_from('!B', data, pos)[0]
        pos += 1
        self.param_count = unpack_from('!B', data, pos)[0]
        pos += 1
        len -= 10
        if len < 0:
            raise ValueError('Bad Response length.')
        if len > 0:
            if not self.param_count:
                raise ValueError(f'Decoding response with parameterCount=0 but {len} bytes of parameters')
            self.parameters = data[pos:pos+len]
            pos += len
        return pos

    def encode_to(self, dst, pos):
        pack_into('!I', dst, pos, self.encoded_length())
        pos += 4
        pack_into('!I', dst, pos, self.handle)
        pos += 4
        pack_into('!B', dst, pos, self.status_code)
        pos += 1
        pack_into('!B', dst, pos, self.param_count)
        pos += 1
        if self.param_count:
            if isinstance(self.parameters, EncodedArguments):
                pos = self.parameters.encode_to(dst, pos)
            else:
                dst[pos:pos+len(self.parameters)] = self.parameters
                pos += len(self.parameters)
        return pos
