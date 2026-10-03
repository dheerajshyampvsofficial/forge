from .instruction import Instruction, INSTR_STRUCT_
from .header import Header, HDR_STRUCT_
from .data import Data

from dataclasses import dataclass, field, replace

@dataclass
class Program:
  header: Header = field(default_factory=Header)
  data: Data | None = None
  instructions: list[Instruction] = field(default_factory=list)

  def __post_init__(self) -> None:
    if isinstance(self.instructions, tuple):
      self.instructions = list(self.instructions)
    self._validate()

  def _validate(self) -> None:
    if (self.header is None) or (not isinstance(self.header, Header)):
      raise TypeError(f"header must be 'Header', got {type(self.header).__name__}")
 
    if self.data is not None and not isinstance(self.data, Data):
      raise TypeError(f"data must be 'Data' or None, got {type(self.data).__name__}")
 
    if (self.instructions is None) or (not isinstance(self.instructions, list)):
      raise TypeError(f"instructions must be a list, got {type(self.instructions).__name__}")
 
    for i, instr in enumerate(self.instructions):
      if (instr is None) or (not isinstance(instr, Instruction)):
        raise TypeError(f"instructions[{i}] must be 'Instruction', got {type(instr).__name__ if instr else "Falsy"}")


  def _export(self) -> bytes:
    self._validate()

    data_bytes = self.data._export() if self.data is not None else b""
    payload_bytes = b"".join([instr._export() for instr in self.instructions])

    new_header = replace(
      self.header,
      data_size=len(data_bytes),
      payload_size=len(payload_bytes)
    )

    return new_header._export() + data_bytes + payload_bytes

  @classmethod
  def from_bytes(cls, program_bytes: bytes) -> "Program":
    if (program_bytes is None) or (not isinstance(program_bytes, bytes | bytearray | memoryview)):
      raise TypeError(f"program_bytes must be bytes-like, got {type(program_bytes).__name__ if program_bytes else "Falsy"}")

    buf = bytes(program_bytes)

    header_end_seekpoint = HDR_STRUCT_.size
    if len(buf) < header_end_seekpoint:
      raise ValueError("truncated Program found - header")
    
    header = Header.from_bytes(buf[0:header_end_seekpoint])

    instructions = []
    data_obj = None

    data_size = int(header.data_size)
    payload_size = int(header.payload_size)

    data_end_seekpoint = header_end_seekpoint + data_size
    payload_end_seekpoint = data_end_seekpoint + payload_size

    if len(buf) < payload_end_seekpoint:
      raise ValueError("truncated 'Program' - payload")

    if len(buf) > payload_end_seekpoint:
      raise ValueError("trailing garbage bytes found, 'Program', post payload bytes")

    data_obj = Data.from_bytes(buf[header_end_seekpoint:data_end_seekpoint]) if data_size else None
    instruction_size = INSTR_STRUCT_.size

    if payload_size % instruction_size:
      raise ValueError(
        f"payload size: {payload_size} is not a multiple of instruction size: {instruction_size}"
      )

    instructions = [
      Instruction.from_bytes(buf[offset:offset + instruction_size])
        for offset in range(data_end_seekpoint, payload_end_seekpoint, instruction_size)
    ]

    return cls(header=header, data=data_obj, instructions=instructions)

  def _format(self, indent_level: int = 0) -> str:
    if (isinstance(indent_level, bool)) or (not isinstance(indent_level, int)):
      raise TypeError(f"indent_level must be an int, got {type(indent_level).__name__}")
    if indent_level < 0:
      raise ValueError(f"indent_level must be non-negative, got {indent_level}")
 
    indent = "  " * indent_level
    field_indent = "  " * (indent_level + 1)
    item_indent = "  " * (indent_level + 2)
 
    data_repr = repr(self.data) if self.data is not None else "<Empty>"
 
    if self.instructions:
      lines = ",\n".join(f"{item_indent}{instr!r}" for instr in self.instructions)
      instructions_repr = f"[\n{lines}\n{field_indent}]"
    else:
      instructions_repr = "<Empty>"
 
    return (
      f"Program(\n"
      f"{field_indent}header = {self.header._format(indent_level + 1)},\n"
      f"{field_indent}data = {data_repr},\n"
      f"{field_indent}instructions = {instructions_repr}\n"
      f"{indent})"
    )
 
  def __str__(self) -> str:
    return self._format()