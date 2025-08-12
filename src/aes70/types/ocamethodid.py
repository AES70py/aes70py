"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaMethodID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Level in tree of class which defines this method (1=root)
    DefLevel: int
    # Index of the method (in the class description).
    MethodIndex: int


class OcaMethodID(IOcaMethodID):
    """
    # Representation of an OCA method ID. A class may define at most 255 methods
    # of its own. Additional methods may be inherited, so the total number may
    # exceed 255.
    @class OcaMethodID
    """
    def __init__(self, DefLevel: int, MethodIndex: int):
        # Level in tree of class which defines this method (1=root)
        self.DefLevel: int = DefLevel
        # Index of the method (in the class description).
        self.MethodIndex: int = MethodIndex