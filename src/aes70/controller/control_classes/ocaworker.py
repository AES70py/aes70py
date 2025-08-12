from ...ocp1.ocaboolean import OcaBoolean
from ...ocp1.ocafloat32 import OcaFloat32
from ...ocp1.ocalist import OcaList
from ...ocp1.ocaport import OcaPort
from ...ocp1.ocaportid import OcaPortID
from ...ocp1.ocaportmode import OcaPortMode
from ...ocp1.ocastring import OcaString
from ...ocp1.ocauint32 import OcaUint32
from ..make_control_class import make_control_class
from .ocaroot import OcaRoot

# Abstract base class for classes that represent the device's application and
# support functions.
# @extends OcaRoot
# @class OcaWorker
OcaWorker = make_control_class(
    'OcaWorker',
    2,
    '\u0001\u0001',
    2,
    OcaRoot,
    [
        ['GetEnabled', 2, 1, [], [OcaBoolean]],
        ['SetEnabled', 2, 2, [OcaBoolean], []],
        ['AddPort', 2, 3, [OcaString, OcaPortMode], [OcaPortID]],
        ['DeletePort', 2, 4, [OcaPortID], []],
        ['GetPorts', 2, 5, [], [OcaList(OcaPort)]],
        ['GetPortName', 2, 6, [OcaPortID], [OcaString]],
        ['SetPortName', 2, 7, [OcaPortID, OcaString], []],
        ['GetLabel', 2, 8, [], [OcaString]],
        ['SetLabel', 2, 9, [OcaString], []],
        ['GetOwner', 2, 10, [], [OcaUint32]],
        ['GetLatency', 2, 11, [], [OcaFloat32]],
        ['SetLatency', 2, 12, [OcaFloat32], []],
        ['GetPath', 2, 13, [], [OcaList(OcaString), OcaList(OcaUint32)]],
    ],
    [
      ['Enabled', [OcaBoolean], 2, 1, False, False, None],
      ['Ports', [OcaList(OcaPort)], 2, 2, False, False, None],
      ['Label', [OcaString], 2, 3, False, False, None],
      ['Owner', [OcaUint32], 2, 4, False, False, None],
      ['Latency', [OcaFloat32], 2, 5, False, False, None],
    ],
    []
)

# Gets the value of the Enabled property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaWorker#GetEnabled
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# Sets the value of the Enabled property. The return value indicates whether the
# property was successfully set.
#
# @method OcaWorker#SetEnabled
# @param {bool} enabled
#
# @returns {Promise<None>}
# Adds an input or output port.. The return value indicates whether the port was
# successfully added.
#
# @method OcaWorker#AddPort
# @param {str} Label
# @param {int} Mode
#
# @returns {Promise<OcaPortID>}
#   A promise which resolves to a single value of type :class:`OcaPortID`.
# Deletes an input or output port.. The return value indicates whether the port
# was successfully deleted.
#
# @method OcaWorker#DeletePort
# @param {IOcaPortID} ID
#
# @returns {Promise<None>}
# Gets the list of ports owned by the Worker object. The return value indicates
# whether the list was successfully retrieved.
#
# @method OcaWorker#GetPorts
# @returns {Promise<list[OcaPort]>}
#   A promise which resolves to a single value of type ``list[OcaPort]``.
# Gets the name of the designated port. The return value indicates whether the
# name was successfully retrieved.
#
# @method OcaWorker#GetPortName
# @param {IOcaPortID} PortID
#
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the name of the designated port. The return value indicates whether the
# name was successfully set.
#
# @method OcaWorker#SetPortName
# @param {IOcaPortID} PortID
# @param {str} Name
#
# @returns {Promise<None>}
# Gets the value of the Label property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaWorker#GetLabel
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the value of the Label property. The return value indicates whether the
# property was successfully set.
#
# @method OcaWorker#SetLabel
# @param {str} label
#
# @returns {Promise<None>}
# Gets the value of the Owner property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaWorker#GetOwner
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the value of the Latency property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaWorker#GetLatency
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the Latency property. The return value indicates whether the
# property was successfully set.
#
# @method OcaWorker#SetLatency
# @param {int} latency
#
# @returns {Promise<None>}
# Returns path from the given object down to root. The return value indicates
# whether the operation succeeded. Added in version 2.
# The return values of this method are
#
# - NamePath of type ``list[str]``
# - ONoPath of type ``list[int]``
#
# @method OcaWorker#GetPath
# @returns {Promise<Arguments[list[str],list[int]]>}
# This event is emitted when the property ``Enabled`` changes in the remote object.
# The property ``Enabled`` is described in the AES70 standard as follows.
# Read/write property that indicates whether the worker object is enabled in the
# device. If an object is disabled it cannot be used by the application. Note
# that the behavior of a disabled object depends on the object itself (e.g. a
# disabled chime generator is silent, a disabled equalizer is flat, etc.).
#
# @member {PropertyEvent<bool>} OcaWorker#OnEnabledChanged
# This event is emitted when the property ``Ports`` changes in the remote object.
# The property ``Ports`` is described in the AES70 standard as follows.
# The list of (input and output) OCA ports the worker object has. Note that a
# worker object can have no ports (in which case the list is empty).
#
# @member {PropertyEvent<list[OcaPort]>} OcaWorker#OnPortsChanged
# This event is emitted when the property ``Label`` changes in the remote object.
# The property ``Label`` is described in the AES70 standard as follows.
# Specific label of the worker. Can be used to provide human readable
# information about the worker. The label can be get and set over the network.
#
# @member {PropertyEvent<str>} OcaWorker#OnLabelChanged
# This event is emitted when the property ``Owner`` changes in the remote object.
# The property ``Owner`` is described in the AES70 standard as follows.
# Object number of block that contains this worker.
#
# @member {PropertyEvent<int>} OcaWorker#OnOwnerChanged
# This event is emitted when the property ``Latency`` changes in the remote object.
# The property ``Latency`` is described in the AES70 standard as follows.
# Processing latency of this object. Optional. Readonly or readwrite, depending
# on implementation.
#
# @member {PropertyEvent<int>} OcaWorker#OnLatencyChanged
