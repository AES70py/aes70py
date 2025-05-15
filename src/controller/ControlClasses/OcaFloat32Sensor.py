from ....aes70.OCP1.OcaFloat32 import OcaFloat32
from ....aes70.controller.make_control_class import make_control_class
from .OcaBasicSensor import OcaBasicSensor

# Basic float32 sensor.
# @extends OcaBasicSensor
# @class OcaFloat32Sensor
OcaFloat32Sensor = make_control_class(
  'OcaFloat32Sensor',
  5,
  '\u0001\u0001\u0002\u0001\n',
  2,
  OcaBasicSensor,
  [
    ['GetReading', 5, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
  ],
  [
    ['Reading', [OcaFloat32], 5, 1, false, false, null
    ],
  ],
  []
);

# Gets the value and limits of the **Reading** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Reading of type ``int``
# - minReading of type ``int``
# - maxReading of type ``int``
#
# @method OcaFloat32Sensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Float32 reading.
#
# @member {PropertyEvent<int>} OcaFloat32Sensor#OnReadingChanged
