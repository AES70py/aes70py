from ...ocp1.ocaboolean import OcaBoolean
from ...ocp1.ocafloat32 import OcaFloat32
from ...ocp1.ocafloat64 import OcaFloat64
from ...ocp1.ocaobservationeventdata import OcaObservationEventData
from ...ocp1.ocaobserverstate import OcaObserverState
from ...ocp1.ocaproperty import OcaProperty
from ...ocp1.ocarelationaloperator import OcaRelationalOperator
from ..make_control_class import make_control_class
from .ocaagent import OcaAgent

# Observer of a scalar numeric or boolean property ("target property") of a
# specified object. Does not work for array, list, map, struct, or string
# properties. **OcaNumericObserver** emits an **Observation** event under
# certain conditions. There are three kinds of conditions:
#
#  - **Numeric comparison**. The target property value meets a certain
#    comparison condition. A selection of comparison operators is available.
#    Such observations are called "asynchronous observations".
#
#  - **Timer expiry**. The value of the** Period** property, if nonzero, is a
#    the time interval for the recurrent timed emission of **Observation**
#    events. Such events ("periodic observations") are emitted regardless of the
#    target property's value.
#
#  - **Combination of (1) and (2)**. If a numeric comparison and a nonzero
#    period are both specified, then the **Observation** event is emitted when
#    the timer expires **and** the numeric comparison is true. Such observations
#    are called "conditional-periodic observations".
#
#
# This is a weakly typed class. Its threshold is specified as an **OcaFloat64**
# number.
#
#  - For unsigned integer targets, the threshold and target are both coerced to
#    **OcaUint64** before comparing.
#
#  - For signed integer targets, the threshold and target are both coerced to
#    **OcaInt64** before comparing.
#
#  - For boolean values, the threshold hreshold and target are both coerced to
#    **OcaUint8**, True is assigned the value One, False is assigned the value
#    Zero.
#
#
# Note that this coercion may result in rounding errors if the observed datatype
# is of type OcaUint64 or OcaUint64. An **OcaNumericObserver** instance and the
# property it observes are bound at the time the **OcaNumericObserver** instance
# is constructed. For static devices, construction will occur during
# manufacture, or possibly during a subsequent hardware configuration step. For
# reconfigurable devices, construction might be done by online controllers as
# part of device configuration sessions. This class is normally used for
# monitoring readings of sensor readings, but may be used equally well for
# watching workers' parameter settings.
# @extends OcaAgent
# @class OcaNumericObserver
OcaNumericObserver = make_control_class(
    'OcaNumericObserver',
    3,
    '\u0001\u0002\u0004',
    2,
    OcaAgent,
    [
        ['GetLastObservation', 3, 1, [], [OcaFloat64]],
        ['GetState', 3, 2, [], [OcaObserverState]],
        ['GetObservedProperty', 3, 3, [], [OcaProperty]],
        ['SetObservedProperty', 3, 4, [OcaProperty], []],
        ['GetThreshold', 3, 5, [], [OcaFloat64]],
        ['SetThreshold', 3, 6, [OcaFloat64], []],
        ['GetOperator', 3, 7, [], [OcaRelationalOperator]],
        ['SetOperator', 3, 8, [OcaRelationalOperator], []],
        ['GetTwoWay', 3, 9, [], [OcaBoolean]],
        ['SetTwoWay', 3, 10, [OcaBoolean], []],
        ['GetHysteresis', 3, 11, [], [OcaFloat64]],
        ['SetHysteresis', 3, 12, [OcaFloat64], []],
        ['GetPeriod', 3, 13, [], [OcaFloat32]],
        ['SetPeriod', 3, 14, [OcaFloat32], []],
    ],
    [
      ['State', [OcaObserverState], 3, 1, False, False, None],
      ['ObservedProperty', [OcaProperty], 3, 2, False, False, None],
      ['Threshold', [OcaFloat64], 3, 3, False, False, None],
      ['Operator', [OcaRelationalOperator], 3, 4, False, False, None],
      ['TwoWay', [OcaBoolean], 3, 5, False, False, None],
      ['Hysteresis', [OcaFloat64], 3, 6, False, False, None],
      ['Period', [OcaFloat32], 3, 7, False, False, None],
    ],
    [
      ['Observation', 3, 1, [OcaObservationEventData] ],
    ]
)

# Gets the value of the observed property that was reported by the most recently
# emitted Observation event. If the numeric observer has never emitted an
# Observation event, returns the IEEE not-a-number value. The return status
# indicates whether the value has been successfully returned.
#
# @method OcaNumericObserver#GetLastObservation
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the observer's state. The return value indicates whether the state was
# successfully retrieved.
#
# @method OcaNumericObserver#GetState
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the identification of the property that the observer observes. The return
# value indicates whether the identification was successfully retrieved.
#
# @method OcaNumericObserver#GetObservedProperty
# @returns {Promise<OcaProperty>}
#   A promise which resolves to a single value of type :class:`OcaProperty`.
# Sets the identification of the property that the observer observes. The return
# value indicates whether the identification was successfully set.
#
# @method OcaNumericObserver#SetObservedProperty
# @param {IOcaProperty} property
#
# @returns {Promise<None>}
# Gets the value of the **Threshold** property. The return value indicates
# whether the threshold value was successfully retrieved.
#
# @method OcaNumericObserver#GetThreshold
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the **Threshold** property. The return value indicates
# whether the threshold value was successfully set.
#
# @method OcaNumericObserver#SetThreshold
# @param {int} Threshold
#
# @returns {Promise<None>}
# Gets the value of the **Operator** property. The return value indicates
# whether the property was successfully retrieved.
#
# @method OcaNumericObserver#GetOperator
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the **Operator** property. The return value indicates
# whether the operator was successfully set.
#
# @method OcaNumericObserver#SetOperator
# @param {int} operator
#
# @returns {Promise<None>}
# Gets the value of the **TwoWay** property. The return value indicates whether
# the property was successfully retrieved.
#
# @method OcaNumericObserver#GetTwoWay
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# Sets the value of the **TwoWay** property. The return value indicates whether
# the property was successfully set.
#
# @method OcaNumericObserver#SetTwoWay
# @param {bool} twoWay
#
# @returns {Promise<None>}
# Gets the value of the **Hysteresis** property. The return value indicates
# whether the property was successfully retrieved.
#
# @method OcaNumericObserver#GetHysteresis
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the **Hysteresis** property. The return value indicates
# whether the property was successfully set.
#
# @method OcaNumericObserver#SetHysteresis
# @param {int} hysteresis
#
# @returns {Promise<None>}
# Gets the value of the **Period** property. The return value indicates whether
# the property was successfully retrieved.
#
# @method OcaNumericObserver#GetPeriod
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the value of the **Period** property. The return value indicates whether
# the property was successfully set.
#
# @method OcaNumericObserver#SetPeriod
# @param {int} period
#
# @returns {Promise<None>}
# Event emitted to signal an asynchronous, periodic, or conditional-periodic
# observation.
# @member OcaNumericObserver#OnObservation {Event}
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# State: triggered, not triggered
#
# @member {PropertyEvent<int>} OcaNumericObserver#OnStateChanged
# This event is emitted when the property ``ObservedProperty`` changes in the remote object.
# The property ``ObservedProperty`` is described in the AES70 standard as follows.
# Identification of the property being observed.
#
# @member {PropertyEvent<OcaProperty>} OcaNumericObserver#OnObservedPropertyChanged
# This event is emitted when the property ``Threshold`` changes in the remote object.
# The property ``Threshold`` is described in the AES70 standard as follows.
# Comparison value for raising the **Triggered** event.
#
# @member {PropertyEvent<int>} OcaNumericObserver#OnThresholdChanged
# This event is emitted when the property ``Operator`` changes in the remote object.
# The property ``Operator`` is described in the AES70 standard as follows.
# Relational operator used when comparing the value of the observed property to
# the threshold value.
#
# @member {PropertyEvent<int>} OcaNumericObserver#OnOperatorChanged
# This event is emitted when the property ``TwoWay`` changes in the remote object.
# The property ``TwoWay`` is described in the AES70 standard as follows.
# True to emit a **Triggered** event upon crossing the threshold in either
# direction; false to emit only upon crossing in the primary direction (i.e.
# rising when **Operator** is set to GreaterThan or GreaterThanOrEqual; falling
# when **Operator** is set to LessThan**** or LessThanOrEqual; equality when
# **Operator** is set to Equality; inequality when **Operator** is set to
# Inequality).
#
# @member {PropertyEvent<bool>} OcaNumericObserver#OnTwoWayChanged
# This event is emitted when the property ``Hysteresis`` changes in the remote object.
# The property ``Hysteresis`` is described in the AES70 standard as follows.
# Hysteresis that is used when observing the property value. This indicates
# which amount must be added/subtracted from the **Threshold** value to raise or
# re-enable the **Triggered** event of this **OcaObserver** object. The rules
# for hysteresis handling depend upon the configured **Operator** and **TwoWay**
# properties. The **Hysteresis** property is ignored if the **Operator**
# property is 'Inequality'.
#
# @member {PropertyEvent<int>} OcaNumericObserver#OnHysteresisChanged
# This event is emitted when the property ``Period`` changes in the remote object.
# The property ``Period`` is described in the AES70 standard as follows.
# Repetition period or zero. If nonzero, the observer will retrieve the value
# and emit
#
# @member {PropertyEvent<int>} OcaNumericObserver#OnPeriodChanged
