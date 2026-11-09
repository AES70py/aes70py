"""
Regression tests — one per defect fixed in this change set
(LOOSE-controller-tcp-connection-18). Not part of the upstream 1.0.3 sdist;
see SRC/upstream.json "fork" for the list of changes.
"""
import queue
import socket
import threading
import time

import asyncio

import pytest
import websocket
from websocket import ABNF

from aes70.controller.control_classes.ocamute import OcaMute
from aes70.controller.remote_device import RemoteDevice
from aes70.controller.tcp_connection import TCPConnection
from aes70.controller.ws_connection import WebSocketConnection
from aes70.ocp1.command import Command
from aes70.ocp1.encode_message import calculate_message_length, encode_message_to
from aes70.ocp1.response import Response
from aes70.types.ocamutestate import OcaMuteState
from aes70.ocp1.commandrrq import CommandRrq
from aes70.ocp1.encoded_arguments import EncodedArguments
from aes70.ocp1 import string16
from aes70.ocp1.string16 import String16


class FakeWebSocket:
    """Minimal stand-in for websocket.WebSocket, just enough to drive
    WebSocketConnection's receive thread without a real socket."""

    def __init__(self):
        self.closed = False
        self.sent = []
        self._queue = queue.Queue()

    def push(self, item):
        self._queue.put(item)

    def recv_data(self):
        try:
            item = self._queue.get(timeout=0.05)
        except queue.Empty:
            raise websocket.WebSocketTimeoutException()
        if isinstance(item, BaseException):
            raise item
        return item

    def send_binary(self, data):
        self.sent.append(bytes(data))

    def close(self):
        self.closed = True


def wait_closed(conn, timeout=5):
    # cleanup() rejects pending commands first, then pauses 0.2 s before it
    # finishes closing, so is_closed() trails the callback slightly.
    deadline = time.monotonic() + timeout
    while not conn.is_closed() and time.monotonic() < deadline:
        time.sleep(0.02)
    return conn.is_closed()


def test_peer_close_settles_command_in_flight():
    """Receive thread ending on EOF must reject every pending command."""
    ours, peer = socket.socketpair()
    conn = TCPConnection(ours, {})
    settled = threading.Event()
    outcome = []

    def callback(ok, result):
        outcome.append((ok, result))
        settled.set()

    conn.send_command(CommandRrq(1, 1, 1, 0, None), None, callback=callback)
    conn.flush()
    assert peer.recv(100)  # the command reached the wire
    peer.close()

    assert settled.wait(5), 'command in flight never settled after peer close'
    ok, err = outcome[0]
    assert ok is False and str(err) == 'closed'
    assert wait_closed(conn)
    assert conn._pending_commands is None


def test_socket_error_settles_command_in_flight():
    """Receive thread ending on OSError must also reject pending commands."""
    ours, peer = socket.socketpair()
    conn = TCPConnection(ours, {})
    settled = threading.Event()
    conn.send_command(CommandRrq(1, 1, 1, 0, None), None,
                      callback=lambda ok, r: settled.set())
    conn.flush()
    peer.recv(100)
    ours.shutdown(socket.SHUT_RDWR)
    ours.close()  # recv in the thread now raises OSError (EBADF)
    assert settled.wait(5)
    assert wait_closed(conn)
    peer.close()


def test_cleanup_survives_socket_close_error(capsys):
    """cleanup() used to raise TypeError building its error message."""
    ours, peer = socket.socketpair()
    conn = TCPConnection(ours, {})

    class Boom:
        def close(self):
            raise OSError('boom')

        def sendall(self, buf):
            pass

        def recv(self, n):
            raise OSError('gone')

    conn.sock = Boom()
    conn.cleanup()  # must not raise
    assert "OSError('boom')" in capsys.readouterr().out
    ours.close()
    peer.close()


def test_ws_close_frame_settles_command_in_flight():
    """Receive thread ending on a close frame must reject every pending command."""
    ws = FakeWebSocket()
    conn = WebSocketConnection(ws, {})
    settled = threading.Event()
    outcome = []

    def callback(ok, result):
        outcome.append((ok, result))
        settled.set()

    conn.send_command(CommandRrq(1, 1, 1, 0, None), None, callback=callback)
    conn.flush()
    assert ws.sent  # the command reached the fake transport
    ws.push((ABNF.OPCODE_CLOSE, b''))

    assert settled.wait(5), 'command in flight never settled after close frame'
    ok, err = outcome[0]
    assert ok is False and str(err) == 'closed'
    assert wait_closed(conn)
    assert conn._pending_commands is None


def test_ws_error_settles_command_in_flight():
    """Receive thread ending on a websocket/socket error must also reject pending commands."""
    ws = FakeWebSocket()
    conn = WebSocketConnection(ws, {})
    settled = threading.Event()
    conn.send_command(CommandRrq(1, 1, 1, 0, None), None,
                      callback=lambda ok, r: settled.set())
    conn.flush()
    ws.push(websocket.WebSocketConnectionClosedException('gone'))
    assert settled.wait(5)
    assert wait_closed(conn)


def test_ws_cleanup_survives_close_error(capsys):
    """cleanup() must not raise if closing the underlying websocket fails."""
    ws = FakeWebSocket()
    conn = WebSocketConnection(ws, {})

    def boom():
        raise OSError('boom')

    ws.close = boom
    conn.cleanup()  # must not raise
    assert "OSError('boom')" in capsys.readouterr().out


def test_command_param_count_limits():
    """OCP.1 parameter count is one Uint8: 255 encodes, 256 is refused clearly."""
    # EncodedArguments([], []) intentionally encodes zero bytes of actual
    # parameter data here; param_count=255 only needs to exercise the Uint8
    # boundary of the byte-level encoding, not a real matching argument list.
    cmd = Command(1, 1, 1, 255, EncodedArguments([], []))
    buf = bytearray(cmd.encoded_length())
    cmd.encode_to(buf, 0)
    assert buf[16] == 255

    with pytest.raises(ValueError, match='0..255'):
        Command(1, 1, 1, 256, EncodedArguments([], []))


@pytest.mark.parametrize('value', ['', 'OcaRoot', 'café', 'a\U0001F600b'])
def test_string16_round_trip(value):
    n = string16.encoded_length(value)
    buf = bytearray(n)
    assert string16.encode_to(buf, 0, value) == n
    assert string16.decode_length(buf, 0) == n
    assert string16.decode_from(buf, 0) == (n, value)


def test_string16_astral_is_a_surrogate_pair():
    """Above U+FFFF: two UTF-16 code units, counted as two (as aes70.js does)."""
    buf = bytearray(string16.encoded_length('\U0001F600'))
    string16.encode_to(buf, 0, '\U0001F600')
    assert bytes(buf) == bytes.fromhex('0002d83dde00')


def test_string16_sizes_as_an_argument():
    """EncodedArguments needs String16.encoded_length (upstream lacked it)."""
    args = EncodedArguments([String16], ['ab'])
    assert args.byte_length == 6
    buf = bytearray(6)
    assert args.encode_to(buf, 0) == 6
    assert bytes(buf) == bytes.fromhex('000200610062')


def test_property_event_over_notification2():
    """A device that accepts AddSubscription2 sends events as Notification2
    (message type 5). They must reach the subscriber, and the connection must
    stay open."""
    ours, peer = socket.socketpair()
    conn = TCPConnection(ours, {})
    device = RemoteDevice(conn)
    mute = OcaMute(4115, device)

    def fake_device():
        # Answer the AddSubscription2 command, then send one captured event.
        # The command PDU starts after the 10-byte message header: a uint32 size,
        # then the uint32 handle.
        buf = b""
        while len(buf) < 18:
            buf += peer.recv(4096)
        assert buf[7] == 1  # CommandRrq
        response = Response(int.from_bytes(buf[14:18], "big"), 0, 0)
        out = bytearray(calculate_message_length([response]))
        encode_message_to(out, 0, [response])
        peer.sendall(out)
        peer.sendall(bytes.fromhex(
            "3b00040000001c05000100000013000010130001000100000400010101"))

    async def run():
        received = asyncio.get_running_loop().create_future()
        loop = asyncio.get_running_loop()
        mute.OnStateChanged.subscribe(
            lambda value, *_: loop.call_soon_threadsafe(received.set_result, value))
        threading.Thread(target=fake_device, daemon=True).start()
        return await asyncio.wait_for(received, 5)

    try:
        assert asyncio.run(run()) == OcaMuteState.Muted
        assert device._supportsEV2 is True
        assert not conn.is_closed()
    finally:
        conn.close()
        peer.close()
