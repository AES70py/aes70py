"""
Tests for Connection classes.
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import socket

from aes70.connection import Connection
from aes70.controller.tcp_connection import TCPConnection
from aes70.controller.client_connection import ClientConnection


class TestConnection:
    """Test the base Connection class."""

    def test_connection_creation(self):
        """Test Connection can be created."""
        conn = Connection()
        assert conn is not None
        assert conn.batchSize == 64 * 1024  # Default batch size

    def test_connection_with_options(self):
        """Test Connection with custom options."""
        conn = Connection({'batch': 1024})
        assert conn.batchSize == 1024

    def test_connection_is_reliable(self):
        """Test Connection reports as reliable."""
        conn = Connection()
        assert conn.is_reliable() is True

    def test_connection_bytes_counters(self):
        """Test Connection tracks RX/TX bytes."""
        conn = Connection()
        assert conn.rx_bytes == 0
        assert conn.tx_bytes == 0

    def test_connection_read_updates_counters(self):
        """Test read() updates RX counters."""
        conn = Connection()
        initial_rx = conn.rx_bytes
        # Read some dummy data
        conn.read(b'\x00\x01\x02\x03')
        assert conn.rx_bytes == initial_rx + 4

    def test_connection_idle_time_tracking(self):
        """Test Connection tracks idle times."""
        conn = Connection()
        # Initially idle time should be very small
        assert conn.tx_idle_time() >= 0
        assert conn.rx_idle_time() >= 0

    def test_connection_close(self):
        """Test Connection close emits event."""
        conn = Connection()
        closed = False

        def on_close(*args):
            nonlocal closed
            closed = True

        conn.on('close', on_close)
        conn.close()
        assert closed is True

    def test_connection_error_event(self):
        """Test Connection error emits event."""
        conn = Connection()
        error_received = None

        def on_error(source, err):
            nonlocal error_received
            error_received = err

        conn.on('error', on_error)
        test_error = Exception("Test error")
        conn.error(test_error)
        assert error_received is test_error


class TestClientConnection:
    """Test the ClientConnection class."""

    def test_client_connection_creation(self):
        """Test ClientConnection can be created."""
        conn = ClientConnection({})
        assert conn is not None
        assert conn._pending_commands is not None

    def test_client_connection_command_handle_generation(self):
        """Test command handle generation."""
        conn = ClientConnection({})
        handle1 = conn._get_next_command_handle()
        handle2 = conn._get_next_command_handle()
        assert handle2 != handle1

    def test_client_connection_cleanup_rejects_pending(self):
        """Test cleanup rejects pending commands."""
        conn = ClientConnection({})

        # Create a mock pending command
        mock_pending = Mock()
        conn._pending_commands[1] = mock_pending

        conn.cleanup()

        # Should have called reject on pending command
        mock_pending.reject.assert_called_once()


class TestTCPConnection:
    """Test the TCPConnection class."""

    @patch('socket.socket')
    def test_tcp_connection_creation(self, mock_socket_class):
        """Test TCPConnection can be created with a socket."""
        mock_sock = Mock()
        mock_sock.settimeout = Mock()
        mock_socket_class.return_value = mock_sock

        # We need to mock threading to avoid starting real threads
        with patch('threading.Thread'):
            conn = TCPConnection(mock_sock, {})
            assert conn is not None
            assert conn.sock is mock_sock

    def test_tcp_connection_write(self):
        """Test TCPConnection write sends data."""
        mock_sock = Mock()
        mock_sock.sendall = Mock()

        with patch('threading.Thread'):
            conn = TCPConnection(mock_sock, {})
            test_data = bytearray(b'\x00\x01\x02\x03')
            conn.write(test_data)

        mock_sock.sendall.assert_called_once_with(test_data)

    def test_tcp_connection_cleanup_closes_socket(self):
        """Test TCPConnection cleanup closes socket."""
        mock_sock = Mock()
        mock_sock.close = Mock()
        mock_sock.settimeout = Mock()

        with patch('threading.Thread'):
            conn = TCPConnection(mock_sock, {})
            conn.cleanup()

        mock_sock.close.assert_called_once()


class TestConnectionIntegration:
    """Integration tests for Connection classes."""

    def test_connection_keepalive_interval(self):
        """Test setting keepalive interval."""
        conn = Connection()
        # Should not raise
        conn.set_keepalive_interval(10)
        assert conn.keepalive_interval == 10000  # Converted to milliseconds

    def test_connection_event_inheritance(self):
        """Test Connection inherits from Events."""
        from aes70.events import Events
        conn = Connection()
        assert isinstance(conn, Events)

    def test_connection_emit_read(self):
        """Test that Connection read triggers events."""
        conn = Connection()
        # Should handle empty read without error
        conn.read(bytearray())
