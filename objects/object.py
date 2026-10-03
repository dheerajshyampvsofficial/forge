from dataclasses import dataclass
from bytecode.data import DataObject
from abc import ABC, abstractmethod
from typing import Final, Callable, Self

import struct

# type: int, size_of_next_bytes: int
FORGE_OBJECT_STRUCT_: Final = struct.Struct('<II')

@dataclass
class ForgeObject(ABC):
  """
  The structure of a ForgeObject is as follows:
    - obtype: int (2 bytes, unsigned short), (1, 2) are reserved for ForgeObject (base) and ForgeNotImplemented, respectively.
  """
  obtype: int = 0x01

  def to_bytes(self) -> bytes | bytearray | memoryview:
    return FORGE_OBJECT_STRUCT_.pack(
      self.obtype,
      len(self._payload())
    ) + self._payload()

  @abstractmethod
  def _payload(self) -> bytes | bytearray | memoryview:
    raise NotImplementedError("_payload() must be implemented")

  @staticmethod
  def from_bytes(
    fo_bytes: bytes | bytearray | memoryview,
    resolver: Callable[[bytes | bytearray | memoryview], Self]
  ) -> Self:

    """
    Reconstructs a ForgeObject from bytes.
    """

    if not isinstance(fo_bytes, (bytes, bytearray, memoryview)):
      raise TypeError(
        f"'fo_bytes' argument must be of type 'bytes', 'bytearray' or 'memoryview', got '{fo_bytes.__class__.__name__}'"
      )

    if len(fo_bytes) < FORGE_OBJECT_STRUCT_.size:
      raise ValueError(
        f"'fo_bytes' argument is too short, expected at least {FORGE_OBJECT_STRUCT_.size} bytes, got {len(fo_bytes)} bytes"
      )
    
    obtype, obsize = FORGE_OBJECT_STRUCT_.unpack(fo_bytes[:FORGE_OBJECT_STRUCT_.size])

    if type(obtype) is not int:
      raise TypeError(
        f"obtype of the forge object must be of type int, got '{obtype.__class__.__name__}'"
      )
    
    if not (0x02 <= obtype <= 0x0f):
      raise ValueError(
        f"obtype of the forge object must be in the range of 2 to 15 (inclusive), got {obtype}"
      )

    if type(obsize) is not int:
      raise TypeError(
        f"size_of_next_bytes of the forge object must be of type int, got '{obsize.__class__.__name__}'"
      )
    
    remaining_bytes = fo_bytes[FORGE_OBJECT_STRUCT_.size:]
    if len(remaining_bytes) < obsize:
      raise ValueError(
        f"size_of_next_bytes of the forge object expects {obsize} bytes, got {len(remaining_bytes)} bytes"
      )

    if len(remaining_bytes) > obsize:
      raise ValueError(
        f"size_of_next_bytes of the forge object expects {obsize} bytes, got extra {len(remaining_bytes)} as garbage bytes"
      )
    
    obj_ = resolver(remaining_bytes)

    if not isinstance(obj_, ForgeObject):
      raise TypeError(
        f"Rebuilder for obtype '{obtype}' returned an object of type '{type(obj_).__name__}', expected type 'ForgeObject'."
      )
    
    return obj_
  
  @abstractmethod
  def type_str(self) -> str:
    return f"<{self.type_str()}>"
    

class __ForgeNotImplemented(ForgeObject):
  def __init__(self):
    super().__init__(0x02)
  
  def _payload(self) -> bytes | bytearray | memoryview:
    return bytes(0)
  
  def __str__(self) -> str:
    return "ForgeNotImplemented"
  
  def type_str(self) -> str:
    return str(self)

ForgeNotImplemented = __ForgeNotImplemented()