"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaSinkConnector import IOcaMediaSinkConnector, OcaMediaSinkConnector


class IOcaMediaSinkConnectorChangedEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The media source connector for which the changed event holds (i.e. that is
    # added, deleted or changed).
    SinkConnector: IOcaMediaSinkConnector
    # Indicates what type of change occurred. Only ItemAdded, ItemChanged and
    # ItemDeleted can be used in this event data.
    ChangeType: int
    # Indicates which element(s) of the connector changed. If the connector is
    # added or deleted, all bits in this bitset shall be set.
    ChangedElement: int


class OcaMediaSinkConnectorChangedEventData(IOcaMediaSinkConnectorChangedEventData):
    """
    #
    @class OcaMediaSinkConnectorChangedEventData
    """
    def __init__(self, SinkConnector: OcaMediaSinkConnector, ChangeType: int, ChangedElement: int):
        # The media source connector for which the changed event holds (i.e.
        # that is added, deleted or changed).
        self.SinkConnector: OcaMediaSinkConnector = SinkConnector
        # Indicates what type of change occurred. Only ItemAdded, ItemChanged
        # and ItemDeleted can be used in this event data.
        self.ChangeType: int = ChangeType
        # Indicates which element(s) of the connector changed. If the connector
        # is added or deleted, all bits in this bitset shall be set.
        self.ChangedElement: int = ChangedElement