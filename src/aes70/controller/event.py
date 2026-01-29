from aes70.controller.base_event import BaseEvent
from logging import getLogger

logger = getLogger(__name__)

emptyBuffer = bytes()

class Event(BaseEvent):
    def __init__(self, object, id, argumentTypes):
        super().__init__(object, id, argumentTypes)
        
        def callback(ok, notification):
            if not ok:
                self.emit_error(notification)
                return

            if not self.has_subscribers():
                return

            if hasattr(notification, 'exception') and notification.exception:
                self.emit_error(Exception(f'Notification error: {notification.exception}'))
                return

            args = [None] * len(argumentTypes)
            data = memoryview(notification.parameters if notification.parameters is not None else emptyBuffer)

            pos = 0
            for i in range(len(argumentTypes)):
                pos, tmp = argumentTypes[i].decode_from(data, pos)
                args[i] = tmp

            self.emit(*args)
            
        self.callback = callback

    def do_subscribe(self):
        self.object.device.add_subscription(
            self.get_oca_event(),
            self.callback
        )

    def do_unsubscribe(self):
        self.object.device.remove_subscription(
            self.get_oca_event(),
            self.callback
        )
