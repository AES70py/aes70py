from ....aes70.controller.make_control_class import make_control_class
from .OcaRoot import OcaRoot

# Abstract base class for classes that represent non-audio (i.e. control and
# monitoring) functions. All concrete manager objects are lockable (the
# constructor of this class initializes the Root object with property Lockable
# true).
# @extends OcaRoot
# @class OcaManager
OcaManager = make_control_class(
  'OcaManager',
  2,
  '\u0001\u0003',
  2,
  OcaRoot,
  [],
  [],
  []
);

