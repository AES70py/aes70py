from ...ocp1.ocabitstring import OcaBitstring
from ...ocp1.ocaboolean import OcaBoolean
from ...ocp1.ocauint16 import OcaUint16
from ..make_control_class import make_control_class
from .ocabasicactuator import OcaBasicActuator

# Bitstring actuator. Maximum bitstring length is 65,536 bits.
# @extends OcaBasicActuator
# @class OcaBitstringActuator
OcaBitstringActuator = make_control_class(
    'OcaBitstringActuator',
    5,
    '\u0001\u0001\u0001\u0001\r',
    2,
    OcaBasicActuator,
    [
        ['GetNrBits', 5, 1, [], [OcaUint16]],
        ['GetBit', 5, 2, [OcaUint16], [OcaBoolean]],
        ['SetBit', 5, 3, [OcaUint16, OcaBoolean], []],
        ['GetBitstring', 5, 4, [], [OcaBitstring]],
        ['SetBitstring', 5, 5, [OcaBitstring], []],
    ],
    [
      ['Bitstring', [OcaBitstring], 5, 1, False, False, None],
    ],
    []
)

# Gets the number of bits in the string. The return value indicates whether the
# property was successfully gathered.
#
# @method OcaBitstringActuator#GetNrBits
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the bit value of the given bit. The return value indicates whether the
# property was successfully gathered.
#
# @method OcaBitstringActuator#GetBit
# @param {int} bitNr
#
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# Sets the bit value of the given bit. The return value indicates whether the
# property was successfully set.
#
# @method OcaBitstringActuator#SetBit
# @param {int} bitNr
# @param {bool} Value
#
# @returns {Promise<None>}
# Gets the entire bitstring.The return value indicates whether the property was
# successfully gathered.
#
# @method OcaBitstringActuator#GetBitstring
# @returns {Promise<list[bool]>}
#   A promise which resolves to a single value of type ``list[bool]``.
# Sets the entire bitstring. The return value indicates whether the property was
# successfully set.
#
# @method OcaBitstringActuator#SetBitstring
# @param {list[bool]} BitString
#
# @returns {Promise<None>}
# This event is emitted when the property ``Bitstring`` changes in the remote object.
# The property ``Bitstring`` is described in the AES70 standard as follows.
# The bitstring data.
#
# @member {PropertyEvent<list[bool]>} OcaBitstringActuator#OnBitstringChanged
