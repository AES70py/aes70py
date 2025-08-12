"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorStatus import IOcaMediaConnectorStatus, OcaMediaConnectorStatus


class IOcaMediaConnectorStatusChangedEventData:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # The status that has changed.
    ConnectorStatus: IOcaMediaConnectorStatus


class OcaMediaConnectorStatusChangedEventData(IOcaMediaConnectorStatusChangedEventData):
    """
    #
    @class OcaMediaConnectorStatusChangedEventData
    """
    def __init__(self, ConnectorStatus: OcaMediaConnectorStatus):
        # The status that has changed.
        self.ConnectorStatus: OcaMediaConnectorStatus = ConnectorStatus