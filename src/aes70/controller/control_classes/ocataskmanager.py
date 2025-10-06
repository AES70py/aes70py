from ...ocp1.ocablob import OcaBlob
from ...ocp1.ocaboolean import OcaBoolean
from ...ocp1.ocamap import OcaMap
from ...ocp1.ocatask import OcaTask
from ...ocp1.ocataskcommand import OcaTaskCommand
from ...ocp1.ocataskmanagerstate import OcaTaskManagerState
from ...ocp1.ocataskstatechangedeventdata import OcaTaskStateChangedEventData
from ...ocp1.ocataskstatus import OcaTaskStatus
from ...ocp1.ocauint16 import OcaUint16
from ...ocp1.ocauint32 import OcaUint32
from ..make_control_class import make_control_class
from .ocamanager import OcaManager

# Optional manager that collects OcaTask and OcaProgram objects.
#
#  - May be instantiated once in any device.
#
#  - If instantiated, object number must be 11.
#
#
# Tasks shall be device execution threads that start, execute, and (normally)
# stop. The action of an **OcaTask** is defined by an **OcaProgram**. The idea
# is that **OcaTasks** shall execute **OcaPrograms**. **OcaTaskManager** offers
# global control over tasks in the device.
#
#  - Device task processing state is **Enabled** by default. In **Enabled**
#    state, tasks may be running.
#
#  - Device task processing state may be **Disabled** by the **OcaTaskManager
#    Disable** command.
#
#  - The **Disable** command will succeed only if no tasks are running.
#
#
# Tasks may be stopped by: passing the **OcaTaskManager** a **Stop** or
# **Abort** command, which will stop designated tasks in the device;.
# @extends OcaManager
# @class OcaTaskManager
OcaTaskManager = make_control_class(
    'OcaTaskManager',
    3,
    '\u0001\u0003\u000b',
    1,
    OcaManager,
    [
        ['Enable', 3, 1, [OcaBoolean], []],
        ['ControlAllTasks', 3, 2, [OcaTaskCommand, OcaBlob], []],
        ['ControlTaskGroup', 3, 3, [OcaUint16, OcaTaskCommand, OcaBlob], []],
        ['ControlTask', 3, 4, [OcaUint32, OcaTaskCommand, OcaBlob], []],
        ['GetState', 3, 5, [], [OcaTaskManagerState]],
        ['GetTaskStatuses', 3, 6, [], [OcaTaskStatus]],
        ['GetTaskStatus', 3, 7, [OcaUint32], [OcaTaskStatus]],
        ['AddTask', 3, 8, [OcaTask], [OcaTask]],
        ['GetTasks', 3, 9, [], [OcaMap(OcaUint32, OcaTask)]],
        ['GetTask', 3, 10, [OcaUint32], [OcaTask]],
        ['SetTask', 3, 11, [OcaUint32, OcaTask], []],
        ['DeleteTask', 3, 12, [OcaUint32], []],
    ],
    [
      ['State', [OcaTaskManagerState], 3, 1, False, False, None],
      ['Tasks', [OcaMap(OcaUint32, OcaTask)], 3, 2, False, False, None],
    ],
    [
      ['TaskStateChanged', 3, 1, [OcaTaskStateChangedEventData] ],
    ]
)

# Enables (parameter =TRUE) or disables (parameter = FALSE) the running of
# tasks. Changes value of property State from Disabled to Enabled and vice
# versa. All tasks running when Enable is called with parameter = FALSE are
# immediately aborted.
#
# @method OcaTaskManager#Enable
# @param {bool} Enable
#
# @returns {Promise<None>}
# Controls all tasks in device. Return value indicates whether tasks were
# successfully controlled.
#
# @method OcaTaskManager#ControlAllTasks
# @param {int} Command
# @param {bytes} ApplicationTaskParameter
#
# @returns {Promise<None>}
# Controls all tasks in the given group. Return value indicates whether tasks
# were successfully controlled.
#
# @method OcaTaskManager#ControlTaskGroup
# @param {int} GroupID
# @param {int} Command
# @param {bytes} ApplicationTaskParameter
#
# @returns {Promise<None>}
# Controls a specified task. Return value indicates whether tasks were
# successfully controlled.
#
# @method OcaTaskManager#ControlTask
# @param {int} TaskID
# @param {int} Command
# @param {bytes} ApplicationTaskParameter
#
# @returns {Promise<None>}
# Gets value of property **State**. Return value indicates whether value was
# successfully retrieved.
#
# @method OcaTaskManager#GetState
# @returns {Promise<int>}
#   A promise which resolves to a single value of type ``int``.
#
# @method OcaTaskManager#GetTaskStatuses
# @returns {Promise<OcaTaskStatus>}
#   A promise which resolves to a single value of type :class:`OcaTaskStatus`.
#
# @method OcaTaskManager#GetTaskStatus
# @param {int} TaskID
#
# @returns {Promise<OcaTaskStatus>}
#   A promise which resolves to a single value of type :class:`OcaTaskStatus`.
# Creates a Task. Parameters of the new Task are given in the Task parameter;
# device returns the same parameter with the new Task ID filled in. Initial task
# state is set to Disabled. Return value indicates whether Task was successfully
# created.
#
# @method OcaTaskManager#AddTask
# @param {IOcaTask} Task
#
# @returns {Promise<OcaTask>}
#   A promise which resolves to a single value of type :class:`OcaTask`.
# Gets map of Tasks in the device. Return value indicates whether map was
# successfully retrieved.
#
# @method OcaTaskManager#GetTasks
# @returns {Promise<dict[int, OcaTask]>}
#   A promise which resolves to a single value of type ``dict[int, OcaTask]``.
# Retrieves a Task. Return value indicates whether Task was successfully
# retrieved.
#
# @method OcaTaskManager#GetTask
# @param {int} ID
#
# @returns {Promise<OcaTask>}
#   A promise which resolves to a single value of type :class:`OcaTask`.
# Updates a Task. Return value indicates whether Task was successfully updated.
#
# @method OcaTaskManager#SetTask
# @param {int} ID
# @param {IOcaTask} Task
#
# @returns {Promise<None>}
# Deletes a task. Return value indicates whether task was successfully deleted.
# Method fails with status=ProcessingFailed if task is running.
#
# @method OcaTaskManager#DeleteTask
# @param {int} ID
#
# @returns {Promise<None>}
# @member OcaTaskManager#OnTaskStateChanged {Event}
# This event is emitted when the property ``State`` changes in the remote object.
# The property ``State`` is described in the AES70 standard as follows.
# Current state of task processing. State is Disabled after a Disable command
# has been received, Enabled otherwise.
#
# @member {PropertyEvent<int>} OcaTaskManager#OnStateChanged
# This event is emitted when the property ``Tasks`` changes in the remote object.
# The property ``Tasks`` is described in the AES70 standard as follows.
# Task collection
#
# @member {PropertyEvent<dict[int, OcaTask]>} OcaTaskManager#OnTasksChanged
