from ....aes70.OCP1.OcaFloat32 import OcaFloat32
from ....aes70.controller.make_control_class import make_control_class
from .OcaSensor import OcaSensor

# Basic voltage sensor.
# @extends OcaSensor
# @class OcaVoltageSensor
OcaVoltageSensor = make_control_class(
  'OcaVoltageSensor',
  4,
  '\u0001\u0001\u0002\u0007',
  1,
  OcaSensor,
  [
    ['GetReading', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
  ],
  [
    ['Reading', [OcaFloat32], 4, 1, false, false, null
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
# @method OcaVoltageSensor#GetReading
# @returns {Promise<Arguments[int,int,int]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Voltage value (volts).
#
# @member {PropertyEvent<int>} OcaVoltageSensor#OnReadingChanged
