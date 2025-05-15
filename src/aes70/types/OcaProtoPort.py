"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaProtoPortID import IOcaProtoPortID, OcaProtoPortID


class IOcaProtoPort:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Proto-object number of the proto-member that owns the proto-port. **The
    # value of 0 (zero) is special, and refers to the block itself, rather than
    # to any of its members.**
    Owner: int
    # ID of the proto-port.
    ProtoID: IOcaProtoPortID
    # Name of the proto-port.
    Name: str


class OcaProtoPort(IOcaProtoPort):
    """
    # Representation of an OCA (input or output) proto-port that is used in the
    # proto-signal path representation of an OCA device.
    @class OcaProtoPort
    """
    def __init__(self, Owner: int, ProtoID: OcaProtoPortID, Name: str):
        # Proto-object number of the proto-member that owns the proto-port.
        # **The value of 0 (zero) is special, and refers to the block itself,
        # rather than to any of its members.**
        self.Owner: int = Owner
        # ID of the proto-port.
        self.ProtoID: OcaProtoPortID = ProtoID
        # Name of the proto-port.
        self.Name: str = Name