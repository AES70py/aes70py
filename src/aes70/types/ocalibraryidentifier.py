"""
This file is part of aes70py.
This file has been generated.
"""
from .ocalibvoltype import IOcaLibVolType, OcaLibVolType


class IOcaLibraryIdentifier:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Type of the library (= type of its volumes)
    Type: IOcaLibVolType
    # Object number of library.
    ONo: int


class OcaLibraryIdentifier(IOcaLibraryIdentifier):
    """
    # Full identifier (type + object number) of Library (i.e. of an
    # **OcaLibrary** instance)
    @class OcaLibraryIdentifier
    """
    def __init__(self, Type: OcaLibVolType, ONo: int):
        # Type of the library (= type of its volumes)
        self.Type: OcaLibVolType = Type
        # Object number of library.
        self.ONo: int = ONo