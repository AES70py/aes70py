from ...OCP1.OcaFloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .OcaSensor import OcaSensor

# Basic current sensor.
# @extends OcaSensor
# @class OcaCurrentSensor
OcaCurrentSensor = make_control_class(
    'OcaCurrentSensor',
    4,
    '\u0001\u0001\u0002\b',
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
# @method OcaCurrentSensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Current value (amperes).
#
# @member {PropertyEvent<int>} OcaCurrentSensor#OnReadingChanged
