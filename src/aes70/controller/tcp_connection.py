import sys
import time
import socket
import threading
from aes70.controller.client_connection import ClientConnection

class TCPConnection(ClientConnection):
    sock = None

    def handle_client_recv(self) -> None:
        while True:
            try:
                data = self.sock.recv(10)
            except (TimeoutError):
                self._check_keepalive()
                continue
            except (OSError):
                #TODO this should be handled more cleanly.
                #print("Connection closed")
                break
            if not data:
                print('Bye')
                break
            else:
                #print('got data')
                self.read(data)

    def __init__(self, sock, options):
        super().__init__(options)
        self.sock = sock
        sock.settimeout(1)
        threading.Thread(target=self.handle_client_recv, args=(

        )).start()

    def cleanup(self):
        super().cleanup()
        try:
            #print('Close the connection')
            self.sock.close()
        except:
            print(repr('error closing connection: ' + sys.exception()))

    def write(self, buf: bytearray):
        #print('>> write: ' + str(buf))
        self.sock.sendall(buf)
        super().write(buf)

    def close(self):
        super().close()
        self.sock.close()

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
