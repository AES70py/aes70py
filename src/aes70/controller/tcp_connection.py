import time
import socket
import threading
from aes70.controller.client_connection import ClientConnection

class TCPConnection(ClientConnection):
    sock = None

    def handle_client_recv(self) -> None:
        # whichever way the loop ends (peer EOF or a socket error),
        # close the connection, so cleanup() rejects every command still in
        # _pending_commands instead of leaving its future unsettled forever.
        try:
            while True:
                try:
                    data = self.sock.recv(10)
                except TimeoutError:
                    self._check_keepalive()
                    continue
                except OSError as err:
                    if not self.is_closed():
                        self.error(err)
                    return
                if not data:
                    return
                self.read(data)
        finally:
            self.close()

    def __init__(self, sock, options):
        super().__init__(options)
        self.sock = sock
        sock.settimeout(1)
        threading.Thread(target=self.handle_client_recv, args=(

        )).start()

    def cleanup(self):
        super().cleanup()
        self._close_socket()

    def _close_socket(self):
        try:
            #print('Close the connection')
            self.sock.close()
        except OSError as err:
            # was `'...' + sys.exception()`, a str + exception TypeError.
            print(f'error closing connection: {err!r}')

    def write(self, buf: bytearray):
        #print('>> write: ' + str(buf))
        self.sock.sendall(buf)
        super().write(buf)

    def close(self):
        super().close()
        self._close_socket()

    def _now(self):
        return time.perf_counter()

def connect(**kwargs):
    def onerror(ev):
        raise ev

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((kwargs['host'], kwargs['port']))
        sock.setblocking(True)
        conn = TCPConnection(sock, kwargs)
        return conn
    except Exception as e:
        onerror(e)
