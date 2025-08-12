import asyncio
from .arguments import Arguments
from ..types.ocapropertychangetype import OcaPropertyChangeType


class PropertySync:
    def init(self, o):
        self.o = o
        self.values = []
        self.synchronized = False
        self.subscriptions = []

    """
    * Starts synchronizing the properties in this object with the corresponding
    * ones in the remote instance.
    *
    * @returns {Promise<void>}
    """

    async def sync(self):
        if self.synchronized:
            return

        index = 0
        tasks = []

        # Iterate over all properties fetched from o.get_properties()
        for prop in self.o.get_properties():
            getter = prop.getter(self.o)

            if not getter:
                continue

            event = prop.event(self.o)

            # Definition of change_handler: updates the corresponding value when changeType matches
            def change_handler(idx, value, changeType):
                if changeType != OcaPropertyChangeType.CurrentChanged:
                    return
                try:
                    self.values[idx] = value
                except IndexError:
                    # Extend the list to the needed index
                    self.values.extend([None] * (idx - len(self.values)))
                    self.values.append(value)

            # Definition of get_handler: processes the value received from getter
            def get_handler(idx, value):
                if isinstance(value, Arguments):
                    value = value.item(0)
                try:
                    self.values[idx] = value
                except IndexError:
                    self.values.extend([None] * (idx - len(self.values)))
                    self.values.append(value)

            if event:
                # Bind change_handler with the current index
                cb = lambda value, changeType, idx=index: change_handler(idx, value, changeType)
                # NOTE: we do not want to wait for the promise to resolve
                # before storing this unsubscription handler because that
                # would have a potential race condition.
                self.subscriptions.append(lambda cb=cb, event=event: event.unsubscribe(cb))

                async def subscribe_task(ev, callback):
                    try:
                        await ev.subscribe(callback)
                    except Exception:
                        pass

                tasks.append(asyncio.create_task(subscribe_task(event, cb)))

            async def getter_task(get_func, idx):
                try:
                    value = await get_func()
                    get_handler(idx, value)
                except Exception:
                    pass

            tasks.append(asyncio.create_task(getter_task(getter, index)))

            index += 1

        await asyncio.gather(*tasks)

    """
    * Iterate over all properties.
    *
    * @param {Function} cb - Callback functions, Will be called with value and
    *                        property name as arguments.
    * @param {Object} ctx - The context to call the callback in. Defaults to
    *                       this.
    """

    def forEach(self, cb, ctx=None):
        index = 0

        if ctx is None:
            ctx = self

        for prop in self.o.get_properties():
            getter = prop.getter(self.o)

            if not getter:
                continue

            # In JavaScript, cb.call(ctx, value, prop.name) is used to bind 'this'.
            # Python does not support function binding in the same way; we directly call cb.
            cb(self.values[index], prop.name)
            index += 1

    """
    * Dispose of this object. Will unsubscribe all event handlers.
    """

    def Dispose(self):
        self.o = None
        if self.subscriptions:
            for cb in self.subscriptions:
                cb()
        self.subscriptions = None
