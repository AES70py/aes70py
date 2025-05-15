"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaSourceConnector import IOcaMediaSourceConnector, OcaMediaSourceConnector
from .OcaPropertyChangeType import OcaPropertyChangeType


class IOcaMediaSourceConnectorChangedEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The media source connector for which the changed event holds (i.e. that is
    # added, deleted or changed).
    SourceConnector: IOcaMediaSourceConnector
    # Indicates what type of change occurred. Only ItemAdded, ItemChanged and
    # ItemDeleted can be used in this event data.
    ChangeType: OcaPropertyChangeType
    # Indicates which element(s) of the connector changed. If the connector is
    # added or deleted, all bits in this bitset shall be set.
    ChangedElement: int


class OcaMediaSourceConnectorChangedEventData(IOcaMediaSourceConnectorChangedEventData):
    """
    #
    @class OcaMediaSourceConnectorChangedEventData
    """
    def __init__(self, SourceConnector: OcaMediaSourceConnector, ChangeType: OcaPropertyChangeType, ChangedElement: int):
        # The media source connector for which the changed event holds (i.e.
        # that is added, deleted or changed).
        self.SourceConnector: OcaMediaSourceConnector = SourceConnector
        # Indicates what type of change occurred. Only ItemAdded, ItemChanged
        # and ItemDeleted can be used in this event data.
        self.ChangeType: OcaPropertyChangeType = ChangeType
        # Indicates which element(s) of the connector changed. If the connector
        # is added or deleted, all bits in this bitset shall be set.
        self.ChangedElement: int = ChangedElement