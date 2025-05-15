from ....aes70.OCP1.OcaList import OcaList
from ....aes70.OCP1.OcaMediaClockType import OcaMediaClockType
from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.controller.make_control_class import make_control_class
from .OcaManager import OcaManager

# Optional manager that collects all media clocks the device uses.
#
#  - Must be instantiated once for every device that has more than one media
#    clock object. In this context, "media clock" means an instance of
#    **OcaMediaClock**, **OcaMediaClock3**, or any subclass of these classes.
#
#  - If instantiated, object number must be 7.
#
#
# @extends OcaManager
# @class OcaMediaClockManager
OcaMediaClockManager = make_control_class(
  'OcaMediaClockManager',
  3,
  '\u0001\u0003\u0007',
  2,
  OcaManager,
  [
    ['GetClocks', 3, 1, [], [OcaList(OcaUint32)]],
    ['GetMediaClockTypesSupported', 3, 2, [], [OcaList(OcaMediaClockType)]],
    ['GetClock3s', 3, 3, [], [OcaList(OcaUint32)]],
  ],
  [
    ['ClockSourceTypesSupported', [OcaList(OcaMediaClockType)], 3, 1, false, false, ['MediaClockTypesSupported']
    ],
    ['Clocks', [OcaList(OcaUint32)], 3, 2, false, false, null
    ],
    ['Clock3s', [OcaList(OcaUint32)], 3, 3, false, false, null
    ],
  ],
  []
);

# Gets the list of object numbers of **OcaMediaClock** instances in this device.
# Return value indicates whether list was successfully retrieved. Note: In
# AES70-2017, this method is deprecated.
#
# @method OcaMediaClockManager#GetClocks
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# Gets the list of media clock types supported by **OcaMediaClock** objects in
# the device. Return value indicates whether the list was successfully
# retrieved. Note : In AES70-2017, this method is deprecated.
#
# @method OcaMediaClockManager#GetMediaClockTypesSupported
# @returns {Promise<list[OcaMediaClockType]>}
#   A promise which resolves to a single value of type ``list[OcaMediaClockType]``.
# Gets the list of object numbers of **OcaMediaClock3** instances in this
# device. Return value indicates whether list was successfully retrieved.
#
# @method OcaMediaClockManager#GetClock3s
# @returns {Promise<list[int]>}
#   A promise which resolves to a single value of type ``list[int]``.
# This event is emitted when the property ``ClockSourceTypesSupported`` changes in the remote object.
# The property ``ClockSourceTypesSupported`` is described in the AES70 standard as follows.
# List of clock source types supported by **OcaMediaClock** objects in this
# device. Note: In AES70-2017, this method is deprecated. It only reflects the
# clock types of **OcaMediaClock** objects, which are now deprecated. It does
# not apply to **OcaMediaClock3** objects, since these do not have type
# attributes. If the number of **OcaMediaClock** objects in the device is zero,
# this property is empty.
#
# @member {PropertyEvent<list[OcaMediaClockType]>} OcaMediaClockManager#OnClockSourceTypesSupportedChanged
/**
 * An alias for OnClockSourceTypesSupportedChanged
 *
 * @member {PropertyEvent<list[OcaMediaClockType]>} OcaMediaClockManager#OnMediaClockTypesSupportedChanged
 */
# This event is emitted when the property ``Clocks`` changes in the remote object.
# The property ``Clocks`` is described in the AES70 standard as follows.
# Object numbers of **OcaMediaClock** objects, one for each clock which this
# device uses and/or sources. Note: In AES70-2017, this property is deprecated.
#
# @member {PropertyEvent<list[int]>} OcaMediaClockManager#OnClocksChanged
# This event is emitted when the property ``Clock3s`` changes in the remote object.
# The property ``Clock3s`` is described in the AES70 standard as follows.
# Object numbers of **OcaMediaClock3** objects, one for each clock which this
# device uses and/or sources.
#
# @member {PropertyEvent<list[int]>} OcaMediaClockManager#OnClock3sChanged
