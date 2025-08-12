from ...ocp1.ocablob import OcaBlob
from ...ocp1.ocalist import OcaList
from ...ocp1.ocanetworkcontrolprotocol import OcaNetworkControlProtocol
from ...ocp1.ocanetworklinktype import OcaNetworkLinkType
from ...ocp1.ocanetworkmediaprotocol import OcaNetworkMediaProtocol
from ...ocp1.ocanetworkstatistics import OcaNetworkStatistics
from ...ocp1.ocanetworkstatus import OcaNetworkStatus
from ...ocp1.ocanetworksysteminterfaceid import OcaNetworkSystemInterfaceID
from ...ocp1.ocauint32 import OcaUint32
from ..make_control_class import make_control_class
from .ocaagent import OcaAgent

# **DEPRECATED CLASS** *Replaced by class* **OcaControlNetwork ***in version 3
# of Connection Management (CM3)* Abstract base class for defining network
# classes to which this device belongs. This class is to be used for control and
# monitoring networks only. For media transport networks, and for networks that
# combine media transport and control, the **OcaStreamNetwork** class should be
# used instead.
# @extends OcaAgent
# @class OcaNetwork
OcaNetwork = make_control_class(
    'OcaNetwork',
    3,
    '\u0001\u0002\u0001',
    2,
    OcaAgent,
    [
        ['GetLinkType', 3, 1, [], [OcaNetworkLinkType]],
        ['GetIDAdvertised', 3, 2, [], [OcaBlob]],
        ['SetIDAdvertised', 3, 3, [OcaBlob], []],
        ['GetControlProtocol', 3, 4, [], [OcaNetworkControlProtocol]],
        ['GetMediaProtocol', 3, 5, [], [OcaNetworkMediaProtocol]],
        ['GetStatus', 3, 6, [], [OcaNetworkStatus]],
        ['GetStatistics', 3, 7, [], [OcaNetworkStatistics]],
        ['ResetStatistics', 3, 8, [], []],
        ['GetSystemInterfaces', 3, 9, [], [OcaList(OcaNetworkSystemInterfaceID)]],
        ['SetSystemInterfaces', 3, 10, [OcaList(OcaNetworkSystemInterfaceID)], []],
        ['GetMediaPorts', 3, 11, [], [OcaList(OcaUint32)]],
        ['Startup', 3, 12, [], []],
        ['Shutdown', 3, 13, [], []],
    ],
    [
      ['LinkType', [OcaNetworkLinkType], 3, 1, True, False, None],
      ['IDAdvertised', [OcaBlob], 3, 2, False, False, None],
      ['ControlProtocol', [OcaNetworkControlProtocol], 3, 3, False, False, None],
      ['MediaProtocol', [OcaNetworkMediaProtocol], 3, 4, False, False, None],
      ['Status', [OcaNetworkStatus], 3, 5, False, False, None],
      ['SystemInterfaces', [OcaList(OcaNetworkSystemInterfaceID)], 3, 6, False, False, None],
      ['MediaPorts', [OcaList(OcaUint32)], 3, 7, False, False, None],
      ['Statistics', [OcaNetworkStatistics], 3, 8, False, False, None],
    ],
    []
)

# Gets the network's link type (wired Ethernet, USB, etc.). Return status
# indicates whether the operation was successful.
#
# @method OcaNetwork#GetLinkType
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the network's IDAdvertised. Return status indicates whether the operation
# was successful.
#
# @method OcaNetwork#GetIDAdvertised
# @returns {Promise<bytes>}
#   A promise which resolves to a single value of type ``bytes``.
# Sets the network's IDAdvertised. Return status indicates whether the operation
# was successful.
#
# @method OcaNetwork#SetIDAdvertised
# @param {bytes} Name
#
# @returns {Promise<None>}
# Gets the network's ControlProtocol property. Return status indicates whether
# the operation was successful.
#
# @method OcaNetwork#GetControlProtocol
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the network's MediaProtocol property. This is a deprecated method that
# always returns the value NONE.
#
# @method OcaNetwork#GetMediaProtocol
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Retrieves the network's status. Return status indicates whether the status was
# successfully retrieved.
#
# @method OcaNetwork#GetStatus
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Retrieves network error statistics counter values. Return status indicates
# whether the values were successfully retrieved.
#
# @method OcaNetwork#GetStatistics
# @returns {Promise<OcaNetworkStatistics>}
#   A promise which resolves to a single value of type :class:`OcaNetworkStatistics`.
# Resets network error statistics counters. Return status indicates whether the
# counters were successfully reset.
#
# @method OcaNetwork#ResetStatistics
# @returns {Promise<None>}
# Gets the list of system interface IDs that this network is using. Return
# status indicates success of the operation.
#
# @method OcaNetwork#GetSystemInterfaces
# @returns {Promise<list[OcaNetworkSystemInterfaceID]>}
#   A promise which resolves to a single value of type ``list[OcaNetworkSystemInterfaceID]``.
# Sets the list of system interface IDs that this network will use. Return
# status indicates success of the operation. This method is not implemented by
# all network implementations.
#
# @method OcaNetwork#SetSystemInterfaces
# @param {list[IOcaNetworkSystemInterfaceID]} Interfaces
#
# @returns {Promise<None>}
# Deprecated method. Always returns status INVALID_REQUEST. Media transport is
# now managed by the class **OcaStreamNetwork.**
#
# @method OcaNetwork#GetMediaPorts
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Start up this network.
#
# @method OcaNetwork#Startup
# @returns {Promise<None>}
# Shut down this network.
#
# @method OcaNetwork#Shutdown
# @returns {Promise<None>}
# This event is emitted when the property ``IDAdvertised`` changes in the remote object.
# The property ``IDAdvertised`` is described in the AES70 standard as follows.
# ID by which this network object is known on the network, i.e. the name or GUID
# that this network object publishes in the network's directory/discovery
# system. As of OCA 1.4, this description has been clarified to indicate this
# property is the registered service name, which may or may not be the same as
# the device's host name, if any. For data network types that have host names
# (e.g. IP networks), the authoritative copy of the host name is in the system
# interface ID.
#
# @member {PropertyEvent<bytes>} OcaNetwork#OnIDAdvertisedChanged
# This event is emitted when the property ``ControlProtocol`` changes in the remote object.
# The property ``ControlProtocol`` is described in the AES70 standard as follows.
# Type of control protocol used by the network (OCAnn) or NONE if this network
# is not used for control.
#
# @member {PropertyEvent<int>} OcaNetwork#OnControlProtocolChanged
# This event is emitted when the property ``MediaProtocol`` changes in the remote object.
# The property ``MediaProtocol`` is described in the AES70 standard as follows.
# Deprecated property. Always has value NONE. Media transport is managed by the
# **OcaStreamNetwork** class.
#
# @member {PropertyEvent<int>} OcaNetwork#OnMediaProtocolChanged
# This event is emitted when the property ``Status`` changes in the remote object.
# The property ``Status`` is described in the AES70 standard as follows.
# Operational status of the network.
#
# @member {PropertyEvent<int>} OcaNetwork#OnStatusChanged
# This event is emitted when the property ``SystemInterfaces`` changes in the remote object.
# The property ``SystemInterfaces`` is described in the AES70 standard as follows.
# Collection of identifiers of system interface(s) used by the network. A
# "system interface" is the system service through which network traffic passes
# into and out of the device -- e.g. a socket. The identifier format is system
# and network dependent; for OCA purposes, it is maintained as a variable-length
# blob which the protocol does not inspect.
#
# @member {PropertyEvent<list[OcaNetworkSystemInterfaceID]>} OcaNetwork#OnSystemInterfacesChanged
# This event is emitted when the property ``MediaPorts`` changes in the remote object.
# The property ``MediaPorts`` is described in the AES70 standard as follows.
# Deprecated property. Always is empty. Media transport is now managed by the
# class **OcaStreamNetwork.**
#
# @member {PropertyEvent<list[int]>} OcaNetwork#OnMediaPortsChanged
# This event is emitted when the property ``Statistics`` changes in the remote object.
# The property ``Statistics`` is described in the AES70 standard as follows.
# Error statistics for this network
#
# @member {PropertyEvent<OcaNetworkStatistics>} OcaNetwork#OnStatisticsChanged
