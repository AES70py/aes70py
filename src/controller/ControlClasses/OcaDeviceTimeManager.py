from ....aes70.OCP1.OcaList import OcaList
from ....aes70.OCP1.OcaTimePTP import OcaTimePTP
from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.OCP1.OcaUint64 import OcaUint64
from ....aes70.controller.make_control_class import make_control_class
from .OcaManager import OcaManager

# Manager that allows controlling and monitoring a device's time-of-day clock,
# and that collects the device's time source objects.
#
#  - Must be instantiated once in every device that has more than one time
#    source object. In this context, a "time source object" is an instance of
#    **OcaTimeSource** or a subclass of it.
#
#  - If instantiated, object number must be 10.
#
#
# Note: The clock value is accessible via Get and Set methods, but has not been
# defined as a public property because its value is volatile and should not
# cause property-change events. The current value of the **OcaTimeSource**
# object designated by the **CurrentDeviceTimeSource** property of this Manager
# is known as the **Device Time**. The property **TimeSources** was added in
# version 2 of this class.
# @extends OcaManager
# @class OcaDeviceTimeManager
OcaDeviceTimeManager = make_control_class(
  'OcaDeviceTimeManager',
  3,
  '\u0001\u0003\n',
  2,
  OcaManager,
  [
    ['GetDeviceTimeNTP', 3, 1, [], [OcaUint64]],
    ['SetDeviceTimeNTP', 3, 2, [OcaUint64], []],
    ['GetTimeSources', 3, 3, [], [OcaList(OcaUint32)]],
    ['GetCurrentDeviceTimeSource', 3, 4, [], [OcaUint32]],
    ['SetCurrentDeviceTimeSource', 3, 5, [OcaUint32], []],
    ['GetDeviceTimePTP', 3, 6, [], [OcaTimePTP]],
    ['SetDeviceTimePTP', 3, 7, [OcaTimePTP], []],
  ],
  [
    ['TimeSources', [OcaList(OcaUint32)], 3, 1, false, false, null
    ],
    ['CurrentDeviceTimeSource', [OcaUint32], 3, 2, false, false, null
    ],
  ],
  []
);

# Get current value of device time-of-day clock in NTP format. Return value
# indicates whether value was successfully retrieved. This method is optional
# and deprecated.
#
# @method OcaDeviceTimeManager#GetDeviceTimeNTP
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets device time-of-day clock in NTP format. Return value indicates whether
# value was successfully set. Not available if a time source is identified in
# property CurrentDeviceTimeSource. This method is optional and deprecated.
#
# @method OcaDeviceTimeManager#SetDeviceTimeNTP
# @param {int} DeviceTime
#
# @returns {Promise<None>}
# Returns list of object numbers of OcaTimeSource instances in this device.
# Return value indicates whether list was successfully retrieved.
#
# @method OcaDeviceTimeManager#GetTimeSources
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Retrieves ONo of current time source object, or zero if none. Return value
# indicates whether value was successfully retrieved.
#
# @method OcaDeviceTimeManager#GetCurrentDeviceTimeSource
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets ONo of current time source object, or zero if none. Return value
# indicates whether value was successfully retrieved.
#
# @method OcaDeviceTimeManager#SetCurrentDeviceTimeSource
# @param {int} TimeSourceONo
#
# @returns {Promise<None>}
# Get current value of device time-of-day clock in PTP format. Return value
# indicates whether value was successfully retrieved.
#
# @method OcaDeviceTimeManager#GetDeviceTimePTP
# @returns {Promise<OcaTimePTP>}
#   A promise which resolves to a single value of type :class:`OcaTimePTP`.
# Sets device time-of-day clock in PTP format. Return value indicates whether
# value was successfully set. Not available if a time source is identified in
# property CurrentDeviceTimeSource.
#
# @method OcaDeviceTimeManager#SetDeviceTimePTP
# @param {IOcaTimePTP} DeviceTime
#
# @returns {Promise<None>}
# This event is emitted when the property ``TimeSources`` changes in the remote object.
# The property ``TimeSources`` is described in the AES70 standard as follows.
# The list of ONos of OcaTimeSource objects in this device
#
# @member {PropertyEvent<list[int]>} OcaDeviceTimeManager#OnTimeSourcesChanged
# This event is emitted when the property ``CurrentDeviceTimeSource`` changes in the remote object.
# The property ``CurrentDeviceTimeSource`` is described in the AES70 standard as follows.
# The current time source for this device's device time, or zero if none.
#
# @member {PropertyEvent<int>} OcaDeviceTimeManager#OnCurrentDeviceTimeSourceChanged
