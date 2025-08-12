from ...ocp1.ocauint16 import OcaUint16
from ..make_control_class import make_control_class
from .ocabasicsensor import OcaBasicSensor

# Basic uint16 sensor.
# @extends OcaBasicSensor
# @class OcaUint16Sensor
OcaUint16Sensor = make_control_class(
    'OcaUint16Sensor',
    5,
    '\u0001\u0001\u0002\u0001\u0007',
    2,
    OcaBasicSensor,
    [
        ['GetReading', 5, 1, [], [OcaUint16, OcaUint16, OcaUint16]],
    ],
    [
      ['Reading', [OcaUint16], 5, 1, False, False, None],
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
# @method OcaUint16Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Uint16 reading.
#
# @member {PropertyEvent<int>} OcaUint16Sensor#OnReadingChanged
