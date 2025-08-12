from ...OCP1.OcaString import OcaString
from ...OCP1.OcaUint16 import OcaUint16
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

# Text string sensor.
# @extends OcaBasicSensor
# @class OcaStringSensor
OcaStringSensor = make_control_class(
    'OcaStringSensor',
    5,
    '\u0001\u0001\u0002\u0001\f',
    2,
    OcaBasicSensor,
    [
        ['GetString', 5, 1, [], [OcaString]],
        ['GetMaxLen', 5, 2, [], [OcaUint16]],
        ['SetMaxLen', 5, 3, [OcaUint16], []],
    ],
    [
      ['String', [OcaString], 5, 1, False, False, None],
      ['MaxLen', [OcaUint16], 5, 2, False, False, None],
    ],
    []
)

# Gets the entire string. Return status indicates success or failure of the
# retrieval.
#
# @method OcaStringSensor#GetString
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Gets the maximum number of bytes that may be returned. Returned status
# indicates success or failure of the retrieval.
#
# @method OcaStringSensor#GetMaxLen
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the maximum number of bytes that the object may return. Returned status
# indicates success or failure of the set.
#
# @method OcaStringSensor#SetMaxLen
# @param {int} maxLen
#
# @returns {Promise<None>}
# This event is emitted when the property ``String`` changes in the remote object.
# The property ``String`` is described in the AES70 standard as follows.
# The string.
#
# @member {PropertyEvent<str>} OcaStringSensor#OnStringChanged
# This event is emitted when the property ``MaxLen`` changes in the remote object.
# The property ``MaxLen`` is described in the AES70 standard as follows.
# Maximum length of the returned string. May be readonly in some
# implementations.
#
# @member {PropertyEvent<int>} OcaStringSensor#OnMaxLenChanged
