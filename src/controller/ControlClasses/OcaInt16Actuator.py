from ....aes70.OCP1.OcaInt16 import OcaInt16
from ....aes70.controller.make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Basic int16 actuator.
# @extends OcaBasicActuator
# @class OcaInt16Actuator
OcaInt16Actuator = make_control_class(
  'OcaInt16Actuator',
  5,
  '\u0001\u0001\u0001\u0001\u0003',
  2,
  OcaBasicActuator,
  [
    ['GetSetting', 5, 1, [], [OcaInt16, OcaInt16, OcaInt16]],
    ['SetSetting', 5, 2, [OcaInt16], []],
  ],
  [
    ['Setting', [OcaInt16], 5, 1, false, false, null
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
# @method OcaInt16Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the **Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaInt16Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Int16 setting.
#
# @member {PropertyEvent<int>} OcaInt16Actuator#OnSettingChanged
