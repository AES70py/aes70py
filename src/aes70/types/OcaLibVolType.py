"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaLibVolType:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Unique identifier of organization that has authority over this library
    # volume type. A zero value indicates a standard library volume type defined
    # by the AES70 standard.
    Authority: bytes
    # ID of library volume type defined by given Authority. Value is unique
    # within the given Authority. If Authority=0, the values of this property
    # are given by enum **OcaLibVolStandardID.**
    ID: int


class OcaLibVolType(IOcaLibVolType):
    """
    # Globally unique identifier of a library type.
    @class OcaLibVolType
    """
    def __init__(self, Authority: bytes, ID: int):
        # Unique identifier of organization that has authority over this library
        # volume type. A zero value indicates a standard library volume type
        # defined by the AES70 standard.
        self.Authority: bytes = Authority
        # ID of library volume type defined by given Authority. Value is unique
        # within the given Authority. If Authority=0, the values of this
        # property are given by enum **OcaLibVolStandardID.**
        self.ID: int = ID