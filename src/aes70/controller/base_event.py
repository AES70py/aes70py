from typing import Callable, List, Any, Optional
from aes70.types.ocaevent import OcaEvent
import logging

logger = logging.getLogger(__name__)

class EventSubscriber:
    def __init__(self, callback: Callable, failure_callback: Optional[Callable] = None):
        self.callback = callback
        self.failure_callback = failure_callback

    def emit(self, ctx: Any, results: List[Any]):
        try:
            self.callback(*results)
        except Exception as error:
            logger.error(f'Exception thrown by event handler: {error}')

    def emit_error(self, ctx: Any, error: Exception):
        if self.failure_callback:
            try:
                self.failure_callback(error)
            except Exception as e:
                logger.error(f'Exception thrown by error event handler: {e}')
        else:
            logger.warning(f'No handler for error: {error}')

class BaseEvent:
    def __init__(self, obj: Any, id: int, argument_types: List[type]):
        self.object = obj
        self.id = id
        self.subscribers: List[EventSubscriber] = []
        self.result = None
        self.argument_types = argument_types

    def has_subscribers(self) -> bool:
        return len(self.subscribers) > 0

    def emit(self, results: List[Any]):
        for subscriber in self.subscribers:
            subscriber.emit(self.object, results)

    def emit_error(self, error: Exception):
        for subscriber in self.subscribers:
            subscriber.emit_error(self.object, error)
        self.subscribers.clear()

    def get_oca_event(self) -> OcaEvent:
        return OcaEvent(self.object.ObjectNumber, self.id)

    def do_subscribe(self):
        pass

    def do_unsubscribe(self):
        pass

    def _remove_subscriber(self, index: int):
        if self.subscribers:
            self.subscribers.pop(index)
            self.do_unsubscribe()

    def subscribe(self, callback: Callable, failure_callback: Optional[Callable] = None) -> Callable:
        subscriber = EventSubscriber(callback, failure_callback)
        self.subscribers.append(subscriber)

        if len(self.subscribers) == 1:
            self.do_subscribe()

        def unsubscribe():
            try:
                index = self.subscribers.index(subscriber)
                self._remove_subscriber(index)
            except ValueError:
                pass

        return unsubscribe

    def unsubscribe(self, callback: Callable) -> bool:
        for i, subscriber in enumerate(self.subscribers):
            if subscriber.callback == callback:
                self._remove_subscriber(i)
                return True
        raise Exception('Subscriber does not exist.')

    def dispose(self):
        self.subscribers.clear()
        if self.subscribers:
            try:
                self.do_unsubscribe()
            except Exception:
                pass



