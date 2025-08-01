from typing import Optional
from struct import pack, unpack

from aes70.OCP1.pdu import PDU
from aes70.types.OcaEvent import OcaEvent
from aes70.OCP1.encoded_arguments import EncodedArguments

class Notification(PDU):
    target: int
    method_level: int
    method_index: int
    context: Optional[bytes]
    event: OcaEvent
    param_count: int
    parameters: Optional[bytes]
    message_type: int = 2

    def __init__(self, target: int, method_level: int, method_index: int, context, event: OcaEvent, param_count:int, parameters) -> None:
        self.target = target
        self.method_level = method_level or 0
        self.method_index = method_index or 0
        self.context = context
        self.event = event
        self.param_count = param_count or 0
        self.parameters = parameters or None


    def encode_to(self, dst: bytearray, pos: int) -> int:
        dst[pos:pos+4] = pack('!I', self.encoded_length())
        pos += 4
        dst[pos:pos+4] = pack('!I', self.target)
        pos += 4
        dst[pos:pos+2] = pack('!H', self.method_level)
        pos += 2
        dst[pos:pos+2] = pack('!H', self.method_index)
        pos += 2
        dst[pos] = self.param_count
        pos += 1
        if self.context:
            context_len = len(self.context)
            dst[pos:pos+2] = pack('!H', context_len)
            pos += 2
            if context_len > 0:
                dst[pos:pos+context_len] = self.context
                pos += context_len
        else:
            dst[pos:pos+2] = pack('!H', 0)
            pos += 2
        dst[pos:pos+4] = pack('!I', self.event.emitter_o_no)
        pos += 4
        dst[pos:pos+2] = pack('!H', self.event.event_id.def_level)
        pos += 2
        dst[pos:pos+2] = pack('!H', self.event.event_id.event_index)
        pos += 2
        if self.param_count > 1:
            if isinstance(self.parameters, EncodedArguments):
                pos = self.parameters.encode_to(dst, pos)
            else:
                dst[pos:pos+len(self.parameters)] = self.parameters
                pos += len(self.parameters)
        return pos

    def encoded_length(self) -> int:
        return 23 + (len(self.parameters) if self.param_count > 1 else 0) + (len(self.context) if self.context else 0)

    def decode_from(self, data: bytes, pos: int, data_len: int) -> int:
        length = unpack('!I', data[pos:pos+4])[0]
        pos += 4
        self.target = unpack('!I', data[pos:pos+4])[0]
        pos += 4
        self.method_level = unpack('!H', data[pos:pos+2])[0]
        pos += 2
        self.method_index = unpack('!H', data[pos:pos+2])[0]
        pos += 2
        self.param_count = data[pos]
        pos += 1
        context_length = unpack('!H', data[pos:pos+2])[0]
        pos += 2
        if context_length:
            self.context = data[pos:pos+context_length]
            pos += context_length
        else:
            self.context = None

        pos, self.event = OcaEvent.decode_from(data, pos)

        length -= 23 + context_length
        if length < 0:
            raise ValueError('Bad Notification Length.')
        if length > 0:
            self.parameters = data[pos:pos+length]
            pos += length
        return pos

