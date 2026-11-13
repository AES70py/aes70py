from typing import Optional
from struct import pack, unpack

from aes70.ocp1.pdu import PDU
from aes70.ocp1.ocaevent import OcaEvent
from aes70.ocp1.encoded_arguments import EncodedArguments

class Notification2(PDU):
    """
    Notification sent for subscriptions made with AddSubscription2 (OCP.1 message type 5).

    The data that follows the header is the event data, encoded the same way as the
    parameters of an EV1 Notification, or the exception data if exception is set.
    """
    event: OcaEvent
    exception: bool
    parameters: Optional[bytes]
    message_type: int = 5

    def __init__(self, event: OcaEvent = None, exception: bool = False, parameters = None) -> None:
        self.event = event
        self.exception = bool(exception)
        self.parameters = parameters or None

    def encode_to(self, dst: bytearray, pos: int) -> int:
        dst[pos:pos+4] = pack('!I', self.encoded_length())
        pos += 4
        dst[pos:pos+4] = pack('!I', self.event.EmitterONo)
        pos += 4
        dst[pos:pos+2] = pack('!H', self.event.EventID.DefLevel)
        pos += 2
        dst[pos:pos+2] = pack('!H', self.event.EventID.EventIndex)
        pos += 2
        dst[pos] = 1 if self.exception else 0
        pos += 1
        if self.parameters:
            if isinstance(self.parameters, EncodedArguments):
                pos = self.parameters.encode_to(dst, pos)
            else:
                dst[pos:pos+len(self.parameters)] = self.parameters
                pos += len(self.parameters)
        return pos

    def encoded_length(self) -> int:
        if not self.parameters:
            return 13
        if isinstance(self.parameters, EncodedArguments):
            return 13 + self.parameters.byte_length
        return 13 + len(self.parameters)

    def decode_from(self, data: bytes, pos: int, data_len: int) -> int:
        length = unpack('!I', data[pos:pos+4])[0]
        pos += 4

        pos, self.event = OcaEvent.decode_from(data, pos)

        self.exception = data[pos] != 0
        pos += 1

        length -= 13
        if length < 0:
            raise ValueError('Bad Notification2 Length.')
        if length > 0:
            self.parameters = data[pos:pos+length]
            pos += length
        else:
            self.parameters = None
        return pos
