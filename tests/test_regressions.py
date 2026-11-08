"""
Regression tests — one per defect fixed in this change set
(LOOSE-controller-tcp-connection-18). Not part of the upstream 1.0.3 sdist;
see SRC/upstream.json "fork" for the list of changes.
"""
import socket
import threading
import time

from aes70.controller.tcp_connection import TCPConnection
from aes70.ocp1.commandrrq import CommandRrq


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
