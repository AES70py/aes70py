from .event import Event
from .property_event import PropertyEvent
from .property_sync import PropertySync
from .properties import Properties
from ..ocp1.commandrrq import CommandRrq
from ..ocp1.ocaeventid import OcaEventId
from aes70.types.ocapropertyid import OcaPropertyID
from ..ocp1.encoded_arguments import EncodedArguments
from ..ocp1.make_encoder import makeEncoder
from .property import Property

def createPropertySync(control_class):
    o = object.__new__(PropertySync)  # Equivalent to Object.create(PropertySync.prototype)
    blue_print = object.__new__(control_class)  # Equivalent to Object.create(control_class.prototype)

    index = 0

    # Iterate over each property returned by control_class.get_properties()
    for prop in control_class.get_properties():
        has_setter = bool(prop.setter(blue_print, True))
        has_getter = bool(prop.getter(blue_print, True))

        def make_getter(i):
            def getter(self):
                return self.values[i]
            return getter

        def make_setter(setter):
            def setter_func(self, val):
                setter(self.o, val)
                return val
            return setter_func

        if not has_getter:
            continue

        # Create property descriptor using Python's property
        if has_setter:
            prop_descriptor = property(make_getter(index), make_setter(prop.setter(blue_print, True)))
        else:
            prop_descriptor = property(make_getter(index))
        setattr(o, prop.name, prop_descriptor)
        index += 1

    # Define the constructor function
    def __init__(self, o_arg):
        self.init(o_arg)

    # Copy all attributes from object o into a dictionary for the class
    class_dict = dict(o.__dict__)
    class_dict['__init__'] = __init__
    PropertySyncConstructor = type('PropertySyncConstructor', (object,), class_dict)
    return PropertySyncConstructor

# method = [ name, level, index, argumentTypes, returnTypes, aliases ]
def implement_method(cls, method):
    if not method or not len(method):
        return

    name, level, index, argumentTypes, returnTypes = method
    if len(method) == 6:
        aliases = method[5]
    else:
        aliases = None

    def method_func(self, *args):
        argumentCount = len(argumentTypes)
        callback = None

        # If there are too few arguments, this might mean
        #
        # - that some of them use the default encoding (e.g. 0)
        # - that the method signature has change in the AES70 version
        #   used
        #
        # this is why we do not error here, yet.
        if argumentCount < len(args):
            if (argumentCount + 1 == len(args)) and callable(args[argumentCount]):
                callback = args[argumentCount]
                args = args[:argumentCount]
        cmd = CommandRrq(self.ono, level, index, argumentCount, EncodedArguments(argumentTypes, args))
        return self.device.send_command(cmd, returnTypes, callback)

    setattr(cls, name, method_func)

    if aliases:
        for alias in aliases:
            def alias_func(self, *args, _name=name):
                return getattr(self, _name)(*args)
            setattr(cls, alias, alias_func)

# event = [ name, level, index, argumentTypes ]
def implement_event(cls, event):
    name, level, index, argumentTypes = event

    def get_event(self):
        ev_name = '_On' + name
        event_val = getattr(self, ev_name, None)
        if event_val:
            return event_val
        event_instance = Event(self, OcaEventId(level, index), argumentTypes)
        setattr(self, ev_name, event_instance)
        return event_instance
    setattr(cls, 'On' + name, property(get_event))

def property_event_name(propertyName):
    return 'On' + propertyName + 'Changed'

def implement_property_event(cls, prop):
    if prop.static:
        return
    if prop.name == 'ObjectNumber':
        return

    event_name = property_event_name(prop.name)

    #print('Event name: ' + event_name)
    def get_prop_event(self):
        ev_name = '_' + event_name
        event_val = getattr(self, ev_name, None)
        if event_val:
            return event_val
        event_instance = PropertyEvent(self, OcaPropertyID(prop.level, prop.index), prop.type)
        setattr(self, ev_name, event_instance)
        return event_instance
    setattr(cls, event_name, property(get_prop_event))

    if prop.aliases:
        for alias in prop.aliases:
            ev_name_alias = property_event_name(alias)
            if hasattr(cls, ev_name_alias):
                continue
            def get_alias(self, _event_name=event_name):
                return getattr(self, _event_name)
            setattr(cls, ev_name_alias, property(get_alias))

def make_property(o):
    if isinstance(o, Property):
        return o

    if isinstance(o, list):
        if not isinstance(o[1], object) or type(o[1]) in (int, float, str, bool):
            o[1] = makeEncoder(o[1])
        #print('making property from ' + str(o[1]))
        return Property(*o)

    raise Exception('Bad property.')

"""
Creates a control class. This is an internal API, use define_custom_class
for a simpler API to be used when defining custom classes.

@param {String} name - The name of this control class.
@param {number} level - The level in the class hierachy.
@param {String} class_id - The class ID.
@param {number} class_version - The class version.
@param {Function} base - Class to extend.
@param {Array} methods - List of methods.
@param {Array} properties - List of properties.
@param {Array} events - List of events.
"""
def make_control_class(name, level, class_id, class_version, baseclass, methods, properties, events):
    property_sync = None
    _properties = None
    #print('making control class ' + name + " from " + str(baseclass))

    properties = list(map(lambda v: make_property(v), properties))

    class ControlClass(baseclass):
        ClassID = class_id
        ClassVersion = class_version
        ClassName = name

# TODO it would be helpful if these string representations were more helpful.
        def __str__(self):
            return '<Control Class ' + self.ClassName + '>'

        def __repr__(self):
            return '<Control Class ' + self.ClassName + '>'


        def get_properties(self):
            nonlocal _properties
            if _properties is None:
                _properties = Properties(properties, level, baseclass.get_properties(self))
            return _properties

        @staticmethod
        def GetPropertySync():
            nonlocal property_sync
            if property_sync is None:
                property_sync = createPropertySync(ControlClass)
            return property_sync

        def __init__(self, device, ono):
            super(ControlClass, self).__init__(device, ono)
            for i in range(0, len(properties)):
                prop = properties[i]
                setattr(self, '_On' + prop.name + 'Changed', None)
            for i in range(0, len(events)):
                ev = events[i]
                setattr(self, '_On' + ev[0], None)

        def Dispose(self):
            super(ControlClass, self).Dispose()
            for i in range(0, len(properties)):
                prop = properties[i]
                event_instance = getattr(self, '_On' + prop.name + 'Changed')
                if event_instance:
                    event_instance.Dispose()
            for i in range(0, len(events)):
                ev = events[i]
                event_instance = getattr(self, '_On' + ev[0])
                if event_instance:
                    event_instance.Dispose()

    cls = ControlClass

    for i in range(0, len(methods)):
        implement_method(cls, methods[i])

    for i in range(0, len(properties)):
        implement_property_event(cls, properties[i])

    for i in range(0, len(events)):
        implement_event(cls, events[i])

    return cls
