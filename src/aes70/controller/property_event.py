from .base_event import BaseEvent
import logging

logger = logging.getLogger(__name__)

"""
 * Class used to represent property changes.
 * When this event fires, event handlers will be called with
 * the new value, the :class:`OcaPropertyChangeType` and
 * the :class:`OcaPropertyID` of the property.
 *
 * @extends BaseEvent
"""
class PropertyEvent(BaseEvent):
    def __init__(self, object, id, propertyType):
        super().__init__(object, id, propertyType)
        def callback(args):
            id_arg, dataView, changeType = args
            if (id_arg.DefLevel != self.id.DefLevel or
                id_arg.PropertyIndex != self.id.PropertyIndex):
                return

            value = propertyType[0].decodeFrom(dataView, 0)[1]

            for callback in self.handlers:
                try:
                    callback(object, value, changeType, id_arg)
                except Exception as e:
                    logger.error(e)
        self.callback = callback

    def do_subscribe(self):
        return self.object.OnPropertyChanged.subscribe(self.callback)

    def do_unsubscribe(self, callback):
        return self.object.OnPropertyChanged.unsubscribe(self.callback)
