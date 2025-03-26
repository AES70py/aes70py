from aes70.OCP1.OcaFloat32 import OcaFloat32
from ..make_control_class import make_control_class

from .OcaActuator import OcaActuator

"""
Gain (or attenuation) element.
@extends OcaActuator
@class OcaGain
"""
OcaGain = make_control_class(
    'OcaGain',
    4,
    '\u0001\u0001\u0001\u0005',
    2,
    OcaActuator,
    [
        ['GetGain', 4, 1, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetGain', 4, 2, [OcaFloat32], []],
    ],
    [['Gain', [OcaFloat32], 4, 1, False, False, None]],
    []
)

"""
Gets the value and limits of the Gain property. The return value indicates
whether the data was successfully retrieved.
The return values of this method are
- Gain of type ``number``
- minGain of type ``number``
- maxGain of type ``number``

@method OcaGain#GetGain
@returns {Promise<Arguments<number,number,number>>}
"""
"""
Sets the value of the Gain property. The return value indicates whether the
property was successfully set.

@method OcaGain#SetGain
@param {number} Gain
@returns {Promise<void>}
"""
"""
This event is emitted when the property ``Gain`` changes in the remote object.
The property ``Gain`` is described in the AES70 standard as follows.
Gain in dB.

@member {PropertyEvent<number>} OcaGain#OnGainChanged
"""