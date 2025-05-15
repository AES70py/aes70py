from ....aes70.OCP1.OcaBlob import OcaBlob
from ....aes70.OCP1.OcaEvent import OcaEvent
from ....aes70.controller.make_control_class import make_control_class
from .OcaAgent import OcaAgent

# Base class for event handler objects. This class applies to controllers that
# subscribe to events and receive notifications for them. Controller developers
# can derive from this class and add specific callback methods that perform
# processing and/or have specific event data structures.
# @extends OcaAgent
# @class OcaEventHandler
OcaEventHandler = make_control_class(
  'OcaEventHandler',
  3,
  '\u0001\u0002\b',
  2,
  OcaAgent,
  [
    ['OnEvent', 3, 1, [OcaBlob, OcaEvent], []],
  ],
  [],
  []
);

# Generic empty callback method for events. Application developers can override
# this method in a derived class to add behavior.
#
# @method OcaEventHandler#OnEvent
# @param {bytes} Context
# @param {IOcaEvent} eventData
#
# @returns {Promise<None>}
