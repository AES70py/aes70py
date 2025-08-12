"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaPortID import IOcaPortID, OcaPortID


class IOcaPort:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Object number of the object that owns the port.
    Owner: int
    # ID of the port.
    ID: IOcaPortID
    # Port ID of the port.
    Name: str


class OcaPort(IOcaPort):
    """
    # Representation of an OCA (input or output) port that is used in the signal
    # path representation of an OCA device.
    @class OcaPort
    """
    def __init__(self, Owner: int, ID: OcaPortID, Name: str):
        # Object number of the object that owns the port.
        self.Owner: int = Owner
        # ID of the port.
        self.ID: OcaPortID = ID
        # Port ID of the port.
        self.Name: str = Name