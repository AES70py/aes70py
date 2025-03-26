from aes70.OCP1.OcaUint64 import OcaUint64
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

"""
 * Basic Uint64 sensor.
 * @extends OcaBasicSensor
 * @class OcaUint64Sensor
 */
 """
OcaUint64Sensor = make_control_class(
    'OcaUint64Sensor',
    5,
    '\u0001\u0001\u0002\u0001\t',
    2,
    OcaBasicSensor,
    [['GetReading', 5, 1, [], [OcaUint64, OcaUint64, OcaUint64]]],
    [['Reading', [OcaUint64], 5, 1, False, False, None]],
    []
)

"""
 * Gets the value and limits of the **Reading** property. The return value
 * indicates whether the data was successfully retrieved.
 * The return values of this method are
 *
 * - Reading of type ``number|BigInt``
 * - minReading of type ``number|BigInt``
 * - maxReading of type ``number|BigInt``
 *
 * @method OcaUint64Sensor#GetReading
 * @returns {Promise<Arguments<number|BigInt,number|BigInt,number|BigInt>>}
 */

/**
 * This event is emitted when the property ``Reading`` changes in the remote object.
 * The property ``Reading`` is described in the AES70 standard as follows.
 * Uint64 reading.
 *
 * @member {PropertyEvent<number|BigInt>} OcaUint64Sensor#OnReadingChanged
 */
"""