from abc import ABC
from dataclasses import dataclass

class ForgeCodeSegment(ABC):
  def is_generic(self) -> bool:
    return True

@dataclass
class Raw(ForgeCodeSegment):
  text: str

  def is_generic(self) -> bool:
    return False

@dataclass
class Embed(ForgeCodeSegment):
  offset_start: int
  offset_end: int

  def is_generic(self) -> bool:
    return False

@dataclass
class SectionCall(ForgeCodeSegment):
  offset_start: int
  offset_end: int

  def is_generic(self) -> bool:
    return False

@dataclass
class Thunk(ForgeCodeSegment):
  expr: str

  def is_generic(self) -> bool:
    return False