from ....aes70.OCP1.OcaBitstring import OcaBitstring
from ....aes70.OCP1.OcaUint16 import OcaUint16
from ....aes70.OCP1.OcaUint8 import OcaUint8
from ....aes70.controller.make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

# Bit string sensor.
# @extends OcaBasicSensor
# @class OcaBitstringSensor
OcaBitstringSensor = make_control_class(
  'OcaBitstringSensor',
  5,
  '\u0001\u0001\u0002\u0001\r',
  2,
  OcaBasicSensor,
  [
    ['GetNrBits', 5, 1, [], [OcaUint16]],
    ['GetBit', 5, 2, [OcaUint16], [OcaUint8]],
    ['GetBitString', 5, 3, [], [OcaBitstring]],
  ],
  [
    ['BitString', [OcaBitstring], 5, 1, false, false, null
    ],
  ],
  []
);

# Gets the number of bits of the bitmask data. Returned status indicates success
# or failure of the retrieval.
#
# @method OcaBitstringSensor#GetNrBits
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the value of the given bit. Return status indicates success or failure of
# the retrieval.
#
# @method OcaBitstringSensor#GetBit
# @param {int} bitNr
#
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the entire bitstring. Return status indicates success or failure of the
# retrieval.
#
# @method OcaBitstringSensor#GetBitString
# @returns {Promise<list[bool]>}
#   A promise which resolves to a single value of type ``list[bool]``.
# This event is emitted when the property ``BitString`` changes in the remote object.
# The property ``BitString`` is described in the AES70 standard as follows.
# The bitstring.
#
# @member {PropertyEvent<list[bool]>} OcaBitstringSensor#OnBitStringChanged
