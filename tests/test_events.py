"""
Tests for the Events class.
"""
import pytest
from aes70.events import Events


class TestEvents:
    """Test the Events base class functionality."""

    def test_event_registration(self):
        """Test that event handlers can be registered."""
        events = Events()
        called = False

        def handler(event_source, *args):
            nonlocal called
            called = True

        events.on('test', handler)
        events.emit('test')
        assert called is True

    def test_event_with_args(self):
        """Test that events can pass arguments to handlers."""
        events = Events()
        received_args = []

        def handler(event_source, *args):
            received_args.extend(args)

        events.on('test', handler)
        events.emit('test', 1, 2, 3)
        assert received_args == [1, 2, 3]

    def test_multiple_handlers(self):
        """Test that multiple handlers can be registered for same event."""
        events = Events()
        call_count = 0

        def handler1(event_source, *args):
            nonlocal call_count
            call_count += 1

        def handler2(event_source, *args):
            nonlocal call_count
            call_count += 1

        events.on('test', handler1)
        events.on('test', handler2)
        events.emit('test')
        assert call_count == 2

    def test_remove_event_listener(self):
        """Test that event handlers can be removed."""
        events = Events()
        called = False

        def handler(event_source, *args):
            nonlocal called
            called = True

        events.on('test', handler)
        events.remove_event_listener('test', handler)
        events.emit('test')
        assert called is False

    def test_remove_all_listeners(self):
        """Test that all listeners can be removed at once."""
        events = Events()
        call_count = 0

        def handler1(event_source, *args):
            nonlocal call_count
            call_count += 1

        def handler2(event_source, *args):
            nonlocal call_count
            call_count += 1

        events.on('test', handler1)
        events.on('test', handler2)
        events.remove_all_event_listeners()
        events.emit('test')
        assert call_count == 0

    def test_handler_error_caught(self):
        """Test that handler errors are caught and don't break other handlers."""
        events = Events()
        second_called = False

        def bad_handler(event_source, *args):
            raise ValueError("Test error")

        def good_handler(event_source, *args):
            nonlocal second_called
            second_called = True

        events.on('test', bad_handler)
        events.on('test', good_handler)
        # Should not raise despite bad_handler error
        events.emit('test')
        assert second_called is True

    def test_add_event_listener_alias(self):
        """Test that add_event_listener is an alias for on."""
        events = Events()
        called = False

        def handler(event_source, *args):
            nonlocal called
            called = True

        events.add_event_listener('test', handler)
        events.emit('test')
        assert called is True

    def test_no_handlers_no_error(self):
        """Test that emitting event with no handlers doesn't error."""
        events = Events()
        # Should not raise
        events.emit('nonexistent')

    def test_remove_nonexistent_handler_raises(self):
        """Test that removing a non-registered handler raises ValueError."""
        events = Events()

        def handler(event_source, *args):
            pass

        with pytest.raises(ValueError):
            events.remove_event_listener('test', handler)
