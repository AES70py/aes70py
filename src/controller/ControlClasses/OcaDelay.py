from ....aes70.OCP1.OcaFloat32 import OcaFloat32
from ....aes70.controller.make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Signal delay - basic version.
# @extends OcaActuator
# @class OcaDelay
OcaDelay = make_control_class(
  'OcaDelay',
  4,
  '\u0001\u0001\u0001\u0007',
  2,
  OcaActuator,
  [
    ['GetDelayTime', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
    ['SetDelayTime', 4, 2, [OcaFloat32], []],
  ],
  [
    ['DelayTime', [OcaFloat32], 4, 1, false, false, null
    ],
  ],
  []
);

# Gets the value of the DelayTime property. The return value indicates whether
# the property was successfully retrieved.
# The return values of this method are
#
# - Time of type ``int``
# - minTime of type ``int``
# - maxTime of type ``int``
#
# @method OcaDelay#GetDelayTime
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the DelayTime property. The return value indicates whether
# the property was successfully set.
#
# @method OcaDelay#SetDelayTime
# @param {int} delayTime
#
# @returns {Promise<None>}
# This event is emitted when the property ``DelayTime`` changes in the remote object.
# The property ``DelayTime`` is described in the AES70 standard as follows.
# Delay in seconds.
#
# @member {PropertyEvent<int>} OcaDelay#OnDelayTimeChanged
