from ...OCP1.OcaFloat32 import OcaFloat32
from ...OCP1.OcaLevelDetectionLaw import OcaLevelDetectionLaw
from ...OCP1.OcaParameterMask import OcaParameterMask
from ..make_control_class import make_control_class
from .OcaActuator import OcaActuator

# Dynamics element : side-chain detector.
# @extends OcaActuator
# @class OcaDynamicsDetector
OcaDynamicsDetector = make_control_class(
    'OcaDynamicsDetector',
    4,
    '\u0001\u0001\u0001\u000f',
    2,
    OcaActuator,
    [
        ['GetLaw', 4, 1, [], [OcaLevelDetectionLaw]],
        ['SetLaw', 4, 2, [OcaLevelDetectionLaw], []],
        ['GetAttackTime', 4, 3, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetAttackTime', 4, 4, [OcaFloat32], []],
        ['GetReleaseTime', 4, 5, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetReleaseTime', 4, 6, [OcaFloat32], []],
        ['GetHoldTime', 4, 7, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetHoldTime', 4, 8, [OcaFloat32], []],
        ['SetMultiple', 4, 9, [OcaParameterMask, OcaLevelDetectionLaw, OcaFloat32, OcaFloat32, OcaFloat32], []],
    ],
    [
      ['Law', [OcaLevelDetectionLaw], 4, 1, False, False, None],
      ['AttackTime', [OcaFloat32], 4, 2, False, False, None],
      ['ReleaseTime', [OcaFloat32], 4, 3, False, False, None],
      ['HoldTime', [OcaFloat32], 4, 4, False, False, None],
    ],
    []
)

# Gets the value of the Law property. Return status indicates whether the value
# was successfully retrieved.
#
# @method OcaDynamicsDetector#GetLaw
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the Law property. Return status indicates whether the value
# was successfully set.
#
# @method OcaDynamicsDetector#SetLaw
# @param {int} Law
#
# @returns {Promise<None>}
# Gets the value of the AttackTime property. The return value indicates if the
# value was successfully retrieved.
# The return values of this method are
#
# - Time of type ``int``
# - minTime of type ``int``
# - maxTime of type ``int``
#
# @method OcaDynamicsDetector#GetAttackTime
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the AttackTime property. The return value indicates whether
# the property was successfully set.
#
# @method OcaDynamicsDetector#SetAttackTime
# @param {int} Time
#
# @returns {Promise<None>}
# Gets the value of the ReleaseTime property. The return value indicates if the
# value was successfully retrieved.
# The return values of this method are
#
# - Time of type ``int``
# - minTime of type ``int``
# - maxTime of type ``int``
#
# @method OcaDynamicsDetector#GetReleaseTime
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the ReleaseTime property. The return value indicates whether
# the property was successfully set.
#
# @method OcaDynamicsDetector#SetReleaseTime
# @param {int} Time
#
# @returns {Promise<None>}
# Gets the value of the HoldTime property. The return value indicates if the
# value was successfully retrieved.
# The return values of this method are
#
# - Time of type ``int``
# - minTime of type ``int``
# - maxTime of type ``int``
#
# @method OcaDynamicsDetector#GetHoldTime
# @returns {Promise<Arguments[int,int,int]>}
# Sets the value of the HoldTime property. The return value indicates whether
# the property was successfully set.
#
# @method OcaDynamicsDetector#SetHoldTime
# @param {int} Time
#
# @returns {Promise<None>}
# Sets some or all detector parameters. The return value indicates if the
# parameters were successfully set. The action of this method is atomic - if any
# of the value changes fails, none of the changes are made.
#
# @method OcaDynamicsDetector#SetMultiple
# @param {int} Mask
# @param {int} Law
# @param {int} AttackTime
# @param {int} ReleaseTime
# @param {int} HoldTime
#
# @returns {Promise<None>}
# This event is emitted when the property ``Law`` changes in the remote object.
# The property ``Law`` is described in the AES70 standard as follows.
# Level detection law: RMS, Peak, possibly others
#
# @member {PropertyEvent<int>} OcaDynamicsDetector#OnLawChanged
# This event is emitted when the property ``AttackTime`` changes in the remote object.
# The property ``AttackTime`` is described in the AES70 standard as follows.
# Detector attack time in seconds.
#
# @member {PropertyEvent<int>} OcaDynamicsDetector#OnAttackTimeChanged
# This event is emitted when the property ``ReleaseTime`` changes in the remote object.
# The property ``ReleaseTime`` is described in the AES70 standard as follows.
# Detector release time in seconds.
#
# @member {PropertyEvent<int>} OcaDynamicsDetector#OnReleaseTimeChanged
# This event is emitted when the property ``HoldTime`` changes in the remote object.
# The property ``HoldTime`` is described in the AES70 standard as follows.
# Detector hold time in seconds.
#
# @member {PropertyEvent<int>} OcaDynamicsDetector#OnHoldTimeChanged
