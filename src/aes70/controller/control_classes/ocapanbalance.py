from ...OCP1.OcaFloat32 import OcaFloat32
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Pan or Balance control.
# @extends OcaActuator
# @class OcaPanBalance
OcaPanBalance = make_control_class(
    'OcaPanBalance',
    4,
    '\u0001\u0001\u0001\u0006',
    2,
    OcaActuator,
    [
        ['GetPosition', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetPosition', 4, 2, [OcaFloat32], []],
        ['GetMidpointGain', 4, 3, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetMidpointGain', 4, 4, [OcaFloat32], []],
    ],
    [
      ['Position', [OcaFloat32], 4, 1, False, False, None],
      ['MidpointGain', [OcaFloat32], 4, 2, False, False, None],
    ],
    []
)

# Gets the value and limits of the Position property. The return value indicates
# whether the data was successfully retrieved.
# The return values of this method are
#
# - Position of type ``int``
# - minPosition of type ``int``
# - maxPosition of type ``int``
#
# @method OcaPanBalance#GetPosition
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the Position property. The return value indicates whether
# the property was successfully set.
#
# @method OcaPanBalance#SetPosition
# @param {int} Position
#
# @returns {Promise<None>}
# Gets the value and limits of the MidpointGain property. The return value
# indicates whether the data was successfully retrieved.
# The return values of this method are
#
# - Gain of type ``int``
# - minGain of type ``int``
# - maxGain of type ``int``
#
# @method OcaPanBalance#GetMidpointGain
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the MidpointGain property. The return value indicates
# whether the property was successfully set.
#
# @method OcaPanBalance#SetMidpointGain
# @param {int} Gain
#
# @returns {Promise<None>}
# This event is emitted when the property ``Position`` changes in the remote object.
# The property ``Position`` is described in the AES70 standard as follows.
# Pan position. Range = -1.0 to +1.0. -1.0 is 100% left, +1.0 is 100% right.
#
# @member {PropertyEvent<int>} OcaPanBalance#OnPositionChanged
# This event is emitted when the property ``MidpointGain`` changes in the remote object.
# The property ``MidpointGain`` is described in the AES70 standard as follows.
# Midpoint gain. Normally, max=0dB, min=-6dB. May be readonly for pan/balance
# objects with fixed midpoint gains.
#
# @member {PropertyEvent<int>} OcaPanBalance#OnMidpointGainChanged
