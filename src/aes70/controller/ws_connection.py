import time
import threading
import websocket
from websocket import ABNF
from aes70.controller.client_connection import ClientConnection


class WebSocketConnection(ClientConnection):
    _ws = None

    def handle_recv(self) -> None:
        while True:
            try:
                opcode, data = self._ws.recv_data()
            except websocket.WebSocketTimeoutException:
                self._check_keepalive()
                continue
            except (websocket.WebSocketConnectionClosedException, OSError):
                break
            if opcode == ABNF.OPCODE_CLOSE:
                break
            if isinstance(data, str):
                data = data.encode()
            self.read(data)

    def __init__(self, ws, options):
        super().__init__(options)
        self._ws = ws
        threading.Thread(target=self.handle_recv, daemon=True).start()

    def write(self, buf: bytearray):
        self._ws.send_binary(bytes(buf))
        super().write(buf)

    def cleanup(self):
        super().cleanup()
        try:
            self._ws.close()
        except Exception:
            pass

    def close(self):
        super().close()
        try:
            self._ws.close()
        except Exception:
            pass

    def _now(self):
        return time.perf_counter()


def connect(**kwargs):
    def onerror(ev):
        raise ev

    try:
        ws = websocket.create_connection(f"ws://{kwargs['host']}:{kwargs['port']}")
        ws.settimeout(1)
        return WebSocketConnection(ws, kwargs["options"])
    except Exception as e:
        onerror(e)
