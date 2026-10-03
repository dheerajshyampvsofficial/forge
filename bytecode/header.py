import math, struct

from dataclasses import dataclass
from typing import ClassVar, Final

HDR_STRUCT_: Final = struct.Struct("<4sddd")

@dataclass(frozen=True)
class Header:
  MAGIC: ClassVar[bytes] = b'\x00\x09\x0f\x0e'
  SUPPORTED_VERSION: ClassVar[float] = 0.09
  MAX_SIZE: ClassVar[int] = 2**22 # 1 MiB max for payload / payload
  HDR_STRUCT_: ClassVar[struct.Struct] = struct.Struct("<4sddd")

  magic_number: bytes = MAGIC
  version: float = SUPPORTED_VERSION
  data_size: float = 0.0
  payload_size: float = 0.0

  def __post_init__(self):
    if not isinstance(self.magic_number, bytes):
      raise TypeError("magic number is not of type 'bytes'")
    
    if self.magic_number != self.MAGIC:
      raise ValueError("invalid header bytes found - magic number")

    if type(self.version) is not float:
      raise TypeError("version is not of type 'float'")

    if self.version != self.SUPPORTED_VERSION:
      raise ValueError(f"unsupported version number found in header - {self.version}")

    for name in ("data_size", "payload_size"):
      value_ = getattr(self, name)
      if isinstance(value_, bool) or not isinstance(value_, (int, float)):
        raise TypeError(f"{name} must be a 'number'")
      if not math.isfinite(value_):
        raise ValueError(f"{name} must be 'finite'")
      # Max payload or data size is 1MB
      if (value_ < 0) or (value_ != int(value_)) or (value_ > self.MAX_SIZE):
        raise ValueError(f"{name} must be a 'whole number' between 0 and {self.MAX_SIZE}")

  def _export(self) -> bytes:

    self.__post_init__()

    raw = HDR_STRUCT_.pack(
      self.magic_number,
      self.version,
      self.data_size,
      self.payload_size
    )
    
    return raw
  
  @classmethod
  def from_bytes(cls, header_bytes: bytes) -> "Header":
    if not isinstance(header_bytes, (bytes, bytearray)):
      raise TypeError("header_bytes must be bytes or bytearray")
    
    if len(header_bytes) != HDR_STRUCT_.size:
      raise ValueError(f"header must be exactly {HDR_STRUCT_.size} bytes, got {len(header_bytes)}")

    (magic_number, version, data_size, payload_size) = HDR_STRUCT_.unpack(header_bytes)

    return cls(
      magic_number=magic_number,
      version=version,
      data_size=data_size,
      payload_size=payload_size
    )

  def _format(self, indent_level: int = 0) -> str:
    indent = "  " * indent_level
    field_indent = "  " * (indent_level + 1)
    return (
      f"Header(\n"
      f"{field_indent}magic_number = {self.magic_number},\n"
      f"{field_indent}version = {self.version},\n"
      f"{field_indent}data_size = {self.data_size},\n"
      f"{field_indent}payload_size = {self.payload_size}\n"
      f"{indent})"
    )

  def __str__(self) -> str:
    return self._format()
    