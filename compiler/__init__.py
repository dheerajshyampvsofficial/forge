import ast


from antlr4 import InputStream, CommonTokenStream
from bytecode import Program, Data
from compiler.backend.foreign_code.structures import ForgeCodeSegment
from compiler.backend.backend_handlers import (
  ForgeSegmentProcessor_Mappings,
  ForgeTranspiler_Mappings
)
from compiler.frontend.fds_lexer import fds_lexer
from compiler.frontend.fds_parser import fds_parser
from compiler.frontend.fds_visitor import FDSVisitor
from dataclasses import dataclass


@dataclass
class VisitorOutput:
  program: Program
  foreign_code_buffer: list[ForgeCodeSegment]


class ForgeCompiler:
  def __init__(self, target_language: str = "py"):
    self.input_text: str
    self.target_language = target_language
  
  def compile(self):
    if (not self.input_text) or (not hasattr(self, "input_text")):
      raise ValueError("No input text provided")
    
    if len(self.input_text) == 0:
      raise ValueError("Input text cannot be empty")
    
    input_stream = InputStream(self.input_text)
    lexer = fds_lexer(input_stream)

    # # Print tokens

    # while True:
    #   token = lexer.nextToken()
    #   if token.type == -1:
    #     break
      
    #   print(
    #     repr(token.text),
    #     '->',
    #     lexer.modeNames[lexer._mode],
    #     end="\n\n"
    #   )
    #   time.sleep(0.5)

    # Run visitor

    token_stream = CommonTokenStream(lexer)

    token_stream.fill()

    # for token in token_stream.tokens:
    #   print(lexer.symbolicNames[token.type], "=", repr(token.text))

    parser = fds_parser(token_stream)
    tree = parser.start()

    visitor_output = VisitorOutput(
      program = Program(
        data = Data()
      ),
      foreign_code_buffer = [],
    )

    visitor = FDSVisitor(
      program = visitor_output.program,
      foreign_code_buffer = visitor_output.foreign_code_buffer
    )
    
    visitor.visit(tree)

    segments_processor_cls = ForgeSegmentProcessor_Mappings.get(
      self.target_language,
      None
    )

    if segments_processor_cls is None:
      raise Exception(
        f"unsupported target language '{self.target_language}' provided"
      )
    
    segments_processor = segments_processor_cls(
      visitor.foreign_code_buffer
    )

    transpiler_cls = ForgeTranspiler_Mappings.get(
      self.target_language,
      None
    )

    if transpiler_cls is None:
      raise Exception(
        f"unsupported target language '{self.target_language}' provided"
      )
    
    transpiler = transpiler_cls(segments_processor)

    return (visitor_output.program, transpiler.flush())

    # if visitor.program.data.objects is not None:
    #   print(visitor.program.data._format())
    #   print()
    
    # print(
    #   ",\n".join([
    #     instruction._format()
    #       for instruction in visitor.program.instructions
    #   ])
    # )
