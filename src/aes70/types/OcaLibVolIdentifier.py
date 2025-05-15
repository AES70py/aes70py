"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaLibVolIdentifier:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Library that holds the LibVol in question.
    Library: int
    # ID of LibVol within the given library.
    ID: int


class OcaLibVolIdentifier(IOcaLibVolIdentifier):
    """
    # Unique identifier of a library volume within the device.
    @class OcaLibVolIdentifier
    """
    def __init__(self, Library: int, ID: int):
        # Library that holds the LibVol in question.
        self.Library: int = Library
        # ID of LibVol within the given library.
        self.ID: int = ID