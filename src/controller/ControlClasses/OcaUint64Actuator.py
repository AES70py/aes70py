from ....aes70.OCP1.OcaUint64 import OcaUint64
from ....aes70.controller.make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Basic Uint64 actuator.
# @extends OcaBasicActuator
# @class OcaUint64Actuator
OcaUint64Actuator = make_control_class(
  'OcaUint64Actuator',
  5,
  '\u0001\u0001\u0001\u0001\t',
  2,
  OcaBasicActuator,
  [
    ['GetSetting', 5, 1, [], [OcaUint64, OcaUint64, OcaUint64]],
    ['SetSetting', 5, 2, [OcaUint64], []],
  ],
  [
    ['Setting', [OcaUint64], 5, 1, false, false, null
    ],
  ],
  []
);

# Gets the value and limits of the Gain property. The return value indicates
# whether the data was successfully retrieved.
# The return values of this method are
#
# - Setting of type ``int``
# - minSetting of type ``int``
# - maxSetting of type ``int``
#
# @method OcaUint64Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Level property. The return value indicates whether the
# property was successfully set.
#
# @method OcaUint64Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Uint64 setting.
#
# @member {PropertyEvent<int>} OcaUint64Actuator#OnSettingChanged
