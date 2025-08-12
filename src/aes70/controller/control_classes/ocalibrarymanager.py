from ...ocp1.ocalibraryidentifier import OcaLibraryIdentifier
from ...ocp1.ocalibvolidentifier import OcaLibVolIdentifier
from ...ocp1.ocalibvoltype import OcaLibVolType
from ...ocp1.ocalist import OcaList
from ...ocp1.ocauint16 import OcaUint16
from ...ocp1.ocauint32 import OcaUint32
from ..make_control_class import make_control_class
from .ocamanager import OcaManager

# Optional manager for handling device presets -- Patch and ParamSet libraries.
#
#  - May be instantiated once in any device.
#
#  - If instantiated, object number must be 8.
#
#
# @extends OcaManager
# @class OcaLibraryManager
OcaLibraryManager = make_control_class(
    'OcaLibraryManager',
    3,
    '\u0001\u0003\b',
    2,
    OcaManager,
    [
        ['AddLibrary', 3, 1, [OcaLibVolType], [OcaLibraryIdentifier]],
        ['DeleteLibrary', 3, 2, [OcaUint32], []],
        ['GetLibraryCount', 3, 3, [OcaLibVolType], [OcaUint16]],
        ['GetLibraryList', 3, 4, [OcaLibVolType], [OcaList(OcaLibraryIdentifier)]],
        ['GetCurrentPatch', 3, 5, [], [OcaLibVolIdentifier]],
        ['ApplyPatch', 3, 6, [OcaLibVolIdentifier], []],
    ],
    [
      ['Libraries', [OcaList(OcaLibraryIdentifier)], 3, 1, False, False, None],
      ['CurrentPatch', [OcaLibVolIdentifier], 3, 2, False, False, None],
    ],
    []
)

# Adds a library to the device. Return value indicates whether the library was
# successfully added.
#
# @method OcaLibraryManager#AddLibrary
# @param {IOcaLibVolType} Type
#
# @returns {Promise<OcaLibraryIdentifier>}
#   A promise which resolves to a single value of type :class:`OcaLibraryIdentifier`.
# Deletes a library from the device.
#
# @method OcaLibraryManager#DeleteLibrary
# @param {int} ID
#
# @returns {Promise<None>}
# Returns the number of libraries of the given type that are instantiated in the
# device..
#
# @method OcaLibraryManager#GetLibraryCount
# @param {IOcaLibVolType} Type
#
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Returns the list of object numbers of libraries of libraries of the given type
# that are instantiated in the device.
#
# @method OcaLibraryManager#GetLibraryList
# @param {IOcaLibVolType} Type
#
# @returns {Promise<list[OcaLibraryIdentifier]>}
#   A promise which resolves to a single value of type ``list[OcaLibraryIdentifier]``.
# Return the identifier of the most recently applied patch. The return value
# indicates whether the method succeeded.
#
# @method OcaLibraryManager#GetCurrentPatch
# @returns {Promise<OcaLibVolIdentifier>}
#   A promise which resolves to a single value of type :class:`OcaLibVolIdentifier`.
# Apply a patch to the device.
#
# @method OcaLibraryManager#ApplyPatch
# @param {IOcaLibVolIdentifier} ID
#
# @returns {Promise<None>}
# This event is emitted when the property ``Libraries`` changes in the remote object.
# The property ``Libraries`` is described in the AES70 standard as follows.
# List of identifiers of all libraries in the device.
#
# @member {PropertyEvent<list[OcaLibraryIdentifier]>} OcaLibraryManager#OnLibrariesChanged
# This event is emitted when the property ``CurrentPatch`` changes in the remote object.
# The property ``CurrentPatch`` is described in the AES70 standard as follows.
# Library volume identifier of the most-recently applied patch in this device.
# Changing the value of this property applies the patch represented by the new
# value.
#
# @member {PropertyEvent<OcaLibVolIdentifier>} OcaLibraryManager#OnCurrentPatchChanged
