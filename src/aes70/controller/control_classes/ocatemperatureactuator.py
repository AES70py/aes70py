from ...ocp1.ocafloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .ocaactuator import OcaActuator

# A temperature actuator. Works in Celsius.
# @extends OcaActuator
# @class OcaTemperatureActuator
OcaTemperatureActuator = make_control_class(
    'OcaTemperatureActuator',
    4,
    '\u0001\u0001\u0001\u0014',
    2,
    OcaActuator,
    [
        ['GetTemperature', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetTemperature', 4, 2, [OcaFloat32], []],
    ],
    [
      ['Temperature', [OcaFloat32], 4, 1, False, False, None],
    ],
    []
)

# Gets the value of the Temperature property. The return value indicates whether
# the property was successfully retrieved.
# The return values of this method are
#
# - temperature of type ``int``
# - minTemperature of type ``int``
# - maxTemperature of type ``int``
#
# @method OcaTemperatureActuator#GetTemperature
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Temperature property. The return value indicates whether
# the property was successfully set.
#
# @method OcaTemperatureActuator#SetTemperature
# @param {int} temperature
#
# @returns {Promise<None>}
# This event is emitted when the property ``Temperature`` changes in the remote object.
# The property ``Temperature`` is described in the AES70 standard as follows.
# The temperature.
#
# @member {PropertyEvent<int>} OcaTemperatureActuator#OnTemperatureChanged
