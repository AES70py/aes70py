from ....aes70.OCP1.OcaBoolean import OcaBoolean
from ....aes70.OCP1.OcaList import OcaList
from ....aes70.OCP1.OcaPowerState import OcaPowerState
from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.controller.make_control_class import make_control_class
from .OcaManager import OcaManager

# Optional manager that manages power settings and state.
#
#  - May be instantiated once in any device.
#
#  - If instantiated, object number must be 5.
#
#
# @extends OcaManager
# @class OcaPowerManager
OcaPowerManager = make_control_class(
  'OcaPowerManager',
  3,
  '\u0001\u0003\u0005',
  2,
  OcaManager,
  [
    ['GetState', 3, 1, [], [OcaPowerState]],
    ['SetState', 3, 2, [OcaPowerState], []],
    ['GetPowerSupplies', 3, 3, [], [OcaList(OcaUint32)]],
    ['GetActivePowerSupplies', 3, 4, [], [OcaList(OcaUint32)]],
    ['ExchangePowerSupply', 3, 5, [OcaUint32, OcaUint32, OcaBoolean], []],
    ['GetAutoState', 3, 6, [], [OcaBoolean]],
  ],
  [
    ['State', [OcaPowerState], 3, 1, false, false, null
    ],
    ['PowerSupplies', [OcaList(OcaUint32)], 3, 2, false, false, null
    ],
    ['ActivePowerSupplies', [OcaList(OcaUint32)], 3, 3, false, false, null
    ],
    ['AutoState', [OcaBoolean], 3, 4, false, false, null
    ],
    ['TargetState', [OcaPowerState], 3, 5, false, false, null
    ],
  ],
  []
);

# Retrieve the value of property **03p01 State**, the current power state of the
# device. Return value indicates whether the value was successfully retrieved.
#
# @method OcaPowerManager#GetState
# @returns {Promise<OcaPowerState>}
#   A promise which resolves to a single value of type :class:`OcaPowerState`.
# Change the device power state. The return value indicates whether the
# requested change has been successfully made.
#
# @method OcaPowerManager#SetState
# @param {OcaPowerState} State
#
# @returns {Promise<None>}
# Retrieves list of object number(s) of all power supply(ies). Return value
# indicates whether the data was successfully retrieved.
#
# @method OcaPowerManager#GetPowerSupplies
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Retrieves list of object number(s) of active power supply(ies). Return value
# indicates whether the data was successfully retrieved.
#
# @method OcaPowerManager#GetActivePowerSupplies
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Deactivate one power supply and activate another. An option switch indicates
# whether the previously active power supply is to be turned off. If it is not
# turned off, it will be placed in the **Unavailable** state. The return value
# indicates whether the requested exchange has been successfully made.
#
# @method OcaPowerManager#ExchangePowerSupply
# @param {int} oldPsu
# @param {int} newPsu
# @param {bool} powerOffOld
#
# @returns {Promise<None>}
# Gets the value of the **AutoState** property. The return value indicates
# whether the value was successfully retrieved.
#
# @method OcaPowerManager#GetAutoState
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# Current power state of device. Readonly.
#
# @member {PropertyEvent<OcaPowerState>} OcaPowerManager#OnStateChanged
# This event is emitted when the property ``PowerSupplies`` changes in the remote object.
# The property ``PowerSupplies`` is described in the AES70 standard as follows.
# List of object numbers of available power supplies.
#
# @member {PropertyEvent<list[int]>} OcaPowerManager#OnPowerSuppliesChanged
# This event is emitted when the property ``ActivePowerSupplies`` changes in the remote object.
# The property ``ActivePowerSupplies`` is described in the AES70 standard as follows.
# Object number(s) of power suppl(ies) currently in use.
#
# @member {PropertyEvent<list[int]>} OcaPowerManager#OnActivePowerSuppliesChanged
# This event is emitted when the property ``AutoState`` changes in the remote object.
# The property ``AutoState`` is described in the AES70 standard as follows.
# True if current state was invoked automatically, not by a controller action.
#
# @member {PropertyEvent<bool>} OcaPowerManager#OnAutoStateChanged
# This event is emitted when the property ``TargetState`` changes in the remote object.
# The property ``TargetState`` is described in the AES70 standard as follows.
# Power state to which the device is transitioning. If no transition is in
# progress, has value None. Readonly.
#
# @member {PropertyEvent<OcaPowerState>} OcaPowerManager#OnTargetStateChanged
