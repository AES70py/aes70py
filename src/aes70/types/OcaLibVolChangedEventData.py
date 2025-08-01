"""
This file is part of aes70py.
This file has been generated.
"""


class IOcaLibVolChangedEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ID of library volume that changed.
    VolumeID: int
    # Type of change : Will be either itemChanged, itemAdded, or itemDeleted.
    ChangeType: int


class OcaLibVolChangedEventData(IOcaLibVolChangedEventData):
    """
    # Event data for the **OcaLibVolChanged** event, which signals a change in
    # an **OcaLibrary.Volumes** property.
    @class OcaLibVolChangedEventData
    """
    def __init__(self, VolumeID: int, ChangeType: int):
        # ID of library volume that changed.
        self.VolumeID: int = VolumeID
        # Type of change : Will be either itemChanged, itemAdded, or
        # itemDeleted.
        self.ChangeType: int = ChangeType