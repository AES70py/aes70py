"""
This file is part of aes70py.
This file has been generated.
"""
from .OcaMediaConnectorState import OcaMediaConnectorState


class IOcaMediaConnectorStatus:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # ID of the connector for which this status is valid
    ConnectorID: int
    # Connector state
    State: OcaMediaConnectorState
    # Indicates what type of error the connector is in (only relevant if the
    # State is Fault).
    ErrorCode: int


class OcaMediaConnectorStatus(IOcaMediaConnectorStatus):
    """
    # Represents the current status of a media (source or sink) connector.
    @class OcaMediaConnectorStatus
    """
    def __init__(self, ConnectorID: int, State: OcaMediaConnectorState, ErrorCode: int):
        # ID of the connector for which this status is valid
        self.ConnectorID: int = ConnectorID
        # Connector state
        self.State: OcaMediaConnectorState = State
        # Indicates what type of error the connector is in (only relevant if the
        # State is Fault).
        self.ErrorCode: int = ErrorCode