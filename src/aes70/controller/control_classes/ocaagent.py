from ...ocp1.ocalist import OcaList
from ...ocp1.ocastring import OcaString
from ...ocp1.ocauint32 import OcaUint32
from ..make_control_class import make_control_class
from .ocaroot import OcaRoot

# Abstract base class for defining agents.
# @extends OcaRoot
# @class OcaAgent
OcaAgent = make_control_class(
    'OcaAgent',
    2,
    '\u0001\u0002',
    2,
    OcaRoot,
    [
        ['GetLabel', 2, 1, [], [OcaString]],
        ['SetLabel', 2, 2, [OcaString], []],
        ['GetOwner', 2, 3, [], [OcaUint32]],
        ['GetPath', 2, 4, [], [OcaList(OcaString), OcaList(OcaUint32)]],
    ],
    [
      ['Label', [OcaString], 2, 1, False, False, None],
      ['Owner', [OcaUint32], 2, 2, False, False, None],
    ],
    []
)

# Gets the value of the Label property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaAgent#GetLabel
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Sets the value of the Label property. The return value indicates whether the
# property was successfully set.
#
# @method OcaAgent#SetLabel
# @param {str} Label
#
# @returns {Promise<None>}
# Gets the value of the Owner property. The return value indicates whether the
# property was successfully retrieved.
#
# @method OcaAgent#GetOwner
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Returns path from the given object down to root. The return value indicates
# whether the operation succeeded. Added in version 2.
# The return values of this method are
#
# - NamePath of type ``list[str]``
# - ONoPath of type ``list[int]``
#
# @method OcaAgent#GetPath
# @returns {Promise<Arguments[list[str],list[int]]>}
# This event is emitted when the property ``Label`` changes in the remote object.
# The property ``Label`` is described in the AES70 standard as follows.
# User-specified label.
#
# @member {PropertyEvent<str>} OcaAgent#OnLabelChanged
# This event is emitted when the property ``Owner`` changes in the remote object.
# The property ``Owner`` is described in the AES70 standard as follows.
# Object number of block that contains this agent.
#
# @member {PropertyEvent<int>} OcaAgent#OnOwnerChanged
