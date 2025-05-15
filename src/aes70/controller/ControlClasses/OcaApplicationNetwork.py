from ...OCP1.OcaApplicationNetworkCommand import OcaApplicationNetworkCommand
from ...OCP1.OcaApplicationNetworkState import OcaApplicationNetworkState
from ...OCP1.OcaBlob import OcaBlob
from ...OCP1.OcaList import OcaList
from ...OCP1.OcaNetworkSystemInterfaceDescriptor import OcaNetworkSystemInterfaceDescriptor
from ...OCP1.OcaString import OcaString
from ...OCP1.OcaUint16 import OcaUint16
from ...OCP1.OcaUint32 import OcaUint32
from ..make_control_class import make_control_class
from .OcaRoot import OcaRoot

# Abstract base class from which the application network classes inherit.
# @extends OcaRoot
# @class OcaApplicationNetwork
OcaApplicationNetwork = make_control_class(
    'OcaApplicationNetwork',
    2,
    '\u0001\u0004',
    1,
    OcaRoot,
    [
        ['GetLabel', 2, 1, [], [OcaString]],
        ['SetLabel', 2, 2, [OcaString], []],
        ['GetOwner', 2, 3, [], [OcaUint32]],
        ['GetServiceID', 2, 4, [], [OcaBlob]],
        ['SetServiceID', 2, 5, [OcaBlob], []],
        ['GetSystemInterfaces', 2, 6, [], [OcaList(OcaNetworkSystemInterfaceDescriptor)]],
        ['SetSystemInterfaces', 2, 7, [OcaList(OcaNetworkSystemInterfaceDescriptor)], []],
        ['GetState', 2, 8, [], [OcaApplicationNetworkState]],
        ['GetErrorCode', 2, 9, [], [OcaUint16]],
        ['Control', 2, 10, [OcaApplicationNetworkCommand], []],
        ['GetPath', 2, 11, [], [OcaList(OcaString), OcaList(OcaUint32)]],
    ],
    [
      ['Label', [OcaString], 2, 1, False, True, None],
      ['Owner', [OcaUint32], 2, 2, False, True, None],
      ['ServiceID', [OcaBlob], 2, 3, False, False, None],
      ['SystemInterfaces', [OcaList(OcaNetworkSystemInterfaceDescriptor)], 2, 4, False, False, None],
      ['State', [OcaApplicationNetworkState], 2, 5, False, False, None],
      ['ErrorCode', [OcaUint16], 2, 6, False, False, None],
    ],
    []
)

# Gets the network's user-specified label. Return status indicates whether the
# operation was successful.
#
# @method OcaApplicationNetwork#GetLabel
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the network's user-specified label. Return status indicates whether the
# operation was successful.
#
# @method OcaApplicationNetwork#SetLabel
# @param {str} Label
#
# @returns {Promise<None>}
# Gets the ONo of this network's containing block. Return status indicates
# whether the operation was successful.
#
# @method OcaApplicationNetwork#GetOwner
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the network's IDAdvertised. Return status indicates whether the operation
# was successful.
#
# @method OcaApplicationNetwork#GetServiceID
# @returns {Promise<bytes>}
#   A promise which resolves to a single value of type ``bytes``.
# Sets the network's IDAdvertised. Return status indicates whether the operation
# was successful.
#
# @method OcaApplicationNetwork#SetServiceID
# @param {bytes} Name
#
# @returns {Promise<None>}
# Retrieves the list of this network's system interface descriptor. Return
# status indicates whether the list was successfully retrieved.
#
# @method OcaApplicationNetwork#GetSystemInterfaces
# @returns {Promise<list[OcaNetworkSystemInterfaceDescriptor]>}
#   A promise which resolves to a single value of type ``list[OcaNetworkSystemInterfaceDescriptor]``.
# Sets the network's System Interface Descriptor(s). Return status indicates
# whether the operation was successful. Optional method; System Interface
# Descriptor may be set at construction time.
#
# @method OcaApplicationNetwork#SetSystemInterfaces
# @param {list[IOcaNetworkSystemInterfaceDescriptor]} Descriptors
#
# @returns {Promise<None>}
# Retrieves the network's state. Return status indicates whether the status was
# successfully retrieved.
#
# @method OcaApplicationNetwork#GetState
# @returns {Promise<OcaApplicationNetworkState>}
#   A promise which resolves to a single value of type :class:`OcaApplicationNetworkState`.
# Retrieves the most recent error code. Return status indicates whether the
# operation was successful. Note that a second parameter 'Reset' is removed in
# v02 of this class.
#
# @method OcaApplicationNetwork#GetErrorCode
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Control the application network. Return value indicates success of command
# execution.
#
# @method OcaApplicationNetwork#Control
# @param {OcaApplicationNetworkCommand} Command
#
# @returns {Promise<None>}
# Returns path from given object down to root. The return value indicates
# whether the operation succeeded.
# The return values of this method are
#
# - NamePath of type ``list[str]``
# - ONoPath of type ``list[int]``
#
# @method OcaApplicationNetwork#GetPath
# @returns {Promise<Arguments[list[str],list[int]]>}
# This event is emitted when the property ``ServiceID`` changes in the remote object.
# The property ``ServiceID`` is described in the AES70 standard as follows.
# Name or GUID that this device publishes in the network's directory/discovery
# system to designate the services offered via this application network object.
# This may or may not be the same as the device's host name, if any. For data
# network types that have host names (e.g. IP networks), the authoritative copy
# of the host name is in the system interface ID.
#
# @member {PropertyEvent<bytes>} OcaApplicationNetwork#OnServiceIDChanged
# This event is emitted when the property ``SystemInterfaces`` changes in the remote object.
# The property ``SystemInterfaces`` is described in the AES70 standard as follows.
# Collection of identifiers of system interface descriptor(s) used by the
# network. A "system interface" is the system service through which network
# traffic passes into and out of the device -- e.g. a socket. The descriptor
# format is system and network dependent; for OCA purposes, it is maintained as
# a variable-length blob which the protocol does not inspect.
#
# @member {PropertyEvent<list[OcaNetworkSystemInterfaceDescriptor]>} OcaApplicationNetwork#OnSystemInterfacesChanged
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# Operational state of the network.
#
# @member {PropertyEvent<OcaApplicationNetworkState>} OcaApplicationNetwork#OnStateChanged
# This event is emitted when the property ``ErrorCode`` changes in the remote object.
# The property ``ErrorCode`` is described in the AES70 standard as follows.
# Most recent error code. 0=no error.
#
# @member {PropertyEvent<int>} OcaApplicationNetwork#OnErrorCodeChanged
