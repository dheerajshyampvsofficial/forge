if "." in __name__:
  from .fds_parserVisitor import fds_parserVisitor
else:
  from fds_parserVisitor import fds_parserVisitor

from bytecode import Program
from bytecode.instruction import Instruction
from bytecode.inst_types import OP_LOAD
from objects.object import ForgeObject
from objects.num_obj import ForgeNumObject



class FDSVisitor(fds_parserVisitor):

  def __init__(self, program: Program):
    self.program: Program = program

    if not isinstance(self.program, Program):
      raise TypeError(
        f"Invalid 'Program' object: '{self.program}', expected type 'Program'"
      )
  
  def visitParenLiteral(self, ctx):
    return self.visit(ctx.expr())

  def visitNumberLiteral(self, ctx) -> ForgeObject:
    numText: str = ctx.getText()

    if type(numText) is not str:
      raise TypeError(
        f"Invalid number literal: '{numText}' of type '{type(numText).__name__}', expected type 'str'"
      )
    
    try:
      
      return ForgeNumObject(value=float(numText))
      
    except ValueError:
      raise SyntaxError(
        f"Invalid number literal: '{numText}'"
      )
  
  def visitVarLiteral(self, ctx) -> ForgeNumObject:
    # @0 = @1; means targets = [@0], value = @1
    # @0 = @1 = 5; means targets = [@0, @1], values = 5

    self.program.instructions.append(
      Instruction(opcode=OP_LOAD, op_arg=int(ctx.getText()))
    )
  
  def visitAssignmentStmt(self, ctx):
    targets = ' = '.join([target.text for target in ctx.targets])
    value = self.visit(ctx.value)
    
    print(f"{targets} = {value}")
  
"""
assignment:
	variable = VAR (EQUALS values += expr)+ # AssignmentStmt;
"""