from abc import ABC, abstractmethod
from compiler.backend.foreign_code.structures import ForgeCodeSegment


class ForgeSegmentProcessor(ABC):
  def __init__(self, segments: list[ForgeCodeSegment]):
    if not segments:
      raise ValueError("Segments list cannot be falsy.")
    
    if len(segments) == 0:
      raise ValueError("Segments list cannot be empty.")
    
    if not all(isinstance(segment, ForgeCodeSegment) for segment in segments):
      raise ValueError("Segments list must contain only ForgeCodeSegment instances.")
    
    self.segments = segments
  
  @abstractmethod
  def flush(self) -> str | None:
    return None


class ForgeTranspiler(ABC):
  def __init__(self, segmentProcessor: ForgeSegmentProcessor):
    if not isinstance(segmentProcessor, ForgeSegmentProcessor):
      raise ValueError("segmentProcessor must be an instance of ForgeSegmentProcessor.")
    
    self.segmentProcessor = segmentProcessor

  @abstractmethod
  def flush(self) -> str | None:
    return None