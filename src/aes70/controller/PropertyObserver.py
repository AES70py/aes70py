from arguments import Arguments
from observe_property import observeProperty

class PropertyObserver:
    def __init__(self, o, propertyName, cacheSubscriptions):
        self.o = o
        self.propertyName = propertyName
        self.cacheSubscriptions = cacheSubscriptions
        self.property = o.get_properties().find_property(propertyName)
        self._subscribers = []
        self._currentValue = None
        self._unsubscribe = None

        if not self.property:
            raise Exception(f"Could not find property {propertyName} in {o.ClassName}")

    def callSubscriber(self, cb, changeIndex):
        try:
            cb(True, self._currentValue, changeIndex)
        except Exception as error:
            print('Subscriber to', self, 'threw and exception', error)

    def subscribe(self, callback):
        self._subscribers.append(callback)

        if self._unsubscribe is None:
            self._unsubscribe = observeProperty(
                self.o,
                self.property,
                lambda ok, result, changeIndex: self._handle_observe(ok, result, changeIndex)
            )
        elif self._currentValue is not None:
            self.callSubscriber(callback, None)

        def unsubscribe():
            self._subscribers = list(filter(lambda entry: entry != callback, self._subscribers))
            if self.cacheSubscriptions:
                return
            if not self._subscribers:
                self.unsubscribeAll()
        return unsubscribe

    def _handle_observe(self, ok, result, changeIndex):
        if ok:
            self._currentValue = result
            subscribers = self._subscribers
            if not subscribers:
                self.unsubscribeAll()
            for cb in subscribers:
                self.callSubscriber(cb, changeIndex)

    def subscribeReturnValue(self, index, callback):
        return self.subscribe(lambda ok, value, changeIndex: self._handle_subscribe_return(index, callback, ok, value, changeIndex))

    def _handle_subscribe_return(self, index, callback, ok, value, changeIndex):
        if not ok:
            callback(ok, value)
        else:
            if changeIndex >= 0 and changeIndex != index:
                return
            if isinstance(value, Arguments):
                callback(True, value.item(index))
            else:
                callback(False, Exception(f"Cannot index {value} with {index}."))

    def subscribeCurrent(self, callback):
        return self.subscribeReturnValue(0, callback)

    def subscribeMin(self, callback):
        return self.subscribeReturnValue(1, callback)

    def subscribeMax(self, callback):
        return self.subscribeReturnValue(2, callback)

    def subscribeValue(self, callback):
        return self.subscribe(lambda ok, value, changeIndex: self._handle_subscribe_value(callback, ok, value, changeIndex))

    def _handle_subscribe_value(self, callback, ok, value, changeIndex):
        if ok:
            if isinstance(value, Arguments):
                if changeIndex > 0:
                    return
                callback(ok, value.item(0))
            else:
                callback(ok, value)
        else:
            callback(ok, value)

    def unsubscribeAll(self):
        self._subscribers = []
        self._currentValue = None
        cleanup = self._unsubscribe
        if cleanup:
            try:
                cleanup()
            except Exception as error:
                print('Unsubscribe in', self, 'threw an exception', error)

    def dispose(self):
        self.unsubscribeAll()
