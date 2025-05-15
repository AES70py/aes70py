from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.controller.make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Basic uint32 actuator.
# @extends OcaBasicActuator
# @class OcaUint32Actuator
OcaUint32Actuator = make_control_class(
  'OcaUint32Actuator',
  5,
  '\u0001\u0001\u0001\u0001\b',
  2,
  OcaBasicActuator,
  [
    ['GetSetting', 5, 1, [], [OcaUint32, OcaUint32, OcaUint32]],
    ['SetSetting', 5, 2, [OcaUint32], []],
  ],
  [
    ['Setting', [OcaUint32], 5, 1, false, false, null
    ],
  ],
  []
);

# Gets the value and limits of the **Setting** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Setting of type ``int``
# - minSetting of type ``int``
# - maxSetting of type ``int``
#
# @method OcaUint32Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the **Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaUint32Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Uint32 setting.
#
# @member {PropertyEvent<int>} OcaUint32Actuator#OnSettingChanged
