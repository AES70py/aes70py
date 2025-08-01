"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaLibVolType import IOcaLibVolType, OcaLibVolType
from .OcaTimePTP import IOcaTimePTP, OcaTimePTP


class IOcaLibVolMetadata:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Name of library volume
    Name: str
    # Type of library volume
    VolType: IOcaLibVolType
    # Access mode of library volume - readonly or readwrite.
    Access: int
    # Version number of library volume.
    Version: int
    # Name of creator of library volume.
    Creator: str
    # Latest update timestamp.
    UpDate: IOcaTimePTP


class OcaLibVolMetadata(IOcaLibVolMetadata):
    """
    # Descriptor of a library volume. See **03 OcaLibrary** for explanation.
    @class OcaLibVolMetadata
    """
    def __init__(self, Name: str, VolType: OcaLibVolType, Access: int, Version: int, Creator: str, UpDate: OcaTimePTP):
        # Name of library volume
        self.Name: str = Name
        # Type of library volume
        self.VolType: OcaLibVolType = VolType
        # Access mode of library volume - readonly or readwrite.
        self.Access: int = Access
        # Version number of library volume.
        self.Version: int = Version
        # Name of creator of library volume.
        self.Creator: str = Creator
        # Latest update timestamp.
        self.UpDate: OcaTimePTP = UpDate