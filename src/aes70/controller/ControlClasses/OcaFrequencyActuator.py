from ...OCP1.OcaFloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Simple frequency actuator.
# @extends OcaActuator
# @class OcaFrequencyActuator
OcaFrequencyActuator = make_control_class(
    'OcaFrequencyActuator',
    4,
    '\u0001\u0001\u0001\b',
    2,
    OcaActuator,
    [
        ['GetFrequency', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetFrequency', 4, 2, [OcaFloat32], []],
    ],
    [
      ['Frequency', [OcaFloat32], 4, 1, False, False, None],
    ],
    []
)

# Gets the value of the Frequency property. The return value indicates whether
# the property was successfully retrieved.
# The return values of this method are
#
# - Frequency of type ``int``
# - minFrequency of type ``int``
# - maxFrequency of type ``int``
#
# @method OcaFrequencyActuator#GetFrequency
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Frequency property. The return value indicates whether
# the property was successfully set.
#
# @method OcaFrequencyActuator#SetFrequency
# @param {int} Frequency
#
# @returns {Promise<None>}
# This event is emitted when the property ``Frequency`` changes in the remote object.
# The property ``Frequency`` is described in the AES70 standard as follows.
# Frequency in Hertz.
#
# @member {PropertyEvent<int>} OcaFrequencyActuator#OnFrequencyChanged
