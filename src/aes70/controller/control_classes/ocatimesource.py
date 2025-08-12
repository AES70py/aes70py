from ...ocp1.ocastring import OcaString
from ...ocp1.ocatimeprotocol import OcaTimeProtocol
from ...ocp1.ocatimereferencetype import OcaTimeReferenceType
from ...ocp1.ocatimesourceavailability import OcaTimeSourceAvailability
from ...ocp1.ocatimesourcesyncstatus import OcaTimeSourceSyncStatus
from ..make_control_class import make_control_class
from .ocaagent import OcaAgent

# A time source, internal or external. See RFC 7273 for a detailed discussion of
# time sources.
# @extends OcaAgent
# @class OcaTimeSource
OcaTimeSource = make_control_class(
    'OcaTimeSource',
    3,
    '\u0001\u0002\u0010',
    1,
    OcaAgent,
    [
        ['GetAvailability', 3, 1, [], [OcaTimeSourceAvailability]],
        ['GetProtocol', 3, 2, [], [OcaTimeProtocol]],
        ['SetProtocol', 3, 3, [OcaTimeProtocol], []],
        ['GetParameters', 3, 4, [], [OcaString]],
        ['SetParameters', 3, 5, [OcaString], []],
        ['GetReferenceType', 3, 6, [], [OcaTimeReferenceType]],
        ['SetReferenceType', 3, 7, [OcaTimeReferenceType], []],
        ['GetReferenceID', 3, 8, [], [OcaString]],
        ['SetReferenceID', 3, 9, [OcaString], []],
        ['GetSyncStatus', 3, 10, [], [OcaTimeSourceSyncStatus]],
        ['Reset', 3, 11, [], []],
    ],
    [
      ['Availability', [OcaTimeSourceAvailability], 3, 1, False, False, None],
      ['Protocol', [OcaTimeProtocol], 3, 2, False, False, None],
      ['Parameters', [OcaString], 3, 3, False, False, None],
      ['ReferenceType', [OcaTimeReferenceType], 3, 4, False, False, None],
      ['ReferenceID', [OcaString], 3, 5, False, False, None],
      ['SyncStatus', [OcaTimeSourceSyncStatus], 3, 6, False, False, None],
    ],
    []
)

# Gets the value of the **Availability** property. The return value indicates
# whether the value was successfully retrieved.
#
# @method OcaTimeSource#GetAvailability
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the value of the **Protocol** property. The return value indicates
# whether the value was successfully retrieved.
#
# @method OcaTimeSource#GetProtocol
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the **Protocol** property. The return value indicates
# whether the value was successfully set.
#
# @method OcaTimeSource#SetProtocol
# @param {int} Protocol
#
# @returns {Promise<None>}
# Gets the value of the **Parameters** property. The return value indicates
# whether the value was successfully retrieved.
#
# @method OcaTimeSource#GetParameters
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the value of the **Parameters** property. The return value indicates
# whether the value was successfully set. Optional method, may not be supported
# in all implementations.
#
# @method OcaTimeSource#SetParameters
# @param {str} Parameters
#
# @returns {Promise<None>}
# Gets the time reference type. The return value indicates whether the value was
# successfully retrieved.
#
# @method OcaTimeSource#GetReferenceType
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the time reference type. The return value indicates whether the value was
# successfully set. Optional method, may not be supported in all
# implementations.
#
# @method OcaTimeSource#SetReferenceType
# @param {int} ReferenceType
#
# @returns {Promise<None>}
# Gets the timing source ID. The return value indicates whether the value was
# successfully retrieved. Optional method, not required for all time reference
# types.
#
# @method OcaTimeSource#GetReferenceID
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the time reference ID. The return value indicates whether the ID was
# successfully set. Optional method, not required for all time reference types.
#
# @method OcaTimeSource#SetReferenceID
# @param {str} ID
#
# @returns {Promise<None>}
# Gets the synchronization status of this time source. The return value
# indicates whether the value was successfully retrieved.
#
# @method OcaTimeSource#GetSyncStatus
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Resets this time source. Initiates a new synchronization sequence. The return
# value indicates whether the reset was successful.
#
# @method OcaTimeSource#Reset
# @returns {Promise<None>}
# This event is emitted when the property ``Availability`` changes in the remote object.
# The property ``Availability`` is described in the AES70 standard as follows.
# Availability of this time source.
#
# @member {PropertyEvent<int>} OcaTimeSource#OnAvailabilityChanged
# This event is emitted when the property ``Protocol`` changes in the remote object.
# The property ``Protocol`` is described in the AES70 standard as follows.
# Time transport protocol used by this time source
#
# @member {PropertyEvent<int>} OcaTimeSource#OnProtocolChanged
# This event is emitted when the property ``Parameters`` changes in the remote object.
# The property ``Parameters`` is described in the AES70 standard as follows.
# Parameters (identifiers, modifiers, etc.) for this time source . Content is an
# SDP timestamp reference specification as defined in RFC7273, section 4.8.
#
# @member {PropertyEvent<str>} OcaTimeSource#OnParametersChanged
# This event is emitted when the property ``ReferenceType`` changes in the remote object.
# The property ``ReferenceType`` is described in the AES70 standard as follows.
# Type of time reference to which this time source is synced, if any.
#
# @member {PropertyEvent<int>} OcaTimeSource#OnReferenceTypeChanged
# This event is emitted when the property ``ReferenceID`` changes in the remote object.
# The property ``ReferenceID`` is described in the AES70 standard as follows.
# Identifier of reference to which this time source is synced, if any. Not
# needed for all reference types.
#
# @member {PropertyEvent<str>} OcaTimeSource#OnReferenceIDChanged
# This event is emitted when the property ``SyncStatus`` changes in the remote object.
# The property ``SyncStatus`` is described in the AES70 standard as follows.
# Synchronization status of this time source.
#
# @member {PropertyEvent<int>} OcaTimeSource#OnSyncStatusChanged
