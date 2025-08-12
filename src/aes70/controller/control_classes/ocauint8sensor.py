from ...ocp1.ocauint8 import OcaUint8
from ..make_control_class import make_control_class
from .ocabasicsensor import OcaBasicSensor

# Basic uint8 sensor.
# @extends OcaBasicSensor
# @class OcaUint8Sensor
OcaUint8Sensor = make_control_class(
    'OcaUint8Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0006',
    2,
    OcaBasicSensor,
    [
        ['GetReading', 5, 1, [], [OcaUint8, OcaUint8, OcaUint8]],
    ],
    [
      ['Reading', [OcaUint8], 5, 1, False, False, None],
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
# @method OcaUint8Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Uint8 reading.
#
# @member {PropertyEvent<int>} OcaUint8Sensor#OnReadingChanged
