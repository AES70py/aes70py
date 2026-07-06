import time
import threading
import websocket
from aes70.controller.client_connection import ClientConnection


class WebSocketConnection(ClientConnection):
    _ws = None

    def handle_recv(self) -> None:
        while True:
            try:
                data = self._ws.recv()
            except websocket.WebSocketTimeoutException:
                self._check_keepalive()
                continue
            except (websocket.WebSocketConnectionClosedException, OSError):
                break
            if not data:
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


def connect(host, port, **options):
    ws = websocket.create_connection(f"ws://{host}:{port}")
    ws.settimeout(1)
    return WebSocketConnection(ws, options)
