"""
Smoke tests - verify all modules can be imported.
"""
import pytest


class TestModuleImports:
    """Test that all major modules can be imported without errors."""

    def test_import_aes70(self):
        """Test main aes70 package imports."""
        import aes70
        assert aes70 is not None

    def test_import_connection(self):
        """Test connection module imports."""
        from aes70 import connection
        assert hasattr(connection, 'Connection')

    def test_import_events(self):
        """Test events module imports."""
        from aes70 import events
        assert hasattr(events, 'Events')

    def test_import_controller(self):
        """Test controller module imports."""
        from aes70 import controller
        assert controller is not None

    def test_import_tcp_connection(self):
        """Test TCP connection module imports."""
        from aes70.controller import tcp_connection
        assert hasattr(tcp_connection, 'TCPConnection')
        assert hasattr(tcp_connection, 'connect')

    def test_import_remote_device(self):
        """Test remote device module imports."""
        from aes70.controller import remote_device
        assert hasattr(remote_device, 'RemoteDevice')

    def test_import_ocp1(self):
        """Test OCP1 module imports."""
        from aes70 import ocp1
        assert ocp1 is not None

    def test_import_types(self):
        """Test types module imports."""
        from aes70 import types
        assert types is not None

    def test_import_decode_message(self):
        """Test decode_message module imports."""
        from aes70.ocp1 import decode_message
        assert hasattr(decode_message, 'decode_message')

    def test_import_encode_message(self):
        """Test encode_message module imports."""
        from aes70.ocp1 import encode_message
        assert hasattr(encode_message, 'encode_message_to')


class TestClassInstantiation:
    """Test that major classes can be instantiated."""

    def test_events_instantiation(self):
        """Test Events class can be instantiated."""
        from aes70.events import Events
        events = Events()
        assert events is not None
        assert hasattr(events, 'emit')
        assert hasattr(events, 'on')

    def test_connection_instantiation(self):
        """Test Connection class can be instantiated with options."""
        from aes70.connection import Connection
        conn = Connection({'batch': 1024})
        assert conn is not None
        assert conn.batchSize == 1024

    def test_object_base_instantiation(self):
        """Test ObjectBase class can be instantiated."""
        from aes70.controller.object_base import ObjectBase

        class MockDevice:
            pass

        obj = ObjectBase(100, MockDevice())
        assert obj is not None
        assert obj.ono == 100
        assert obj.ObjectNumber == 100
