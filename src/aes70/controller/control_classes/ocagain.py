from ...ocp1.ocafloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .ocaactuator import OcaActuator

# Gain (or attenuation) element.
# @extends OcaActuator
# @class OcaGain
OcaGain = make_control_class(
    'OcaGain',
    4,
    '\u0001\u0001\u0001\u0005',
    2,
    OcaActuator,
    [
        ['GetGain', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetGain', 4, 2, [OcaFloat32], []],
    ],
    [
      ['Gain', [OcaFloat32], 4, 1, False, False, None],
    ],
    []
)

# Gets the value and limits of the Gain property. The return value indicates
# whether the data was successfully retrieved.
# The return values of this method are
#
# - Gain of type ``int``
# - minGain of type ``int``
# - maxGain of type ``int``
#
# @method OcaGain#GetGain
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Gain property. The return value indicates whether the
# property was successfully set.
#
# @method OcaGain#SetGain
# @param {int} Gain
#
# @returns {Promise<None>}
# This event is emitted when the property ``Gain`` changes in the remote object.
# The property ``Gain`` is described in the AES70 standard as follows.
# Gain in dB.
#
# @member {PropertyEvent<int>} OcaGain#OnGainChanged
