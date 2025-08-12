from ...ocp1.ocafloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .ocasensor import OcaSensor

# Senses a gain value. Typically used to indicate instantaneous gain value of a
# dynamics element.
# @extends OcaSensor
# @class OcaGainSensor
OcaGainSensor = make_control_class(
    'OcaGainSensor',
    4,
    '\u0001\u0001\u0002\n',
    1,
    OcaSensor,
    [
        ['GetReading', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
    ],
    [
      ['Reading', [OcaFloat32], 4, 1, False, False, None],
    ],
    []
)

# Gets the value and limits of the **Reading** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Reading of type ``int``
# - minReading of type ``int``
# - maxReading of type ``int``
#
# @method OcaGainSensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Gain in dB
#
# @member {PropertyEvent<int>} OcaGainSensor#OnReadingChanged
