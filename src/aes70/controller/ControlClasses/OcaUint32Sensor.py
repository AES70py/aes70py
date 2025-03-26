from aes70.OCP1.OcaUint32 import OcaUint32
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor
"""
 * Basic uint32 sensor.
 * @extends OcaBasicSensor
 * @class OcaUint32Sensor
"""
OcaUint32Sensor = make_control_class(
    'OcaUint32Sensor',
    5,
    '\u0001\u0001\u0002\u0001\b',
    2,
    OcaBasicSensor,
    [['GetReading', 5, 1, [], [OcaUint32, OcaUint32, OcaUint32]]],
    [['Reading', [OcaUint32], 5, 1, False, False, None]],
    []
)

"""
 * Gets the value and limits of the **Reading** property. The return value
 * indicates whether the data was successfully retrieved.
 * The return values of this method are
 *
 * - Reading of type ``number``
 * - minReading of type ``number``
 * - maxReading of type ``number``
 *
 * @method OcaUint32Sensor#GetReading
 * @returns {Promise<Arguments<number,number,number>>}
 */
/**
 * This event is emitted when the property ``Reading`` changes in the remote object.
 * The property ``Reading`` is described in the AES70 standard as follows.
 * Uint32 reading.
 *
 * @member {PropertyEvent<number>} OcaUint32Sensor#OnReadingChanged
"""
