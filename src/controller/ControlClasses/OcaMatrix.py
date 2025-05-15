from ....aes70.OCP1.OcaList2D import OcaList2D
from ....aes70.OCP1.OcaUint16 import OcaUint16
from ....aes70.OCP1.OcaUint32 import OcaUint32
from ....aes70.OCP1.OcaUint8 import OcaUint8
from ....aes70.controller.make_control_class import make_control_class
from .OcaWorker import OcaWorker

# A matrix is a rectangular array of identical objects ("**members**") that is
# coordinate addressable and has sets of common input and output ports. The
# matrix host does not instantiate these objects, but instead mediates the
# coordinate addressing, implements the common input and output ports, and
# provdes certain other aggregate functions. Matrix members may be workers
# (including blocks), or agents. All members of a matrix must be of the same
# class. No object may belong to more than one matrix at a time. No object may
# appear more than once in a given matrix. The complete model of an OCA matrix
# consists of: 1. One instance of **OcaMatrix.** 2. **(N x M) members**, where
# each member is an instance of a worker or agent class. For any given matrix,
# this class must be the same for all members, and is referred to as the
# **member class.** Members are sometimes referred to as **cells** of the
# matrix. 3. One additional instance of the member class, called the **matrix
# proxy.** Thus, the **OcaMatrix** instance is a container for the
# two-dimensional collection of its members. Once a matrix is set up, the
# controller may get and set member properties by the following procedures:
# **Get** To get a property value of member (x :sub:`1`, y :sub:`1`): 1.
# Controller calls **OcaMatrix.SetXY(x1, y1)**. This action: - locks the
# **OcaMatrix** instance, and - posts x :sub:`1` and y :sub:`1` as coordinates
# of the object whose property value is to be retrieved. 2. Controller calls the
# matrix proxy's **Get** method for the property value desired. This action
# causes the **OcaMatrix** instance to: - decode the posted x :sub:`1` and y
# :sub:`1` values into a member ONo. - call the given **Get** method for the
# object identified by the decoded ONo. - aggregate the **OcaResult** from each
# **Get** call into a consolidated **OcaResult**. - unlock the **OcaMatrix**
# instance. - return the consolidated **OcaResult** to the controller. **Set**
# ** **To set a property value of member (x :sub:`1`, y :sub:`1`), or of row (0,
# y :sub:`1`) or column (x :sub:`1`, 0) or whole matrix (0,0) 1. Controller
# calls **OcaMatrix.SetXY(x1, y1)**. This action: - locks the **OcaMatrix**
# instance, and - posts x :sub:`1` and y :sub:`1` as coordinates of the object
# whose property value is to be changed. 2. Controller calls the matrix proxy's
# **Set** method for the target property. This action causes the **OcaMatrix**
# instance to: - decode the posted x :sub:`1` and y :sub:`1` values into a list
# of target member ONos, as follows: If x :sub:`1` ``>`` 0 and y :sub:`1` ``>``
# 0, the list will be the single ONo of the addressed cell. If x :sub:`1` = 0
# and y :sub:`1` ``>`` 0, the list will be the list of ONos of the cells in row
# y :sub:`1` . If x :sub:`1` ``>`` 0 and y :sub:`1` = 0, the list will be the
# list of ONos of the cells in column x :sub:`1`. If x :sub:`1` = 0 and y
# :sub:`1` = 0, the list will be the list of ONos of all cells of the matrix. -
# call the given **Set** method for each target member in the ONo list. -
# aggregate the **OcaResult** from each **Set** call into a consolidated
# **OcaResult**. - unlock the **OcaMatrix** instance.
# @extends OcaWorker
# @class OcaMatrix
OcaMatrix = make_control_class(
  'OcaMatrix',
  3,
  '\u0001\u0001\u0005',
  2,
  OcaWorker,
  [
    ['GetCurrentXY', 3, 1, [], [OcaUint16, OcaUint16]],
    ['SetCurrentXY', 3, 2, [OcaUint16, OcaUint16], []],
    ['GetSize', 3, 3, [], [OcaUint16, OcaUint16, OcaUint16, OcaUint16, OcaUint16, OcaUint16]],
    ['SetSize', 3, 4, [OcaUint16, OcaUint16], []],
    ['GetMembers', 3, 5, [], [OcaList2D(OcaUint32)]],
    ['SetMembers', 3, 6, [OcaList2D(OcaUint32)], []],
    ['GetMember', 3, 7, [OcaUint16, OcaUint16], [OcaUint32]],
    ['SetMember', 3, 8, [OcaUint16, OcaUint16, OcaUint32], []],
    ['GetProxy', 3, 9, [], [OcaUint32]],
    ['SetProxy', 3, 10, [OcaUint32], []],
    ['GetPortsPerRow', 3, 11, [], [OcaUint8]],
    ['SetPortsPerRow', 3, 12, [OcaUint8], []],
    ['GetPortsPerColumn', 3, 13, [], [OcaUint8]],
    ['SetPortsPerColumn', 3, 14, [OcaUint8], []],
    ['SetCurrentXYLock', 3, 15, [OcaUint16, OcaUint16], []],
    ['UnlockCurrent', 3, 16, [], []],
  ],
  [
    ['X', [OcaUint16], 3, 1, false, false, null
    ],
    ['Y', [OcaUint16], 3, 2, false, false, null
    ],
    ['xSize', [OcaUint16], 3, 3, false, false, null
    ],
    ['ySize', [OcaUint16], 3, 4, false, false, null
    ],
    ['Members', [OcaList2D(OcaUint32)], 3, 5, false, false, null
    ],
    ['Proxy', [OcaUint32], 3, 6, false, false, null
    ],
    ['PortsPerRow', [OcaUint8], 3, 7, false, false, null
    ],
    ['PortsPerColumn', [OcaUint8], 3, 8, false, false, null
    ],
  ],
  []
);

# Gets coordinates of the currently active area (cell, row, column, or whole
# matrix). The returned status indicates whether the operation was successful.
# The return values of this method are
#
# - x of type ``int``
# - y of type ``int``
#
# @method OcaMatrix#GetCurrentXY
# @returns {Promise<Arguments[int,int]>}
# Sets the currently active area (cell, row, column, or whole matrix). The
# returned status indicates whether the operation was successful.
#
# @method OcaMatrix#SetCurrentXY
# @param {int} x
# @param {int} y
#
# @returns {Promise<None>}
# Gets the matrix size. The returned status indicates whether the operation was
# successful.
# The return values of this method are
#
# - xSize of type ``int``
# - ySize of type ``int``
# - minXSize of type ``int``
# - maxXSize of type ``int``
# - minYSize of type ``int``
# - maxYSize of type ``int``
#
# @method OcaMatrix#GetSize
# @returns {Promise<Arguments[int,int,int,int,int,int]>}
# Sets the matrix size. The returned status indicates whether the operation was
# successful. This method will not be available for fixed-size matrices.
#
# @method OcaMatrix#SetSize
# @param {int} xSize
# @param {int} ySize
#
# @returns {Promise<None>}
# Retrieves the 2D array of member object numbers. Cells for which no member has
# been defined will return Zero as the object number.
#
# @method OcaMatrix#GetMembers
# @returns {Promise<list[list[int]]>}
#   A promise which resolves to a single value of type ``list[list[int]]``.
# Sets the entire 2D array of member object numbers. Row and column size of the
# **members** parameter must be equal to the current size of the matrix.
#
# @method OcaMatrix#SetMembers
# @param {list[list[int]]} members
#
# @returns {Promise<None>}
# Retrieves the object number of the member at position (x,y). If no member is
# defined at this position, returns an object number value of Zero.
#
# @method OcaMatrix#GetMember
# @param {int} x
# @param {int} y
#
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Installs a particular object as a member at position (x,y). If another object
# was at this position, it is removed.
#
# @method OcaMatrix#SetMember
# @param {int} x
# @param {int} y
# @param {int} memberONo
#
# @returns {Promise<None>}
# Gets the object number of the matrix proxy.
#
# @method OcaMatrix#GetProxy
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the object number of the matrix proxy.
#
# @method OcaMatrix#SetProxy
# @param {int} ONo
#
# @returns {Promise<None>}
# Gets the number of ports per row. These are input ports.
#
# @method OcaMatrix#GetPortsPerRow
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the number of ports per row. These must be input ports.
#
# @method OcaMatrix#SetPortsPerRow
# @param {int} Ports
#
# @returns {Promise<None>}
# Gets the number of ports per output channel. These are output ports.
#
# @method OcaMatrix#GetPortsPerColumn
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
# Sets the number of ports per column. These must be output ports.
#
# @method OcaMatrix#SetPortsPerColumn
# @param {int} Ports
#
# @returns {Promise<None>}
# Sets the currently active area (cell, row, column, or whole matrix) and locks
# it. Fails if the referenced members cannot all be locked. The returned status
# indicates whether the operation was successful.
#
# @method OcaMatrix#SetCurrentXYLock
# @param {int} x
# @param {int} y
#
# @returns {Promise<None>}
# Unlocks the currently active area of the matrix. Fails if all the members of
# the currently active area cannot be unlocked. Failure is not triggered if one
# or more members of the currently active area are already unlocked at the time
# Unlock() is called. The returned status indicates whether the operation was
# successful.
#
# @method OcaMatrix#UnlockCurrent
# @returns {Promise<None>}
# This event is emitted when the property ``X`` changes in the remote object.
# The property ``X`` is described in the AES70 standard as follows.
# Active column index. The active column is the column to which matrix proxy
# method calls will be reflected. Value is zero-relative, i.e. the first column
# is number zero. A value of 65535 means all columns in the matrix.
#
# @member {PropertyEvent<int>} OcaMatrix#OnXChanged
# This event is emitted when the property ``Y`` changes in the remote object.
# The property ``Y`` is described in the AES70 standard as follows.
# Active row index. The active row is the row to which matrix proxy changes will
# be reflected. Value is zero-relative, i.e. the first row is number zero. A
# value of 65535 means all rows in the matrix.
#
# @member {PropertyEvent<int>} OcaMatrix#OnYChanged
# This event is emitted when the property ``xSize`` changes in the remote object.
# The property ``xSize`` is described in the AES70 standard as follows.
# Number of columns in the matrix. Readonly in some cases.
#
# @member {PropertyEvent<int>} OcaMatrix#OnxSizeChanged
# This event is emitted when the property ``ySize`` changes in the remote object.
# The property ``ySize`` is described in the AES70 standard as follows.
# Number of rows in the matrix. Readonly in some cases.
#
# @member {PropertyEvent<int>} OcaMatrix#OnySizeChanged
# This event is emitted when the property ``Members`` changes in the remote object.
# The property ``Members`` is described in the AES70 standard as follows.
# 2D array of member object numbers.
#
# @member {PropertyEvent<list[list[int]]>} OcaMatrix#OnMembersChanged
# This event is emitted when the property ``Proxy`` changes in the remote object.
# The property ``Proxy`` is described in the AES70 standard as follows.
# Object number of the matrix proxy.
#
# @member {PropertyEvent<int>} OcaMatrix#OnProxyChanged
# This event is emitted when the property ``PortsPerRow`` changes in the remote object.
# The property ``PortsPerRow`` is described in the AES70 standard as follows.
# Number of input ports per row- e.g. for a stereo matrix, the value would be 2.
#
# @member {PropertyEvent<int>} OcaMatrix#OnPortsPerRowChanged
# This event is emitted when the property ``PortsPerColumn`` changes in the remote object.
# The property ``PortsPerColumn`` is described in the AES70 standard as follows.
# Number of output ports per column - e.g. for a stereo matrix, the value would
# be 2.
#
# @member {PropertyEvent<int>} OcaMatrix#OnPortsPerColumnChanged
