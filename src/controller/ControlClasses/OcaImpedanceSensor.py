from ....aes70.OCP1.OcaImpedance import OcaImpedance
from ....aes70.controller.make_control_class import make_control_class
from .OcaSensor import OcaSensor

# Basic impedance sensor. Value is complex (magnitude and phase).
# @extends OcaSensor
# @class OcaImpedanceSensor
OcaImpedanceSensor = make_control_class(
  'OcaImpedanceSensor',
  4,
  '\u0001\u0001\u0002\t',
  1,
  OcaSensor,
  [
    ['GetReading', 4, 1, [], [OcaImpedance, OcaImpedance, OcaImpedance]],
  ],
  [
    ['Reading', [OcaImpedance], 4, 1, false, false, null
    ],
  ],
  []
);

# Gets the value and limits of the **Reading** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Reading of type ``IOcaImpedance``
# - minReading of type ``IOcaImpedance``
# - maxReading of type ``IOcaImpedance``
#
# @method OcaImpedanceSensor#GetReading
# @returns {Promise<Arguments[OcaImpedance,OcaImpedance,OcaImpedance]>}
# This event is emitted when the property ``Reading`` changes in the remote object.
# The property ``Reading`` is described in the AES70 standard as follows.
# Impedance value (magnitude and phase).
#
# @member {PropertyEvent<OcaImpedance>} OcaImpedanceSensor#OnReadingChanged
