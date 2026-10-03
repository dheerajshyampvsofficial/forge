from compiler.backend import ForgeSegmentProcessor
from compiler.backend.foreign_code.py import PySegmentProcessor
from compiler.backend.foreign_code.structures import ForgeCodeSegment
from compiler.backend.transpiler.py import PyTranspiler

ForgeSegmentProcessor_Mappings: dict[
  str, Callable[list[ForgeCodeSegment]]
] = {
  "py": PySegmentProcessor
}

ForgeTranspiler_Mappings: dict[
  str, Callable[ForgeSegmentProcessor]
] = {
  "py": PyTranspiler
}