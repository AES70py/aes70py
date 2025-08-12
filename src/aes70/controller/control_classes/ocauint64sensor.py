from ...ocp1.ocauint64 import OcaUint64
from ..make_control_class import make_control_class
from .ocabasicsensor import OcaBasicSensor

# Basic Uint64 sensor.
# @extends OcaBasicSensor
# @class OcaUint64Sensor
OcaUint64Sensor = make_control_class(
    'OcaUint64Sensor',
    5,
    '\u0001\u0001\u0002\u0001\t',
    2,
    OcaBasicSensor,
    [
        ['GetReading', 5, 1, [], [OcaUint64, OcaUint64, OcaUint64]],
    ],
    [
      ['Reading', [OcaUint64], 5, 1, False, False, None],
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
# @method OcaUint64Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Uint64 reading.
#
# @member {PropertyEvent<int>} OcaUint64Sensor#OnReadingChanged
