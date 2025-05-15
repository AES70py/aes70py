"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaPropertyID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Level in tree of class which defines this property (1=root)
    DefLevel: int
    # Index of the property (in the class description).
    PropertyIndex: int


class OcaPropertyID(IOcaPropertyID):
    """
    # Representation of an OCA property ID. A class may define at most 255
    # properties of its own. Additional properties may be inherited, so the
    # total number may exceed 255.
    @class OcaPropertyID
    """
    def __init__(self, DefLevel: int, PropertyIndex: int):
        # Level in tree of class which defines this property (1=root)
        self.DefLevel: int = DefLevel
        # Index of the property (in the class description).
        self.PropertyIndex: int = PropertyIndex