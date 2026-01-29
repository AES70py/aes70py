import time
import threading
from .events import Events
from aes70.ocp1.decode_message import decode_message
from aes70.ocp1.keepalive import KeepAlive
from aes70.ocp1.message_generator import MessageGenerator


class Connection(Events):

    def __init__(self, options=None):
        if options is None:
            options = {}
        super().__init__()
        now = self._now()
        self.options = options
        self.batchSize = options.get('batch', 64 * 1024)

        self.inbuf = None
        self.inpos = 0
        self.last_rx_time = now
        self.last_tx_time = now
        self.rx_bytes = 0
        self.tx_bytes = 0
        self.keepalive_interval = -1
        self._keepalive_interval_id = None

        self._message_generator = MessageGenerator(self.batchSize, self.write)

        self.on('close', self.onClose)
        self.on('error', self.onError)

    def onError(self, conn, exception):
        if self.is_closed():
            return
        self.emit('close')

    def onClose(self, conn):
        # print('Closing connection')
        if self.is_closed() :
            return
        self.cleanup()

    # @property
    def is_reliable(self):
        return True

    def write(self, buf):
        #print('connection.write: ', len(buf))
        self.last_tx_time = self._now()
        self.tx_bytes += len(buf)

    def send(self, pdu):
        if self.is_closed():
            raise Exception("Connection is closed.")
        self._message_generator.add(pdu)

    def tx_idle_time(self):
        return self._now() - self.last_tx_time

    def rx_idle_time(self):
        return self._now() - self.last_rx_time

    def read(self, buf):
        self.rx_bytes += len(buf)
        self.last_rx_time = self._now()

        if self.inbuf:
            len_remaining = len(self.inbuf) - self.inpos
            tmp = bytearray(len_remaining + len(buf))
            tmp[:len_remaining] = self.inbuf[self.inpos:]
            tmp[len_remaining:] = buf
            self.inbuf = None
            self.inpos = 0
            buf = tmp

        pos = 0

        #print('>> data ' + str(len(buf)))
        try:
            while pos < len(buf):
                ret = []
                #print('decoding from ' + str(pos))
                len_decoded = decode_message(buf, pos, ret)
                #print('len_decoded: ' + str(len_decoded))
                if len_decoded == -1:
                #print('pos ' + str(pos))
                    self.inbuf = buf[pos:]
                    self.inpos = 0
                    break
                pos = len_decoded
                #print(ret)
                self.incoming(ret)
        except Exception as e:
            if self.is_reliable:
                #print(e)
                self.emit('error', e)
                return
            else:
                print(e)

        self._check_keepalive()

    def incoming(self, a):
        pass

    def is_closed(self) -> bool:
        return self._message_generator is None

    def close(self):
        if self.is_closed():
            return
        self.emit('close')

    def error(self, err):
        if self.is_closed():
            return
        self.emit('error', err)

    def cleanup(self):
        if self.is_closed():
          return
        self.set_keepalive_interval(0)
        if self._message_generator is not None:
            self._message_generator.dispose()
        self._message_generator = None
        self.remove_all_event_listeners()

    def _check_keepalive(self):
        #print("===== checking keepalive at ", self._now())
        if not (self.keepalive_interval > 0):
            return

        t = self.keepalive_interval

        #print('tx idle ' + str(self.tx_idle_time()))
        #print('tx idle1 ' + str(((t/1000) * 0.3)))
        if self.rx_idle_time() > ((t/1000) * 3):
            self.emit('timeout')
            self.error(Exception('Keepalive timeout.'))
        if self.tx_idle_time() > ((t/1000) * 0.3):
            self.flush()
            # if self.tx_idle_time() > (t/1000 * 0.75):
         #   print("####### keepalive")
            self.send(KeepAlive(t))
            self.flush()

    def flush(self):
        if self._message_generator is not None:
            self._message_generator.flush()

    def set_keepalive_interval(self, seconds):
        #print("set_keepalive_interval ", seconds)
        t = seconds * 1000

        if self._keepalive_interval_id is not None:
            self._keepalive_interval_id.cancel()
            self._keepalive_interval_id = None

        self.keepalive_interval = t

        if self.is_closed():
            return

        self.send(KeepAlive(t))

        if not (t > 0):
            return

        def keepalive_check():
            self._check_keepalive()

        self._keepalive_interval_id = threading.Timer(t / 5000.0, keepalive_check)
        self._keepalive_interval_id.start()

    def _now(self):
        return time.time()



