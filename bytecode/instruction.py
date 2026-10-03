from dataclasses import dataclass
from typing import Final
from .inst_types import get_valid_opcodes_range
from functools import lru_cache

import struct, helpers.u32 as u32

INSTR_STRUCT_: Final = struct.Struct("<II")

@dataclass(frozen=True, slots=True)
class Instruction:
  opcode: int
  op_arg: int

  @staticmethod
  @lru_cache(maxsize=1)
  def _valid_opcodes() -> frozenset:
    return frozenset(get_valid_opcodes_range())

  def __post_init__(self):
    for name in ("opcode", "op_arg"):
      value = getattr(self, name)
      if (isinstance(value, bool)) or (not isinstance(value, int)):
        raise TypeError(f"{name.lstrip('_')} must be an integer, got {type(value).__name__}")
      object.__setattr__(self, name, int(value))

    u32.ensure_u32("opcode", self.opcode)
    u32.ensure_u32("op-arg", self.op_arg)

    if self.opcode not in self._valid_opcodes():
        raise ValueError(f"invalid opcode: {self.opcode} (0x{self.opcode:08X})")
    
  def _export(self) -> bytes:
    return INSTR_STRUCT_.pack(
      self.opcode,
      self.op_arg
    )

  @classmethod
  def from_bytes(cls, instruction_bytes: bytes | bytearray | memoryview) -> "Instruction":
    if not isinstance(instruction_bytes, (bytes, bytearray, memoryview)):
      raise TypeError(f"instruction_bytes must be bytes-like, got {type(instruction_bytes).__name__}")

      mv = memoryview(instruction_bytes)
      if mv.nbytes != INSTR_STRUCT_.size:
        raise ValueError(f"'Instruction' must be exactly {INSTR_STRUCT_.size} bytes, got {mv.nbytes}")
      instruction_bytes = mv.tobytes()

    op_code, op_arg = INSTR_STRUCT_.unpack(instruction_bytes)

    return cls(
      opcode=op_code,
      op_arg=op_arg
    )

  def _format(self, indent_level: int = 0) -> str:
    if isinstance(indent_level, bool) or not isinstance(indent_level, int):
      raise TypeError(f"indent_level must be an int, got {type(indent_level).__name__}")
    
    if not 0 <= indent_level <= 255:
      raise ValueError(f"indent_level must be in range 0-255, got {indent_level}")
    
    return f"{' ' * indent_level}Instruction(op_code={self._opcode}, op_arg={self._op_arg})"