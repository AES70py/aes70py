"""
This file is part of aes70py.
This file has been generated.
"""
from .ocaprotoport import OcaProtoPort
from .struct import Struct

from ..types.ocaprotosignalpath import OcaProtoSignalPath as type

OcaProtoSignalPath = Struct(
  {
    "SourceProtoPort": OcaProtoPort,
    "SinkProtoPort": OcaProtoPort,
  },
  type
)
