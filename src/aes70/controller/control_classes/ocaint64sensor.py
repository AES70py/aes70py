from ...ocp1.ocaint64 import OcaInt64
from ..make_control_class import make_control_class
from .ocabasicsensor import OcaBasicSensor

# Basic int64 sensor.
# @extends OcaBasicSensor
# @class OcaInt64Sensor
OcaInt64Sensor = make_control_class(
    'OcaInt64Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0005',
    2,
    OcaBasicSensor,
    [
        ['GetReading', 5, 1, [], [OcaInt64, OcaInt64, OcaInt64]],
    ],
    [
      ['Reading', [OcaInt64], 5, 1, False, False, None],
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
# @method OcaInt64Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Int64 reading.
#
# @member {PropertyEvent<int>} OcaInt64Sensor#OnReadingChanged
