from aes70.OCP1.OcaUint16 import OcaUint16
from aes70.OCP1.OcaUint32 import OcaUint32
from aes70.OCP1.String16 import String16
from ..make_control_class import make_control_class
from ..object_base import ObjectBase
from ...OCP1.OcaBoolean import OcaBoolean
from ...OCP1.OcaString import OcaString
from ...OCP1.OcaClassIdentification import OcaClassIdentification

OcaRoot = make_control_class(
    'OcaRoot',
    1,
    '\u0001',
    2,
    ObjectBase,
    [
        ['GetClassIdentification', 1, 1, [], [OcaClassIdentification]],
        ['GetLockable', 1, 2, [], [OcaBoolean]],
        ['LockTotal', 1, 3, [], []],
        ['Unlock', 1, 4, [], []],
        ['GetRole', 1, 5, [], [OcaString]],
        ['LockReadonly', 1, 6, [], []],
    ],
    [
        ['ClassID', [String16], 1, 1, True, True, None],
        ['ClassVersion', [OcaUint16], 1, 2, True, True, None],
        ['ObjectNumber', [OcaUint32], 1, 3, True, False, None],
        ['Lockable', [OcaBoolean], 1, 4, True, False, None],
        ['Role', [OcaString], 1, 5, True, False, None],
    ], []
#    [['PropertyChanged', 1, 1, [OcaPropertyChangedEventData]]]
)

# JavaScript method documentation comments preserved as Python comments below:

"""
Gets the class identification, a structure that contains the ClassID and
ClassVersion. The return value indicates whether the property was
successfully retrieved.

@method OcaRoot#GetClassIdentification
@returns {Promise<OcaClassIdentification>}
  A promise which resolves to a single value of type OcaClassIdentification.
"""

"""
Gets the value of the Lockable property. The return value indicates whether
the property was successfully retrieved.

@method OcaRoot#GetLockable
@returns {Promise<boolean>}
  A promise which resolves to a single value of type boolean.
"""

"""
Locks the object totally, so that it can only be accessed for reading or
writing by the lockholder. If the device is read-only locked (by a prior call
to LockReadonly()) when Lock() is called by the same lockholder, the lock
state is upgraded to total. If the call is from a session other than the
lockholder's, the call fails. The return value indicates whether the
operation succeeded.

@method OcaRoot#LockTotal
@returns {Promise<void>}
"""

"""
Unlocks the object so that it can be freely accessed again. This method can
only succeed if it is called by the lockholder. The return value indicates
whether the operation succeeded.

@method OcaRoot#Unlock
@returns {Promise<void>}
"""

"""
Returns value of Role property. The return value indicates whether the
operation succeeded.

@method OcaRoot#GetRole
@returns {Promise<string>}
  A promise which resolves to a single value of type string.
"""

"""
Locks the object so that its properties may only be modified by the
lockholder, but others can still retrieve property values. If the device is
already locked (by a prior call to Lock() or LockReadonly()) when
LockReadonly() is called by the same lockholder, the lock state is set to
read-only. If the call is from a session other than the lockholder's, the
call fails. The return value indicates whether the operation succeeded.

@method OcaRoot#LockReadonly
@returns {Promise<void>}
"""

"""
General event that is emitted when a property changes. In each setter method
(of derived classes) this event must be raised with the proper derived event
data structure.
@member OcaRoot#OnPropertyChanged {Event}
"""
