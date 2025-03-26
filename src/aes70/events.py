from typing import Callable, Dict, Set

class Events:
    def __init__(self):
        self.event_handlers: Dict[str, Set[Callable]] = {}

    def emit(self, name: str, *args):
        handlers = self.event_handlers.get(name)
        if handlers:
            # Todo we should perform some kind of locking to prevent handlers changing during iteration.
            for cb in handlers.copy():
                try:
                    cb(self, *args)
                except Exception as e:
                    print(f"ERROR when calling {cb}: {e}")

    def on(self, name: str, cb: Callable):
        handlers = self.event_handlers.get(name)
        if not handlers:
            self.event_handlers[name] = handlers = set()
        handlers.add(cb)

    def add_event_listener(self, name: str, cb: Callable):
        self.on(name, cb)

    def remove_event_listener(self, name: str, cb: Callable):
        handlers = self.event_handlers.get(name)
        if not handlers or cb not in handlers:
            raise ValueError("remove_event_listeners(): not installed.")
        handlers.remove(cb)

    def remove_all_event_listeners(self):
        # Todo we should perform some kind of locking to prevent handlers changing during iteration in emit.
        self.event_handlers.clear()


