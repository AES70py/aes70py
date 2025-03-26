from aes70.OCP1.OcaInt32 import OcaInt32
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

# Basic int32 sensor.
# @extends OcaBasicSensor
# @class OcaInt32Sensor
OcaInt32Sensor = make_control_class(
    'OcaInt32Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0004',
    2,
    OcaBasicSensor,
    [['GetReading', 5, 1, [], [OcaInt32, OcaInt32, OcaInt32]]],
    [['Reading', [OcaInt32], 5, 1, False, False, None]],
    []
)

# Gets the value and limits of the **Reading** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Reading of type number
# - minReading of type number
# - maxReading of type number
#
# @method OcaInt32Sensor#GetReading
# @returns {Promise<Arguments<number,number,number>>}

# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Int32 reading.
#
# @member {PropertyEvent<number>} OcaInt32Sensor#OnReadingChanged
