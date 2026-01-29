#!/usr/bin/env python3
"""
Test script to validate subscription functionality.
This performs a series of tests without requiring a real device.
"""

import asyncio
import sys
import traceback

def test_imports():
    """Test that all subscription-related imports work."""
    print("Testing imports...")
    try:
        from aes70.controller import tcp_connection
        from aes70.controller.remote_device import RemoteDevice, EventSubscription
        from aes70.controller.base_event import BaseEvent, EventSubscriber
        from aes70.controller.event import Event
        from aes70.controller.property_event import PropertyEvent
        from aes70.controller.control_classes.ocasubscriptionmanager import OcaSubscriptionManager
        from aes70.types.ocanotificationdeliverymode import OcaNotificationDeliveryMode
        print("✓ All imports successful")
        return True
    except Exception as e:
        print(f"✗ Import failed: {e}")
        traceback.print_exc()
        return False

def test_event_subscription_class():
    """Test EventSubscription class functionality."""
    print("\nTesting EventSubscription class...")
    try:
        from aes70.controller.remote_device import EventSubscription
        
        event = {"EmitterONo": 100, "EventID": {"DefLevel": 1, "EventIndex": 1}}
        
        def test_callback(ok, notification):
            pass
        
        sub = EventSubscription(event, test_callback)
        
        assert sub.version == 0, "Initial version should be 0"
        assert not sub.has_subscribers(), "Should have no subscribers initially"
        
        sub.add_callback(lambda ok, n: None)
        assert sub.has_subscribers(), "Should have subscribers after add"
        
        sub.version = 2
        assert sub.version == 2, "Version should be settable"
        
        print("✓ EventSubscription class works correctly")
        return True
    except Exception as e:
        print(f"✗ EventSubscription test failed: {e}")
        traceback.print_exc()
        return False

def test_event_subscriber_class():
    """Test EventSubscriber class functionality."""
    print("\nTesting EventSubscriber class...")
    try:
        from aes70.controller.base_event import EventSubscriber
        
        callback_called = []
        error_called = []
        
        def test_callback(*args):
            callback_called.append(args)
        
        def error_callback(error):
            error_called.append(error)
        
        subscriber = EventSubscriber(test_callback, error_callback)
        
        subscriber.emit(None, [1, 2, 3])
        assert len(callback_called) == 1, "Callback should be called once"
        assert callback_called[0] == (1, 2, 3), "Callback should receive correct args"
        
        test_error = Exception("test error")
        subscriber.emit_error(None, test_error)
        assert len(error_called) == 1, "Error callback should be called once"
        assert error_called[0] == test_error, "Error callback should receive error"
        
        print("✓ EventSubscriber class works correctly")
        return True
    except Exception as e:
        print(f"✗ EventSubscriber test failed: {e}")
        traceback.print_exc()
        return False

def test_base_event_subscribe():
    """Test BaseEvent subscribe/unsubscribe pattern."""
    print("\nTesting BaseEvent subscribe/unsubscribe...")
    try:
        from aes70.controller.base_event import BaseEvent
        
        class MockObject:
            ObjectNumber = 100
        
        event = BaseEvent(MockObject(), 1, [])
        
        callback_called = []
        def test_callback(*args):
            callback_called.append(args)
        
        unsubscribe = event.subscribe(test_callback)
        
        assert callable(unsubscribe), "subscribe should return a callable"
        assert event.has_subscribers(), "Should have subscribers"
        
        event.emit([1, 2, 3])
        assert len(callback_called) == 1, "Callback should be called"
        
        unsubscribe()
        assert not event.has_subscribers(), "Should have no subscribers after unsubscribe"
        
        event.emit([4, 5, 6])
        assert len(callback_called) == 1, "Callback should not be called after unsubscribe"
        
        print("✓ BaseEvent subscribe/unsubscribe works correctly")
        return True
    except Exception as e:
        print(f"✗ BaseEvent test failed: {e}")
        traceback.print_exc()
        return False

def test_subscription_manager_methods():
    """Test that OcaSubscriptionManager has the required methods."""
    print("\nTesting OcaSubscriptionManager methods...")
    try:
        from aes70.controller.control_classes.ocasubscriptionmanager import OcaSubscriptionManager
        
        required_methods = [
            'AddSubscription',
            'RemoveSubscription',
            'AddSubscription2',
            'RemoveSubscription2',
            'DisableNotifications',
            'ReEnableNotifications',
            'AddPropertyChangeSubscription',
            'RemovePropertyChangeSubscription',
        ]
        
        for method_name in required_methods:
            assert hasattr(OcaSubscriptionManager, method_name), \
                f"OcaSubscriptionManager should have {method_name} method"
        
        print("✓ OcaSubscriptionManager has all required methods")
        return True
    except Exception as e:
        print(f"✗ OcaSubscriptionManager test failed: {e}")
        traceback.print_exc()
        return False

def test_remote_device_initialization():
    """Test RemoteDevice subscription-related initialization."""
    print("\nTesting RemoteDevice initialization...")
    try:
        from aes70.controller.remote_device import RemoteDevice
        from aes70.controller.client_connection import ClientConnection
        
        class MockConnection(ClientConnection):
            def __init__(self):
                super().__init__({})
                self._closed = False
            
            def is_closed(self):
                return self._closed
            
            def write(self, buf):
                pass
        
        conn = MockConnection()
        device = RemoteDevice(conn)
        
        assert hasattr(device, 'SubscriptionManager'), "Should have SubscriptionManager"
        assert hasattr(device, 'subscriptions'), "Should have subscriptions dict"
        assert hasattr(device, '_supportsEV2'), "Should have _supportsEV2 flag"
        assert hasattr(device, '_checkEV2Promise'), "Should have _checkEV2Promise"
        assert hasattr(device, 'add_subscription'), "Should have add_subscription method"
        assert hasattr(device, 'remove_subscription'), "Should have remove_subscription method"
        
        assert device._supportsEV2 is None, "_supportsEV2 should be None initially"
        assert isinstance(device.subscriptions, dict), "subscriptions should be a dict"
        
        print("✓ RemoteDevice initialization correct")
        return True
    except Exception as e:
        print(f"✗ RemoteDevice test failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("=" * 60)
    print("AES70 Subscription Implementation Tests")
    print("=" * 60)
    
    tests = [
        test_imports,
        test_event_subscription_class,
        test_event_subscriber_class,
        test_base_event_subscribe,
        test_subscription_manager_methods,
        test_remote_device_initialization,
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Test Results: {passed}/{total} passed")
    
    if passed == total:
        print("✓ All tests passed!")
        return 0
    else:
        print(f"✗ {total - passed} test(s) failed")
        return 1

if __name__ == '__main__':
    sys.exit(main())
