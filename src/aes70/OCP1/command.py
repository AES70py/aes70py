from typing import Optional
from dataclasses import dataclass
from struct import pack, unpack

from .pdu import PDU
from .response import Response
from .encoded_arguments import EncodedArguments

@dataclass
class Command(PDU):
    target: int
    method_level: int
    method_index: int
    param_count: int
    parameters: Optional[bytes]

    message_type: int

    def __init__(self, target: int, method_level: int, method_index: int, param_count:int, parameters) -> None:
        self.target = target
        self.method_level = method_level or 0
        self.method_index = method_index or 0
        self.param_count = param_count or 0
        self.parameters = parameters or None
        self.handle = 0

    def encode_to(self, dst: bytearray, pos: int) -> int:
        #print("command.encode_to")
        #print("bytearray length: ", len(dst), " pos: ", pos)

        # TODO slicing is probably not the best way to deal with this
        # supposedly, bytearrays can be appended to efficiently.
        dst[pos:pos+4] = pack('!I', self.encoded_length())
        pos += 4
        dst[pos:pos+4] = pack('!I', self.handle)
        pos += 4
        dst[pos:pos+4] = pack('!I', self.target)
        pos += 4
        dst[pos:pos+2] = pack('!H', self.method_level)
        pos += 2
        dst[pos:pos+2] = pack('!H', self.method_index)
        pos += 2
        # TODO ensure we're not overflowing this value
        dst[pos] = self.param_count #pack('B', self.param_count)
        pos += 1
        #TODO This needs attention
        if self.param_count > 0:
            #print("doing arguments")
            if isinstance(self.parameters, EncodedArguments):
                #print("encoding")
                pos = self.parameters.encode_to(dst, pos)
            else:
                #print("encoding not needed")
                dst[pos:pos+len(self.parameters)] = self.parameters
                pos += len(self.parameters)

        return pos

    def encoded_length(self) -> int:

        return 17 + (self.parameters.byte_length if self.param_count > 0 else 0)

    def decode_from(self, data: bytes, pos: int, data_len: int) -> int:
        length = unpack('!I', data[pos:pos+4])[0]
        pos += 4
        self.handle = unpack('!I', data[pos:pos+4])[0]
        pos += 4
        self.target = unpack('!I', data[pos:pos+4])[0]
        pos += 4
        self.method_level = unpack('!H', data[pos:pos+2])[0]
        pos += 2
        self.method_index = unpack('!H', data[pos:pos+2])[0]
        pos += 2
        self.param_count = data[pos]
        pos += 1
        length -= 17
        if length < 0:
            raise ValueError('Bad Command Length.')
        if length > 0:
            if not self.param_count:
                raise ValueError('Expected no parameter bytes.')
            self.parameters = data[pos:pos+length]
            pos += length
        return pos

    def response(self, status_code, param_count: int, parameters) -> Response:
        return Response(self.handle, status_code, param_count, parameters)
