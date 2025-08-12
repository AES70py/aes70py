from ...OCP1.OcaFloat64 import OcaFloat64
from ..make_control_class import make_control_class
from .OcaBasicActuator import OcaBasicActuator

# Basic Float64 actuator.
# @extends OcaBasicActuator
# @class OcaFloat64Actuator
OcaFloat64Actuator = make_control_class(
    'OcaFloat64Actuator',
    5,
    '\u0001\u0001\u0001\u0001\u000b',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaFloat64, OcaFloat64, OcaFloat64]],
        ['SetSetting', 5, 2, [OcaFloat64], []],
    ],
    [
      ['Setting', [OcaFloat64], 5, 1, False, False, None],
    ],
    []
)

# Gets the value and limits of the **Setting** property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Setting of type ``int``
# - minSetting of type ``int``
# - maxSetting of type ``int``
#
# @method OcaFloat64Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Level property. The return value indicates whether the
# property was successfully set.
#
# @method OcaFloat64Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Float64 value.
#
# @member {PropertyEvent<int>} OcaFloat64Actuator#OnSettingChanged
