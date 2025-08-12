from ...ocp1.ocauint8 import OcaUint8
from ..make_control_class import make_control_class
from .ocabasicactuator import OcaBasicActuator

# Basic uint8 actuator.
# @extends OcaBasicActuator
# @class OcaUint8Actuator
OcaUint8Actuator = make_control_class(
    'OcaUint8Actuator',
    5,
    '\u0001\u0001\u0001\u0001\u0006',
    2,
    OcaBasicActuator,
    [
        ['GetSetting', 5, 1, [], [OcaUint8, OcaUint8, OcaUint8]],
        ['SetSetting', 5, 2, [OcaUint8], []],
    ],
    [
      ['Setting', [OcaUint8], 5, 1, False, False, None],
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
# @method OcaUint8Actuator#GetSetting
# @returns {Promise<Arguments[int,int,int]>}
# Sets the **Setting** property. The return value indicates whether the property
# was successfully set.
#
# @method OcaUint8Actuator#SetSetting
# @param {int} Setting
#
# @returns {Promise<None>}
# This event is emitted when the property ``Setting`` changes in the remote object.
# The property ``Setting`` is described in the AES70 standard as follows.
# Uint8 setting.
#
# @member {PropertyEvent<int>} OcaUint8Actuator#OnSettingChanged
