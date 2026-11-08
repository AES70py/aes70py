import time
import threading
import websocket
from websocket import ABNF
from aes70.controller.client_connection import ClientConnection


class WebSocketConnection(ClientConnection):
    _ws = None

    def handle_recv(self) -> None:
        # ensure that we close the connection, so cleanup()
        # rejects every command still in _pending_commands rather than
        # leaving them hanging forever
        try:
            while True:
                try:
                    opcode, data = self._ws.recv_data()
                except websocket.WebSocketTimeoutException:
                    self._check_keepalive()
                    continue
                except (websocket.WebSocketConnectionClosedException, OSError) as err:
                    self.error(err)
                    return
                if opcode == ABNF.OPCODE_CLOSE:
                    return
                if isinstance(data, str):
                    data = data.encode()
                self.read(data)
        finally:
            self.close()

    def __init__(self, ws, options):
        super().__init__(options)
        self._ws = ws
        threading.Thread(target=self.handle_recv, daemon=True).start()

    def write(self, buf: bytearray):
        self._ws.send_binary(bytes(buf))
        super().write(buf)

    def cleanup(self):
        super().cleanup()
        self._close_ws()

    def _close_ws(self):
        try:
            self._ws.close()
        except (OSError, websocket.WebSocketException) as err:
            print(f'error closing connection: {err!r}')

    def close(self):
        super().close()

    def _now(self):
        return time.perf_counter()


def connect(**kwargs):
    """
    To use a secure WebSocket connection, pass `secure=True`
    """

    def onerror(ev):
        raise ev

    try:
        protocol = "ws://"
        if kwargs.get("secure"):
            protocol = "wss://"
        sslopt = kwargs.get("sslopt")

        ws = websocket.create_connection(
            url=f"{protocol}{kwargs['host']}:{kwargs['port']}", sslopt=sslopt
        )
        ws.settimeout(1)
        return WebSocketConnection(ws, kwargs)
    except Exception as e:
        onerror(e)
