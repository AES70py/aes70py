# Required Dependencies and Imports
from aes70.OCP1.OcaBoolean import OcaBoolean
from ..make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

# /**
#  * Basic boolean sensor.
#  * @extends OcaBasicSensor
#  * @class OcaBooleanSensor
#  */
OcaBooleanSensor = make_control_class(
    'OcaBooleanSensor',
    5,
    '\u0001\u0001\u0002\u0001\u0001',
    2,
    OcaBasicSensor,
    [['GetReading', 5, 1, [], [OcaBoolean]]],
    [['Reading', [OcaBoolean], 5, 1, False, False, None]],
    []
)

# /**
#  * Gets the **Reading** property. The return value indicates whether the data
#  * was successfully retrieved.
#  *
#  * @method OcaBooleanSensor#GetReading
#  * @returns {Promise<boolean>}
#  *   A promise which resolves to a single value of type ``boolean``.
#  */
# /**
#  * This event is emitted when the property ``Reading`` changes in the remote object.
#  * The property ``Reading`` is described in the AES70 standard as follows.
#  * Boolean reading.
#  *
#  * @member {PropertyEvent<boolean>} OcaBooleanSensor#OnReadingChanged
#  */
