from typing import Callable
from dataclasses import dataclass

from aes70.ocp1.encode_message import encode_message_to, MESSAGE_HEADER_SIZE

pduTypeKeepAlive = 4

@dataclass
class MessageGenerator:
    _batchSize: int
    _result_callback: Callable[[bytes], None]
    _pdus: list = None
    _currentSize: int = 0
    _currentCount: int = 0
    _lastMessageType: int = -1
    _flushScheduled: bool = False

    def __init__(self, batch_size: int, cb: Callable[[bytes], None]) -> None:
        self. _batchSize = batch_size
        self. _result_callback = cb

        if not (self._batchSize <= 0xffffffff):
            raise TypeError('Invalid batch size.')
        self._pdus = []

    def _flush_cb(self):
        self._flushScheduled = False
        if self._pdus is None:
            return
        self.flush()

    def add(self, pdu):
        current_size = self._currentSize
        encoded_length = pdu.encoded_length()
        message_type = pdu.message_type

        #print("pdu:", pdu)
        # Can we add to the current message?
        combine = (
            self._lastMessageType == message_type
            and message_type != pduTypeKeepAlive
            and self._currentCount < 0xffff
        )
        additional_size = encoded_length

        if not combine:
            additional_size += MESSAGE_HEADER_SIZE

        # The resulting buffer would become too large, we flush now.
        if current_size and current_size + additional_size > self._batchSize:
            self.flush()
            additional_size = encoded_length + MESSAGE_HEADER_SIZE

        self._pdus.append(pdu)
        self._currentSize += additional_size

        if combine:
            self._currentCount += 1
        else:
            self._currentCount = 1

        # Keepalive packets are never combined into one message.
        self._lastMessageType = message_type

        if self._currentSize > self._batchSize:
            self.flush()
        elif len(self._pdus) == 1:
            self.scheduleFlush()

    def scheduleFlush(self):
        if self._flushScheduled:
            return
        self._flushScheduled = True
        try:
            self._flush_cb()
        except Exception as err:
            print(f"Error: {err}")

    def flush(self):
        if not self._currentSize:
            return

        #print(f"flushing, current size: {self._currentSize}")
        pdus = self._pdus
        buf = bytearray(self._currentSize)
        pos = 0
        fr = 0

        for i in range(len(pdus)):
            pdu = pdus[i]
            message_type = pdu.message_type
            if (
                i == len(pdus) - 1
                or i + 1 - len(pdus) == 0xffff
                or message_type == pduTypeKeepAlive
                or message_type != pdus[i + 1].message_type
            ):
                pos = encode_message_to(buf, pos, pdus, fr, i + 1)
                fr = i + 1
        self._currentSize = 0
        self._lastMessageType = -1
        self._currentCount = 0
        self._pdus.clear()
        #print("sending bytes(", len(buf), "):", buf)
        self._result_callback(bytes(buf))

    def dispose(self):
        self._pdus = []


