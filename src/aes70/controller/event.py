from aes70.controller.base_event import BaseEvent
from logging import getLogger

logger = getLogger(__name__)

emptyBuffer = bytes()

# /**
#  * Class used to represent all events specified by the OCA standard.
#  *
#  * @extends BaseEvent
#  */
class Event(BaseEvent):
    def __init__(self, object, id, argumentTypes):
        super().__init__(object, id, argumentTypes)
        # Using a closure to capture 'argumentTypes'
        def callback(notification):
            if not self.handlers or len(self.handlers) == 0:
                return

            args = [None] * len(argumentTypes)
            # Events without arguments have parameters = null
            data = memoryview(notification.parameters if notification.parameters is not None else emptyBuffer)

            pos = 0
            for i in range(len(argumentTypes)):
                # Each decodeFrom returns a tuple of (new pos, tmp)
                pos, tmp = argumentTypes[i].decodeFrom(data, pos)
                args[i] = tmp

            obj = self.object
            for cb in self.handlers:
                try:
                    # TODO figure out if we actually need this, as unbound functions
                    # no longer exist in python 3
                    # Simulate callback.apply(object, args)
                    # If cb is an unbound function, bind it to obj
                    #bound_cb = cb.__get__(obj, type(obj))
                    bound_cb = cb
                    bound_cb(*args)
                except Exception as e:
                    logger.error(e)
        self.callback = callback

    def do_subscribe(self):
        return self.object.device.add_subscription(
            self.get_oca_event(),
            self.callback
        )

# TODO this seems wrong wrt callback
    def do_unsubscribe(self, callback):
        return self.object.device.remove_subscription(
            self.get_oca_event(),
            self.callback
        )
