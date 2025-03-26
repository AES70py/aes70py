from aes70.OCP1.OcaBitstring import OcaBitstring
from aes70.OCP1.OcaBoolean import OcaBoolean
from aes70.OCP1.OcaUint16 import OcaUint16
from ..make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Bitstring actuator. Maximum bitstring length is 65,536 bits.
# @extends OcaBasicActuator
# @class OcaBitstringActuator
OcaBitstringActuator = make_control_class(
    "OcaBitstringActuator",
    5,
    "\u0001\u0001\u0001\u0001\r",
    2,
    OcaBasicActuator,
    [
        ["GetNrBits", 5, 1, [], [OcaUint16]],
        ["GetBit", 5, 2, [OcaUint16], [OcaBoolean]],
        ["SetBit", 5, 3, [OcaUint16, OcaBoolean], []],
        ["GetBitstring", 5, 4, [], [OcaBitstring]],
        ["SetBitstring", 5, 5, [OcaBitstring], []],
    ],
    [["Bitstring", [OcaBitstring], 5, 1, False, False, None]],
    []
)

# Gets the number of bits in the string. The return value indicates whether the
# property was successfully gathered.
#
# @method OcaBitstringActuator.GetNrBits
# @returns: A promise which resolves to a single value of type number.

# Gets the bit value of the given bit. The return value indicates whether the
# property was successfully gathered.
#
# @method OcaBitstringActuator.GetBit
# @param bitNr: number
#
# @returns: A promise which resolves to a single value of type boolean.

# Sets the bit value of the given bit. The return value indicates whether the
# property was successfully set.
#
# @method OcaBitstringActuator.SetBit
# @param bitNr: number
# @param Value: boolean
#
# @returns: A promise which resolves to void.

# Gets the entire bitstring. The return value indicates whether the property was
# successfully gathered.
#
# @method OcaBitstringActuator.GetBitstring
# @returns: A promise which resolves to a single value of type boolean[].

# Sets the entire bitstring. The return value indicates whether the property
# was successfully set.
#
# @method OcaBitstringActuator.SetBitstring
# @param BitString: boolean[]
#
# @returns: A promise which resolves to void.

# This event is emitted when the property 'Bitstring' changes in the remote object.
# The property 'Bitstring' is described in the AES70 standard as follows.
# The bitstring data.
#
# @member OcaBitstringActuator.OnBitstringChanged
# @type PropertyEvent[boolean[]]
