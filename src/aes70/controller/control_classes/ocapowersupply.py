from ...ocp1.ocaboolean import OcaBoolean
from ...ocp1.ocafloat32 import OcaFloat32
from ...ocp1.ocapowersupplylocation import OcaPowerSupplyLocation
from ...ocp1.ocapowersupplystate import OcaPowerSupplyState
from ...ocp1.ocapowersupplytype import OcaPowerSupplyType
from ...ocp1.ocastring import OcaString
from ..make_control_class import make_control_class
from .ocaagent import OcaAgent

# A power supply.
# @extends OcaAgent
# @class OcaPowerSupply
OcaPowerSupply = make_control_class(
    'OcaPowerSupply',
    3,
    '\u0001\u0002\u0007',
    3,
    OcaAgent,
    [
        ['GetType', 3, 1, [], [OcaPowerSupplyType]],
        ['GetModelInfo', 3, 2, [], [OcaString]],
        ['GetState', 3, 3, [], [OcaPowerSupplyState]],
        ['SetState', 3, 4, [OcaPowerSupplyState], []],
        ['GetCharging', 3, 5, [], [OcaBoolean]],
        ['GetLoadFractionAvailable', 3, 6, [], [OcaFloat32]],
        ['GetStorageFractionAvailable', 3, 7, [], [OcaFloat32]],
        ['GetLocation', 3, 8, [], [OcaPowerSupplyLocation]],
    ],
    [
      ['Type', [OcaPowerSupplyType], 3, 1, False, False, None],
      ['ModelInfo', [OcaString], 3, 2, False, False, None],
      ['State', [OcaPowerSupplyState], 3, 3, False, False, None],
      ['Charging', [OcaBoolean], 3, 4, False, False, None],
      ['LoadFractionAvailable', [OcaFloat32], 3, 5, False, False, None],
      ['StorageFractionAvailable', [OcaFloat32], 3, 6, False, False, None],
      ['Location', [OcaPowerSupplyLocation], 3, 7, True, False, None],
    ],
    []
)

# Gets the type of the power supply. Return value indicates whether the data was
# successfully retrieved.
#
# @method OcaPowerSupply#GetType
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the power supply's model information text. Return value indicates whether
# the data was successfully retrieved.
#
# @method OcaPowerSupply#GetModelInfo
# @returns {Promise<str>}
#   A promise which resolves to a single value of type ``str``.
# Gets the state of the power supply. Return value indicates whether the data
# was successfully retrieved.
#
# @method OcaPowerSupply#GetState
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Changes the power supply's state. Return value indicates whether the state was
# successfully changed.
#
# @method OcaPowerSupply#SetState
# @param {int} state
#
# @returns {Promise<None>}
# Gets the value of property **Charging**. Return value indicates whether the
# value was successfully retrieved.
#
# @method OcaPowerSupply#GetCharging
# @returns {Promise<bool>}
#   A promise which resolves to a single value of type ``bool``.
# Gets the available load fraction. Return value indicates whether the data was
# successfully retrieved.
#
# @method OcaPowerSupply#GetLoadFractionAvailable
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the available storage fraction. Return value indicates whether the data
# was successfully retrieved.
#
# @method OcaPowerSupply#GetStorageFractionAvailable
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Gets the power supply physical location. Return value indicates whether the
# data was successfully retrieved.
#
# @method OcaPowerSupply#GetLocation
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# This event is emitted when the property ``Type`` changes in the remote object.
# The property ``Type`` is described in the AES70 standard as follows.
# Type of power supply.
#
# @member {PropertyEvent<int>} OcaPowerSupply#OnTypeChanged
# This event is emitted when the property ``ModelInfo`` changes in the remote object.
# The property ``ModelInfo`` is described in the AES70 standard as follows.
# Model information for power supply. Text; content is implementation-dependent.
#
# @member {PropertyEvent<str>} OcaPowerSupply#OnModelInfoChanged
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# State of power supply: off, unavailable, available, active.
#
# @member {PropertyEvent<int>} OcaPowerSupply#OnStateChanged
# This event is emitted when the property ``Charging`` changes in the remote object.
# The property ``Charging`` is described in the AES70 standard as follows.
# True iff charging. For rechargable supplies (obviously).
#
# @member {PropertyEvent<bool>} OcaPowerSupply#OnChargingChanged
# This event is emitted when the property ``LoadFractionAvailable`` changes in the remote object.
# The property ``LoadFractionAvailable`` is described in the AES70 standard as follows.
# Fraction of power supply's load capacity that is currently not being used.
# Readonly. Normal value range 0...1. A negative value indicates this data is
# not available.
#
# @member {PropertyEvent<int>} OcaPowerSupply#OnLoadFractionAvailableChanged
# This event is emitted when the property ``StorageFractionAvailable`` changes in the remote object.
# The property ``StorageFractionAvailable`` is described in the AES70 standard as follows.
# Fraction of power supply's energy storage that remains available. For battery
# supplies. Readonly. Normal value range 0...1. A negative value indicates this
# data is not available.
#
# @member {PropertyEvent<int>} OcaPowerSupply#OnStorageFractionAvailableChanged
