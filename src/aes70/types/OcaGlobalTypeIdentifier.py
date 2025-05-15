"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaGlobalTypeIdentifier:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Unique identifier of organization that has authority over this reusable
    # block type. A zero value indicates a global type defined by the AES70
    # standard itself.
    Authority: bytes
    # ID of library volume type defined by given Authority. Value is unique
    # within the given Authority.
    ID: int


class OcaGlobalTypeIdentifier(IOcaGlobalTypeIdentifier):
    """
    # Globally unique identifier of something that belongs to an organization.
    @class OcaGlobalTypeIdentifier
    """
    def __init__(self, Authority: bytes, ID: int):
        # Unique identifier of organization that has authority over this
        # reusable block type. A zero value indicates a global type defined by
        # the AES70 standard itself.
        self.Authority: bytes = Authority
        # ID of library volume type defined by given Authority. Value is unique
        # within the given Authority.
        self.ID: int = ID