"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaClassAuthorityID:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Sentinel signifying an Authority ID
    Sentinel: int
    # Reserved, must be zero.
    Reserved: int
    # Authority's IEEE public Company ID (public CID) or IEEE Organizational
    # Unique Identifier (OUI), or the value zero, which signifies the Authority
    # of this AES70 standard.
    OrganizationID: bytes


class OcaClassAuthorityID(IOcaClassAuthorityID):
    """
    # Class authority identifier. Identifies the authority for a class's
    # definition.
    @class OcaClassAuthorityID
    """
    def __init__(self, Sentinel: int, Reserved: int, OrganizationID: bytes):
        # Sentinel signifying an Authority ID
        self.Sentinel: int = Sentinel
        # Reserved, must be zero.
        self.Reserved: int = Reserved
        # Authority's IEEE public Company ID (public CID) or IEEE Organizational
        # Unique Identifier (OUI), or the value zero, which signifies the
        # Authority of this AES70 standard.
        self.OrganizationID: bytes = OrganizationID