from ...ocp1.ocaint8 import OcaInt8
from ..make_control_class import make_control_class
from .ocabasicsensor import OcaBasicSensor

# Basic int8 sensor.
# @extends OcaBasicSensor
# @class OcaInt8Sensor
OcaInt8Sensor = make_control_class(
    'OcaInt8Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0002',
    2,
    OcaBasicSensor,
    [
        ['GetReading', 5, 1, [], [OcaInt8, OcaInt8, OcaInt8]],
    ],
    [
      ['Reading', [OcaInt8], 5, 1, False, False, None],
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
# @method OcaInt8Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Int8 reading.
#
# @member {PropertyEvent<int>} OcaInt8Sensor#OnReadingChanged
