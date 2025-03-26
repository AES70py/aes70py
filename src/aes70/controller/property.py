from ..types.OcaPropertyId import OcaPropertyID
from promise import Promise
import logging

logger = logging.getLogger(__name__)

# Describes an AES70 property. Simplifies getting or setting properties
# and listening to property changes.
class Property:
    def __init__(self, name, type, level, index, readonly, is_static, aliases, accessorsa = []):
        self.name = name
        self.type = type
        self.level = level
        self.index = index
        self.readonly = readonly
        self.static = is_static
        self.aliases = aliases

        accessors = accessorsa
        if (not aliases) and (not accessors) and (not is_static):
            accessors = { 'get': 'Get' + name }
        self.accessors = accessors

    # Returns the OcaPropertyID of this property.
    def GetPropertyID(self):
        return OcaPropertyID(self.level, self.index)

    # Returns the name of this property.
    def GetName(self):
        return self.name

    # Returns the getter for this property in o.
    #
    # @param o - The remote object.
    # @param no_bind - If true, the returned function is not
    #                bound to the object o.
    # @returns The getter. If none could be found, None is returned.
    def getter(self, o, no_bind=False):
        name = self.name
        i = 0
        aliases = self.aliases
        accessors = self.accessors

        if accessors:
            get = accessors.get('get')
            if not get:
                return None

            fun = None

            if isinstance(get, str):
                fun = getattr(o, get, None)
            elif isinstance(get, dict):
                new_name = get.get('name')
                index = get.get('index')
                if index >= 0:
                    def fun(callback=None):
                        if callable(callback):
                            def inner(ok, result):
                                if ok:
                                    result = result.item(index)
                                callback(ok, result)
                            getattr(o, new_name)(inner)
                        else:
                            res = getattr(o, new_name)()
                            return res.then(lambda result: result.item(index))
                    # End of fun definition
                else:
                    fun = getattr(o, name, None)
            else:
                raise Exception("Unexpected accessor.")

            if not fun:
                return None

            return fun if no_bind else (fun.__get__(o, type(o)))

        while True:
            if self.static:
                c = type(o)
                v = getattr(c, name, None)
                if v is not None:
                    def bound_func(*args, **kwargs):
                        return Promise.resolve(v)
                    if no_bind:
                        return bound_func
                    else:
                        return bound_func
            else:
                fun = getattr(o, "Get" + name, None)
                if fun:
                    return fun if no_bind else (fun.__get__(o, type(o)))
            if aliases and i < len(aliases):
                name = aliases[i]
                i += 1
                continue
            break

        return None

    # Returns the setter for this property in o.
    #
    # @param o - The remote object.
    # @param no_bind - If true, the returned function is not
    #                bound to the object o.
    # @returns The setter. If none could be found, None is returned.
    def setter(self, o, no_bind=False):
        if self.readonly or self.static:
            return None

        name = self.name
        i = 0
        aliases = self.aliases

        while True:
            fun = getattr(o, "Set" + name, None)
            if fun:
                return fun if no_bind else (fun.__get__(o, type(o)))
            if aliases and i < len(aliases):
                name = aliases[i]
                i += 1
                continue
            break

        return None

    # Returns the event for this property in o.
    #
    # @returns The event.
    def event(self, o):
        name = self.name
        i = 0
        aliases = self.aliases

        while True:
            event = getattr(o, "On" + name + "Changed", None)
            if event:
                return event
            if aliases and i < len(aliases):
                name = aliases[i]
                i += 1
                continue
            break

        return None

    # Subscribe to changes of this property in o. If successful, the callback will be called at least
    # once with the initial value.
    #
    # @param o - The remote object.
    # @param cb - The callback.
    # @returns Returns true if the property could be subscribed.
    def subscribe(self, o, cb):
        event_obj = self.event(o)
        getter_func = self.getter(o)

        if event_obj:
            event_obj.subscribe(cb).catch(logger.error)

        if getter_func:
            getter_func().then(cb, logger.error)

        if event_obj:
            return event_obj

        return bool(getter_func)
