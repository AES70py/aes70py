import logging
from arguments import Arguments

# /**
#  * Observe a property in an object.
#  *
#  * The callback function is called when a property value or change is received. In
#  * that case the callback is called with the arguments `true, value, changeIndex`. When an
#  * error occurs, e.g. when fetching the initial property value using the corresponding
#  * getter, the callback is called with arguments `false, Error`.
#  *
#  * The meaning of the changeIndex argument is meaningful in situations where a property has
#  * associated min and max value. In that situation the value received by the callback is
#  * the return value of the getter, which is an instance of Arguments. When either the property
#  * itself or min/max changes, the changeIndex will be the corresponding index in the arguments
#  * list. If the property has no min and max or when the initial value is returned from the
#  * getter, the value of changeIndex is undefined.
#  *
#  * @param {ObjectBase} o The remote object.
#  * @param {string|Property} property
#  * @param {Function} callback The callback function
#  * @returns An unsubscribe/cleanup function.
#  */
def observeProperty(o, property, callback):
    propertyName = None

    if isinstance(property, str):
        propertyName = property
        property = o.get_properties().find_property(propertyName)
        if not property:
            raise Exception(f"Could not find property {propertyName} in {o.ClassName}")
    else:
        propertyName = property.name

    if getattr(property, 'static', False):
        callback(True, getattr(o, propertyName))
        return lambda: None

    lastValue = None

    def notify(changeIndex=None):
        try:
            callback(True, lastValue, changeIndex)
        except Exception as error:
            logging.error('Subscriber %s to property %s in %s threw exception %s', callback, propertyName, o, error)

    def eventCallback(value, changeType, eventId):
        nonlocal lastValue
        if lastValue is None:
            return
        if changeType.value == 1:  # OcaPropertyChangeType.CurrentChanged
            if isinstance(lastValue, Arguments):
                lastValue.values[0] = value
                notify(0)
                return
            else:
                lastValue = value
                notify()
                return
        elif changeType.value == 2:  # OcaPropertyChangeType.MinChanged
            if isinstance(lastValue, Arguments):
                lastValue.values[1] = value
                notify(1)
                return
        elif changeType.value == 3:  # OcaPropertyChangeType.MaxChanged
            if isinstance(lastValue, Arguments):
                lastValue.values[2] = value
                notify(2)
                return
        else:
            # No supported.
            pass
        logging.warning('Unhandled event %s %s %s', value, changeType, eventId)

    active = True
    event = property.event(o)
    getter = property.getter(o)
    if not getter:
        raise Exception(f"Not getter found for {propertyName} in {o.ClassName}")

    if event:
        p = event.subscribe(eventCallback)
        if p:
            def catch_callback(error):
                nonlocal active
                if not active:
                    return
                callback(False, error)
            p.catch(catch_callback)

    def getterCallback(ok, result):
        nonlocal active, lastValue
        if not active:
            return
        if not ok:
            callback(False, result)
        else:
            lastValue = result
            notify()

    getter(getterCallback)

    def unsubscribe():
        nonlocal active
        active = False
        if event:
            event.unsubscribe(eventCallback)

    return unsubscribe
