#from aes70.OCP1.OcaBlob import OcaBlob
#from OCP1.OcaBlobFixedLen import OcaBlobFixedLen
from aes70.OCP1.OcaBoolean import OcaBoolean
# from OCP1.OcaDeviceState import OcaDeviceState
# from OCP1.OcaList import OcaList
# from OCP1.OcaManagerDescriptor import OcaManagerDescriptor
from aes70.OCP1.OcaModelDescription import OcaModelDescription

from aes70.OCP1.OcaModelGUID import OcaModelGUID
# from OCP1.OcaResetCause import OcaResetCause
from aes70.OCP1.OcaString import OcaString
from aes70.OCP1.OcaUint16 import OcaUint16
from ..make_control_class import make_control_class
from .OcaManager import OcaManager

"""
/**
 * Mandatory manager that contains information relevant to the whole device.
 *
 *  - Must be instantiated once in every device.
 *
 *  - Must have object number 1.
 *
 *
 * @extends OcaManager
 * @class OcaDeviceManager
 */
"""

OcaDeviceManager = make_control_class(
  'OcaDeviceManager',
  3,
  '\u0001\u0003\u0001',
  2,
  OcaManager,
  [
    ['GetOcaVersion', 3, 1, [], [OcaUint16]],
    ['GetModelGUID', 3, 2, [], [OcaModelGUID]],
    ['GetSerialNumber', 3, 3, [], [OcaString]],
    ['GetDeviceName', 3, 4, [], [OcaString]],
    ['SetDeviceName', 3, 5, [OcaString], []],
    ['GetModelDescription', 3, 6, [], [OcaModelDescription]],
    ['GetDeviceRole', 3, 7, [], [OcaString]],
    ['SetDeviceRole', 3, 8, [OcaString], []],
    ['GetUserInventoryCode', 3, 9, [], [OcaString]],
    ['SetUserInventoryCode', 3, 10, [OcaString], []],
    ['GetEnabled', 3, 11, [], [OcaBoolean]],
    # ['SetEnabled', 3, 12, [OcaBoolean], []],
    # ['GetState', 3, 13, [], [OcaDeviceState]],
    # ['SetResetKey', 3, 14, [OcaBlobFixedLen(16), OcaBlob], []],
    # ['GetResetCause', 3, 15, [], [OcaResetCause]],
    # ['ClearResetCause', 3, 16, [], []],
    ['GetMessage', 3, 17, [], [OcaString]],
    ['SetMessage', 3, 18, [OcaString], []],
    # ['GetManagers', 3, 19, [], [OcaList(OcaManagerDescriptor)]],
    ['GetDeviceRevisionID', 3, 20, [], [OcaString]],
  ],
  [
    ['ModelGUID', [OcaModelGUID], 3, 1, False, False, None],
    ['SerialNumber', [OcaString], 3, 2, False, False, None],
#    ['ModelDescription', [OcaModelDescription.py], 3, 3, False, False, None],
    ['DeviceName', [OcaString], 3, 4, False, False, None],
    ['OcaVersion', [OcaUint16], 3, 5, False, False, None],
    ['DeviceRole', [OcaString], 3, 6, False, False, None],
    ['UserInventoryCode', [OcaString], 3, 7, False, False, None],
    ['Enabled', [OcaBoolean], 3, 8, False, False, None],
#    ['State', [OcaDeviceState], 3, 9, False, False, None],
    ['Busy', [OcaBoolean], 3, 10, False, False, None],
#    ['ResetCause', [OcaResetCause], 3, 11, False, False, None],
    ['Message', [OcaString], 3, 12, False, False, None],
#    ['Managers', [OcaList(OcaManagerDescriptor)], 3, 13, False, False, None],
    ['DeviceRevisionID', [OcaString], 3, 14, True, False, None],
  ],
  []
)
"""
/**
 * Gets the value of the OcaVersion property. The return value indicates whether
 * the property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetOcaVersion
 * @returns {Promise<number>}
 *   A promise which resolves to a single value of type ``number``.
 */
/**
 * Gets the model GUID. The return value indicates whether the GUID was
 * successfully retrieved.
 *
 * @method OcaDeviceManager#GetModelGUID
 * @returns {Promise<OcaModelGUID>}
 *   A promise which resolves to a single value of type :class:`OcaModelGUID`.
 */
/**
 * Gets the value of the SerialNumber property. The return value indicates
 * whether the property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetSerialNumber
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * Gets the device name. The return value indicates whether the property was
 * successfully retrieved.
 *
 * @method OcaDeviceManager#GetDeviceName
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * Sets the device name. The return value indicates whether the property was
 * successfully set.
 *
 * @method OcaDeviceManager#SetDeviceName
 * @param {string} Name
 *
 * @returns {Promise<void>}
 */
/**
 * Gets the model description. The return value indicates whether the
 * description was successfully retrieved.
 *
 * @method OcaDeviceManager#GetModelDescription
 * @returns {Promise<OcaModelDescription.py>}
 *   A promise which resolves to a single value of type :class:`OcaModelDescription.py`.
 */
/**
 * Gets the value of the Role property. The return value indicates whether the
 * property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetDeviceRole
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * Sets the value of the Role property. The return value indicates whether the
 * property was successfully set.
 *
 * @method OcaDeviceManager#SetDeviceRole
 * @param {string} role
 *
 * @returns {Promise<void>}
 */
/**
 * Gets the value of the UserInventoryCode property. The return value indicates
 * whether the property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetUserInventoryCode
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * Sets the value of the UserInventoryCode property. The return value indicates
 * whether the property was successfully set.
 *
 * @method OcaDeviceManager#SetUserInventoryCode
 * @param {string} Code
 *
 * @returns {Promise<void>}
 */
/**
 * Gets the value of the Enabled property. The return value indicates whether
 * the property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetEnabled
 * @returns {Promise<boolean>}
 *   A promise which resolves to a single value of type ``boolean``.
 */
/**
 * Sets the value of the Enabled property. The return value indicates whether
 * the property was successfully set.
 *
 * @method OcaDeviceManager#SetEnabled
 * @param {boolean} enabled
 *
 * @returns {Promise<void>}
 */
/**
 * Gets the value of the State property. The return value indicates whether the
 * property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetState
 * @returns {Promise<IOcaDeviceState>}
 *   A promise which resolves to a single value of type ``IOcaDeviceState``.
 */
/**
 * Sets the value of the reset key of the device. The return value indicates
 * whether the property was successfully set. Note that the device manager must
 * inform the CAP gateway of this key (via the host interface), since the CAP
 * gateway will check for and handle the special reset message.
 *
 * @method OcaDeviceManager#SetResetKey
 * @param {Uint8Array} Key
 * @param {Uint8Array} Address
 *
 * @returns {Promise<void>}
 */
/**
 * Gets the value of the ResetCause property. The return value indicates whether
 * the property was successfully retrieved.
 *
 * @method OcaDeviceManager#GetResetCause
 * @returns {Promise<OcaResetCause>}
 *   A promise which resolves to a single value of type :class:`OcaResetCause`.
 */
/**
 * Clears the ResetCause property, i.e. resets it to the default value
 * 'PowerOn'. Must be used after the reset cause has been read out to ensure
 * differentation between reconnects due to network loss and reconnects due to
 * external or internal reset. Offered as a separate method (instead of
 * implicitly clearing the cause after it has been read out) to accomodate
 * systems that have multiple controllers. The return value indicates whether
 * the property was successfully retrieved.
 *
 * @method OcaDeviceManager#ClearResetCause
 * @returns {Promise<void>}
 */
/**
 * Gets the value of property **Message**. Return value indicates whether value
 * was successfully retrieved.
 *
 * @method OcaDeviceManager#GetMessage
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * Set arbitrary text message into **Message** property. The return value
 * indicates whether the value was successfully set.
 *
 * @method OcaDeviceManager#SetMessage
 * @param {string} Text
 *
 * @returns {Promise<void>}
 */
/**
 * Retrive the list of descriptors of managers instantiated in this device. The
 * return value indicates whether the retrieval was successful.
 *
 * @method OcaDeviceManager#GetManagers
 * @returns {Promise<OcaManagerDescriptor[]>}
 *   A promise which resolves to a single value of type :class:`OcaManagerDescriptor[]`.
 */
/**
 * Gets the value of property **DeviceRevisionID**. Return value indicates
 * whether value was successfully retrieved.
 *
 * @method OcaDeviceManager#GetDeviceRevisionID
 * @returns {Promise<string>}
 *   A promise which resolves to a single value of type ``string``.
 */
/**
 * This event is emitted when the property ``ModelGUID`` changes in the remote object.
 * The property ``ModelGUID`` is described in the AES70 standard as follows.
 * Read-only property that identifies the model of the device. Note this
 * property is not equivalent to a MAC address, because (a) MAC addresses
 * identify individual devices, not models, and (b) MAC addresses are
 * Ethernet-specific, but an OCA device need not have an Ethernet port.
 *
 * @member {PropertyEvent<OcaModelGUID>} OcaDeviceManager#OnModelGUIDChanged
 */
/**
 * This event is emitted when the property ``SerialNumber`` changes in the remote object.
 * The property ``SerialNumber`` is described in the AES70 standard as follows.
 * Read-only property that identifies the serial number of the CAP device.
 *
 * @member {PropertyEvent<string>} OcaDeviceManager#OnSerialNumberChanged
 */
/**
 * This event is emitted when the property ``ModelDescription`` changes in the remote object.
 * The property ``ModelDescription`` is described in the AES70 standard as follows.
 * Read-only property that contains text names for this model, its manufacturer,
 * and its version.
 *
 * @member {PropertyEvent<OcaModelDescription.py>} OcaDeviceManager#OnModelDescriptionChanged
 */
/**
 * This event is emitted when the property ``DeviceName`` changes in the remote object.
 * The property ``DeviceName`` is described in the AES70 standard as follows.
 * Name of the device. Should be unique manufacturer-qualified identifier.
 *
 * @member {PropertyEvent<string>} OcaDeviceManager#OnDeviceNameChanged
 */
/**
 * This event is emitted when the property ``OcaVersion`` changes in the remote object.
 * The property ``OcaVersion`` is described in the AES70 standard as follows.
 * Read-only property that indicates the AES70 version number used by the
 * device.
 *
 * @member {PropertyEvent<number>} OcaDeviceManager#OnOcaVersionChanged
 */
/**
 * This event is emitted when the property ``DeviceRole`` changes in the remote object.
 * The property ``DeviceRole`` is described in the AES70 standard as follows.
 * Role of device in application (arbitrary).
 *
 * @member {PropertyEvent<string>} OcaDeviceManager#OnDeviceRoleChanged
 */
/**
 * This event is emitted when the property ``UserInventoryCode`` changes in the remote object.
 * The property ``UserInventoryCode`` is described in the AES70 standard as follows.
 * Code used for equipment tracking.
 *
 * @member {PropertyEvent<string>} OcaDeviceManager#OnUserInventoryCodeChanged
 */
/**
 * This event is emitted when the property ``Enabled`` changes in the remote object.
 * The property ``Enabled`` is described in the AES70 standard as follows.
 * Indicates whether the device is enabled (and therefore operational).
 *
 * @member {PropertyEvent<boolean>} OcaDeviceManager#OnEnabledChanged
 */
/**
 * This event is emitted when the property ``State`` changes in the remote object.
 * The property ``State`` is described in the AES70 standard as follows.
 * Read-only property that indicates the current state of the device.
 *
 * @member {PropertyEvent<IOcaDeviceState>} OcaDeviceManager#OnStateChanged
 */
/**
 * This event is emitted when the property ``Busy`` changes in the remote object.
 * The property ``Busy`` is described in the AES70 standard as follows.
 * True iff device is working on something and is not available for OCA command
 * activity. Readonly.
 *
 * @member {PropertyEvent<boolean>} OcaDeviceManager#OnBusyChanged
 */
/**
 * This event is emitted when the property ``ResetCause`` changes in the remote object.
 * The property ``ResetCause`` is described in the AES70 standard as follows.
 * Read-only attribute that indicates the reset cause of the last reset.
 *
 * @member {PropertyEvent<OcaResetCause>} OcaDeviceManager#OnResetCauseChanged
 */
/**
 * This event is emitted when the property ``Message`` changes in the remote object.
 * The property ``Message`` is described in the AES70 standard as follows.
 * Arbitrary text message provided by controller. Display and handling of the
 * text is device-dependent and not defined by OCA.
 *
 * @member {PropertyEvent<string>} OcaDeviceManager#OnMessageChanged
 */
/**
 * This event is emitted when the property ``Managers`` changes in the remote object.
 * The property ``Managers`` is described in the AES70 standard as follows.
 * List of all manager objects instantiated in this device.
 *
 * @member {PropertyEvent<OcaManagerDescriptor[]>} OcaDeviceManager#OnManagersChanged
 */
"""