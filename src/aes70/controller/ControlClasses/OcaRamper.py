from ...OCP1.OcaFloat32 import OcaFloat32
from ...OCP1.OcaFloat64 import OcaFloat64
from ...OCP1.OcaProperty import OcaProperty
from ...OCP1.OcaRamperCommand import OcaRamperCommand
from ...OCP1.OcaRamperInterpolationLaw import OcaRamperInterpolationLaw
from ...OCP1.OcaRamperState import OcaRamperState
from ...OCP1.OcaTimeMode import OcaTimeMode
from ...OCP1.OcaUint64 import OcaUint64
from ..make_control_class import make_control_class
from .OcaAgent import OcaAgent

# Agent that gradually changes a property setting from one value to another.
# Works on a scalar numeric or boolean property of a specified object. Does not
# work for array, list, map, struct, or string properties. Contains timer
# features to allow ramps to start immediately or at any time in the future.
# This is a weakly typed class. All ramping parameters are specified as a
# **OcaFloat64** numbers.
#
#  - For unsigned integer targets, the ramping parameters are coerced to
#    **OcaUint64** before comparing.
#
#  - For signed integer targets, the ramping parameters are coerced to
#    **OcaInt64** before comparing.
#
#  - For boolean values, the the ramping parameters are coerced to **OcaUint8.**
#    True is assigned the value One, False is assigned the value Zero.
#
#
# @extends OcaAgent
# @class OcaRamper
OcaRamper = make_control_class(
    'OcaRamper',
    3,
    '\u0001\u0002\u0003',
    2,
    OcaAgent,
    [
        ['Control', 3, 1, [OcaRamperCommand], []],
        ['GetState', 3, 2, [], [OcaRamperState]],
        ['GetRampedProperty', 3, 3, [], [OcaProperty]],
        ['SetRampedProperty', 3, 4, [OcaProperty], []],
        ['GetTimeMode', 3, 5, [], [OcaTimeMode]],
        ['SetTimeMode', 3, 6, [OcaTimeMode], []],
        ['GetStartTime', 3, 7, [], [OcaUint64]],
        ['SetStartTime', 3, 8, [OcaUint64], []],
        ['GetDuration', 3, 9, [], [OcaFloat32, OcaFloat32, OcaFloat32]],
        ['SetDuration', 3, 10, [OcaFloat32], []],
        ['GetInterpolationLaw', 3, 11, [], [OcaRamperInterpolationLaw]],
        ['SetInterpolationLaw', 3, 12, [OcaRamperInterpolationLaw], []],
        ['GetGoal', 3, 13, [], [OcaFloat64]],
        ['SetGoal', 3, 14, [OcaFloat64], []],
    ],
    [
      ['State', [OcaRamperState], 3, 1, False, False, None],
      ['RampedProperty', [OcaProperty], 3, 2, False, False, None],
      ['TimeMode', [OcaTimeMode], 3, 3, False, False, None],
      ['StartTime', [OcaUint64], 3, 4, False, False, None],
      ['Duration', [OcaFloat32], 3, 5, False, False, None],
      ['InterpolationLaw', [OcaRamperInterpolationLaw], 3, 6, False, False, None],
      ['Goal', [OcaFloat64], 3, 7, False, False, None],
    ],
    []
)

# Executes the given ramper command. The return value indicates whether the
# command was successfully executed.
#
# @method OcaRamper#Control
# @param {OcaRamperCommand} Command
#
# @returns {Promise<None>}
# Gets current state of ramper. The return value indicates whether the state was
# successfully retrieved.
#
# @method OcaRamper#GetState
# @returns {Promise<OcaRamperState>}
#   A promise which resolves to a single value of type :class:`OcaRamperState`.
# Gets definition of ramped property. The return value indicates whether the
# object number was successfully retrieved.
#
# @method OcaRamper#GetRampedProperty
# @returns {Promise<OcaProperty>}
#   A promise which resolves to a single value of type :class:`OcaProperty`.
# Defines property to be ramped. The return value indicates whether the
# definition was successful.
#
# @method OcaRamper#SetRampedProperty
# @param {IOcaProperty} property
#
# @returns {Promise<None>}
# Gets ramper time mode (absolute or relative). The return value indicates
# whether the time mode was successfully retrieved.
#
# @method OcaRamper#GetTimeMode
# @returns {Promise<OcaTimeMode>}
#   A promise which resolves to a single value of type :class:`OcaTimeMode`.
# Sets ramper time mode (absolute or relative). The return value indicates
# whether the time mode was successfully set.
#
# @method OcaRamper#SetTimeMode
# @param {OcaTimeMode} TimeMode
#
# @returns {Promise<None>}
# Gets ramp start time. The return value indicates whether the start time was
# successfully retrieved.
#
# @method OcaRamper#GetStartTime
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets ramper start time. The return value indicates whether the start time was
# successfully set.
#
# @method OcaRamper#SetStartTime
# @param {int} TimeMode
#
# @returns {Promise<None>}
# Gets ramp duration. The return value indicates whether the duration was
# successfully retrieved.
# The return values of this method are
#
# - Duration of type ``int``
# - miinDuration of type ``int``
# - maxDuration of type ``int``
#
# @method OcaRamper#GetDuration
# @returns {Promise<Arguments[int,int,int]>}
# Sets ramp duration. The return value indicates whether the duration was
# successfully set.
#
# @method OcaRamper#SetDuration
# @param {int} Duration
#
# @returns {Promise<None>}
# Retrieves interpolation law setting. The return value indicates whether the
# setting was successfully retrieved.
#
# @method OcaRamper#GetInterpolationLaw
# @returns {Promise<OcaRamperInterpolationLaw>}
#   A promise which resolves to a single value of type :class:`OcaRamperInterpolationLaw`.
# Sets ramp interpolation law. The return value indicates whether the law was
# successfully set.
#
# @method OcaRamper#SetInterpolationLaw
# @param {OcaRamperInterpolationLaw} law
#
# @returns {Promise<None>}
# Retrieves ramp goal value. The return value indicates whether the duration was
# successfully retrieved.
#
# @method OcaRamper#GetGoal
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets ramp goal value. The return value indicates whether the duration was
# successfully set.
#
# @method OcaRamper#SetGoal
# @param {int} goal
#
# @returns {Promise<None>}
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# {Ready, Ramping, Paused, Completed, Disabled} Readonly.
#
# @member {PropertyEvent<OcaRamperState>} OcaRamper#OnStateChanged
# This event is emitted when the property ``RampedProperty`` changes in the remote object.
# The property ``RampedProperty`` is described in the AES70 standard as follows.
# Identification of the property being ramped.
#
# @member {PropertyEvent<OcaProperty>} OcaRamper#OnRampedPropertyChanged
# This event is emitted when the property ``TimeMode`` changes in the remote object.
# The property ``TimeMode`` is described in the AES70 standard as follows.
# Absolute or Relative time.
#
# @member {PropertyEvent<OcaTimeMode>} OcaRamper#OnTimeModeChanged
# This event is emitted when the property ``StartTime`` changes in the remote object.
# The property ``StartTime`` is described in the AES70 standard as follows.
# Time at which to start ramp. If **TimeMode=Relative**, the actual event start
# time equals the value of **StartTime** plus the absolute time that
# **StartTime** was most recently set. If **TimeMode=Absolute**, the actual
# event start time equals the value of **StartTime**
#
# @member {PropertyEvent<int>} OcaRamper#OnStartTimeChanged
# This event is emitted when the property ``Duration`` changes in the remote object.
# The property ``Duration`` is described in the AES70 standard as follows.
# Duration of ramp period.
#
# @member {PropertyEvent<int>} OcaRamper#OnDurationChanged
# This event is emitted when the property ``InterpolationLaw`` changes in the remote object.
# The property ``InterpolationLaw`` is described in the AES70 standard as follows.
# Ramper interpolation law
#
# @member {PropertyEvent<OcaRamperInterpolationLaw>} OcaRamper#OnInterpolationLawChanged
# This event is emitted when the property ``Goal`` changes in the remote object.
# The property ``Goal`` is described in the AES70 standard as follows.
# Final value of ramp. Datatype is target property's datatype.
#
# @member {PropertyEvent<int>} OcaRamper#OnGoalChanged
