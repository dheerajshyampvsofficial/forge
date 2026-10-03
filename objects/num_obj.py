from dataclasses import dataclass
from typing import Final
from .object import ForgeObject

import struct

FORGE_NUMBER_OBJECT_STRUCT_: Final = struct.Struct('<I')

class ForgeNumObject(ForgeObject):
  def __init__(self, value: float):
    self.obtype = 0x03
    self.value = value
    
    if type(self.value) is not float:
      raise TypeError(
        f"ForgeNumObject's value member must be of type float, got {self.value.__class__.__name__}"
      )

  def binop_methods(self) -> dict[str, callable]:
    return {
      "0x01": None
    }

  @classmethod
  def from_bytes(cls, fo_bytes: bytes | bytearray | memoryview) -> "ForgeNumObject":
    return cls(
      value = 3.0
    )
  
  def _payload(self) -> bytes:
    return FORGE_NUMBER_OBJECT_STRUCT_.pack(int(self.value))
  
  def _format(self, indent_level):
    indent = " " * indent_level
    field_intent = " " * (indent_level + 1)
    return f"{indent}ForgeNumObject(\n{field_intent}value: {self.value}\n{indent})"

  def __str__(self) -> str:
    return self._format(0)
  
  def type_str(self) -> str:
    return "num"

