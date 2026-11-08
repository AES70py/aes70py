"""
Tests for OCP1 protocol encoding and decoding.
"""
import pytest
from aes70.ocp1.keepalive import KeepAlive
from aes70.ocp1.response import Response
from aes70.ocp1.command import Command
from aes70.ocp1.encode_message import encode_message_to, calculate_message_length
from aes70.ocp1.decode_message import decode_message


class TestKeepAlive:
    """Test KeepAlive PDU encoding and decoding."""

    def test_keepalive_creation(self):
        """Test KeepAlive can be created."""
        ka = KeepAlive(5000)
        assert ka.time == 5000
        assert ka.message_type == 4

    def test_keepalive_encode_decode_roundtrip(self):
        """Test KeepAlive encoding and decoding roundtrip."""
        original = KeepAlive(5000)
        dst = bytearray(1024)
        pos = original.encode_to(dst, 0)
        assert pos == 2  # 5000ms is divisible by 1000, so 2 bytes

        # Decode
        decoded = KeepAlive()
        new_pos = decoded.decode_from(dst, 0, 2)
        assert new_pos == 2
        assert decoded.time == 5000

    def test_keepalive_encode_milliseconds(self):
        """Test KeepAlive with non-divisible time uses 4 bytes."""
        ka = KeepAlive(5500)
        dst = bytearray(1024)
        pos = ka.encode_to(dst, 0)
        assert pos == 4  # 5500 is not divisible by 1000, so 4 bytes
        assert ka.encoded_length() == 4

    def test_keepalive_encoded_length(self):
        """Test KeepAlive encoded length calculation."""
        ka1 = KeepAlive(5000)
        assert ka1.encoded_length() == 2

        ka2 = KeepAlive(5500)
        assert ka2.encoded_length() == 4


class TestResponse:
    """Test Response PDU encoding and decoding."""

    def test_response_creation(self):
        """Test Response can be created."""
        resp = Response(handle=1, status_code=0, param_count=0)
        assert resp.handle == 1
        assert resp.status_code == 0
        assert resp.param_count == 0
        assert resp.message_type == 3

    def test_response_with_parameters(self):
        """Test Response with parameters."""
        params = b'\x00\x01\x02\x03'
        resp = Response(handle=42, status_code=0, param_count=1, parameters=params)
        assert resp.handle == 42
        assert resp.parameters == params

    def test_response_encoded_length(self):
        """Test Response encoded length calculation."""
        resp = Response(handle=1, status_code=0, param_count=0)
        assert resp.encoded_length() == 10

        params = b'\x00\x01\x02\x03'
        resp2 = Response(handle=1, status_code=0, param_count=1, parameters=params)
        # 10 + (1 * 4) = 14
        assert resp2.encoded_length() == 14


class TestCommand:
    """Test Command PDU encoding."""

    def test_command_creation(self):
        """Test Command can be created."""
        cmd = Command(target=100, method_level=1, method_index=1, param_count=0, parameters=None)
        assert cmd.target == 100
        assert cmd.method_level == 1
        assert cmd.method_index == 1
        assert cmd.param_count == 0

    def test_command_encoded_length(self):
        """Test Command encoded length."""
        cmd = Command(target=100, method_level=1, method_index=1, param_count=0, parameters=None)
        # Base length is 17
        assert cmd.encoded_length() == 17


class TestMessageEncoding:
    """Test message encoding functions."""

    def test_calculate_message_length(self):
        """Test message length calculation."""
        ka = KeepAlive(5000)
        length = calculate_message_length([ka])
        # Header (10) + KeepAlive (2)
        assert length == 12

    def test_calculate_message_length_multiple_pdus(self):
        """Test message length with multiple PDUs."""
        ka1 = KeepAlive(5000)
        ka2 = KeepAlive(5000)
        length = calculate_message_length([ka1, ka2])
        # Header (10) + 2 * KeepAlive (2 each)
        assert length == 14

    def test_calculate_message_length_mixed_types_raises(self):
        """Test that mixing PDU types raises error."""
        ka = KeepAlive(5000)
        resp = Response(handle=1, status_code=0, param_count=0)
        # Different message types should raise
        with pytest.raises(ValueError):
            calculate_message_length([ka, resp])

    def test_encode_message_to_keepalive(self):
        """Test encoding a message with KeepAlive."""
        ka = KeepAlive(5000)
        dst = bytearray(1024)
        pos = encode_message_to(dst, 0, [ka])

        # Should write header + 2 bytes for keepalive
        assert pos > 10
        # Check sync byte
        assert dst[0] == 0x3B


class TestMessageDecoding:
    """Test message decoding functions."""

    def test_decode_message_insufficient_data(self):
        """Test decode with insufficient data returns -1."""
        data = bytearray(b'\x3b')  # Just sync byte, not enough
        ret = []
        result = decode_message(data, 0, ret)
        assert result == -1

    def test_decode_message_bad_sync(self):
        """Test decode with bad sync byte raises ValueError."""
        data = bytearray(20)
        data[0] = 0x00  # Wrong sync byte
        ret = []
        with pytest.raises(ValueError, match='Bad sync'):
            decode_message(data, 0, ret)

    def test_decode_keepalive_roundtrip(self):
        """Test encode and decode KeepAlive roundtrip."""
        # Encode
        ka = KeepAlive(5000)
        dst = bytearray(1024)
        encode_message_to(dst, 0, [ka])

        # Decode
        ret = []
        pos = decode_message(dst, 0, ret)

        assert pos > 0
        assert len(ret) == 1
        assert isinstance(ret[0], KeepAlive)
        assert ret[0].time == 5000

    def test_decode_response_roundtrip(self):
        """Test encode and decode Response roundtrip."""
        # Encode
        resp = Response(handle=42, status_code=0, param_count=0)
        dst = bytearray(1024)
        encode_message_to(dst, 0, [resp])

        # Decode
        ret = []
        pos = decode_message(dst, 0, ret)

        assert pos > 0
        assert len(ret) == 1
        assert isinstance(ret[0], Response)
        assert ret[0].handle == 42
        assert ret[0].status_code == 0
