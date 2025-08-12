# Required dependencies and imports
from typing import Any

def hasOwnProperty(o, name):
    return name in o

def Enum(values):
    names = None
    def getName(value):
        nonlocal names
        if names is None:
            names = {}
            for name in values:
                if not hasOwnProperty(values, name):
                    continue
                names[values[name]] = name
        return names.get(value)

    def getValue(name):
        if name in values:
            return values[name]

    blueprints = None

    def setBlueprint(value, o):
        nonlocal blueprints
        if blueprints is None:
            blueprints = {}
        blueprints[value] = o

    # Descriptor to emulate JavaScript static property getter behavior on the class.
    class EnumDescriptor:
        def __init__(self, name):
            self.name = name
        def __get__(self, instance, owner):
            return owner(values[self.name])
        def __str__(self):
            return 'EnumDescriptor:'+self.name

    class result:
        @property
        def isEnum(self):
            return True

        def __new__(cls, value):
            # If value is a string, retrieve the corresponding enum using the class attribute.
            if isinstance(value, str):
                if value not in values:
                    raise Exception('No such enum value.')
                return getattr(cls, value)
            # If a blueprint already exists for this value, return it.
            if blueprints is not None and value in blueprints:
                return blueprints[value]
            # Create a new instance and store its value.
            instance = super(result, cls).__new__(cls)
            instance._value = value
            setBlueprint(value, instance)
            return instance

        def __init__(self, value):
            # Constructor does nothing further since initialization is handled in __new__
            pass

        @property
        def name(self):
            return getName(self._value)

        @property
        def value(self):
            return self._value

        def __str__(self):
            return getName(self._value)

        @staticmethod
        def getName(value):
            name = getName(value)
            if name is None:
                raise Exception('No such enum value.')
            return name

        @staticmethod
        def getValue(name):
            value = getValue(name)
            if value is None:
                raise Exception('No such enum value.')
            return value

        @staticmethod
        def values():
            return values

    # Define static properties on the result class corresponding to each name in values.
    for name in values:
        if not hasOwnProperty(values, name):
            continue
        descriptor = EnumDescriptor(name)
        setattr(result, name, descriptor)

    return result
