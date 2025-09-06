"""
This file is part of aes70py.
This file has been generated.
"""
from .ocamediacoding import IOcaMediaCoding, OcaMediaCoding
from .ocamediaconnection import IOcaMediaConnection, OcaMediaConnection
from .ocaportid import IOcaPortID, OcaPortID


class IOcaMediaSourceConnector:
    # Since this is an interface, no implementation is provided.
    # Properties to be implemented by subclasses:
    # Internal ID.
    IDInternal: int
    # Public name of connector. May be published to the media transport network,
    # depending on the type of network.
    IDExternal: str
    # Descriptor of the stream connection to this connector. If there is no
    # stream connected to this controller, (i.e. property Connected = FALSE),
    # the value of this property is undefined.
    Connection: IOcaMediaConnection
    # List of codings available for this connector.
    AvailableCodings: list[IOcaMediaCoding]
    # Number of pins in this connector.
    PinCount: int
    # Map of stream pins (source channels) to OCA ports (input ports) of the
    # owning **OcaMediaNetwork** object. This defines what source channels are
    # sent to the network. A pin is identified by an OcaUint16 with value
    # 1..MaxPinCount. Not having a certain pin identifier in this map means that
    # the pin is empty (i.e. not carrying a source channel).
    ChannelPinMap: dict[int, IOcaPortID]
    # Alignment level of the interface. Note that the dBFS value is referenced
    # to the *interface's* fullscale value, not to device's internal fullscale
    # value.
    AlignmentLevel: int
    # Coding currently used by this connector.
    CurrentCoding: IOcaMediaCoding


class OcaMediaSourceConnector(IOcaMediaSourceConnector):
    """
    # Media source (i.e. output) connector. Connects to an outbound stream.
    # Collected by **OcaMediaTransportNetwork**.
    @class OcaMediaSourceConnector
    """
    def __init__(self, IDInternal: int, IDExternal: str, Connection: OcaMediaConnection, AvailableCodings: list[OcaMediaCoding], PinCount: int, ChannelPinMap: dict[int, OcaPortID], AlignmentLevel: int, CurrentCoding: OcaMediaCoding):
        # Internal ID.
        self.IDInternal: int = IDInternal
        # Public name of connector. May be published to the media transport
        # network, depending on the type of network.
        self.IDExternal: str = IDExternal
        # Descriptor of the stream connection to this connector. If there is no
        # stream connected to this controller, (i.e. property Connected =
        # FALSE), the value of this property is undefined.
        self.Connection: OcaMediaConnection = Connection
        # List of codings available for this connector.
        self.AvailableCodings: list[OcaMediaCoding] = AvailableCodings
        # Number of pins in this connector.
        self.PinCount: int = PinCount
        # Map of stream pins (source channels) to OCA ports (input ports) of the
        # owning **OcaMediaNetwork** object. This defines what source channels
        # are sent to the network. A pin is identified by an OcaUint16 with
        # value 1..MaxPinCount. Not having a certain pin identifier in this map
        # means that the pin is empty (i.e. not carrying a source channel).
        self.ChannelPinMap: dict[int, OcaPortID] = ChannelPinMap
        # Alignment level of the interface. Note that the dBFS value is
        # referenced to the *interface's* fullscale value, not to device's
        # internal fullscale value.
        self.AlignmentLevel: int = AlignmentLevel
        # Coding currently used by this connector.
        self.CurrentCoding: OcaMediaCoding = CurrentCoding
