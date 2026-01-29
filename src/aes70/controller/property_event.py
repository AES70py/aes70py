from .base_event import BaseEvent
import logging

logger = logging.getLogger(__name__)

class PropertyEvent(BaseEvent):
    def __init__(self, object, id, propertyType):
        super().__init__(object, id, propertyType)
        
        def callback(propertyId, data, changeType):
            # TODO must be a better way to express this arg
            # propertyId = arg[0]
            # data = arg[1]
            # changeType = arg[2]

            if (propertyId.DefLevel != self.id.DefLevel or
                propertyId.PropertyIndex != self.id.PropertyIndex):
                return

            value = propertyType[0].decode_from(data, 0)[1]
            self.emit([value, changeType, propertyId])
        
        def error_callback(error):
            print("from error_callback")
            self.emit_error(error)
        
        self.callback = callback
        self.error_callback = error_callback
        self._unsubscribe = None

    def do_subscribe(self):
        print("[INFO] Subscribing to property event")
        self._unsubscribe = self.object.OnPropertyChanged.subscribe(
            self.callback,
            self.error_callback
        )

    def do_unsubscribe(self):
        if self._unsubscribe:
            unsubscribe = self._unsubscribe
            self._unsubscribe = None
            try:
                unsubscribe()
            except Exception as error:
                logger.error(f'Unsubscribing PropertyChanged event failed: {error}')
