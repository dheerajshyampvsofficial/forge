from compiler.backend import ForgeSegmentProcessor
from compiler.backend.foreign_code.structures import (
  ForgeCodeSegment,
  Raw,
  Embed,
  SectionCall,
  Thunk,
)

class PySegmentProcessor(ForgeSegmentProcessor):
  def __init__(self, segments: list[ForgeCodeSegment]):
    super().__init__(segments=segments)
    self.__py_code: str = ""
  
  def flush(self) -> str:
    return self.__process()
  
  def __process(self) -> str:
    for segment in self.segments:
      self.__accept(segment)
    return self.__py_code
  
  def __accept(self, segment: ForgeCodeSegment):
    if segment.is_generic():
      raise TypeError("Generic code segment type is not supported for this backend.")

    if isinstance(segment, Raw):
      self.__process_raw(segment)
    elif isinstance(segment, Embed):
      self.__process_embed(segment)
    elif isinstance(segment, SectionCall):
      self.__process_section_call(segment)
    elif isinstance(segment, Thunk):
      self.__process_thunk(segment)
    else:
      raise ValueError("Unknown segment type.")
    
  def __process_raw(self, raw_segment: Raw):
    self.__py_code += raw_segment.text
  
  def __process_embed(self, embed_segment: Embed):
    self.__py_code += (
      "self.interpreter.run("
      f"{embed_segment.offset_start}, {embed_segment.offset_end}"
      ")"
    )
  
  def __process_section_call(self, section_call_segment: SectionCall):
    self.__py_code += (
      "self.interpreter.run("
      f"{section_call_segment.offset_start}, {section_call_segment.offset_end}"
      ")"
    )
  
  def __process_thunk(self, thunk_segment: Thunk):
    self.__py_code += (
      f"lambda: ({thunk_segment.expr})"
    )