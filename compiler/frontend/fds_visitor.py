import ast

from bytecode import Program
from bytecode.data import DataObject
from bytecode.instruction import Instruction
from bytecode.inst_types import get_valid_opcodes
from compiler.backend.foreign_code.structures import *
from compiler.frontend.fds_parserVisitor import fds_parserVisitor
from dataclasses import dataclass
from objects.object import ForgeObject
from objects.num_obj import ForgeNumObject


class FDSVisitor(fds_parserVisitor):

  def __init__(self, program: Program, foreign_code_buffer: list[ForeignCodeSegment]):

    self.program: Program = program
    self.foreign_code_buffer: list[ForeignCodeSegment] = foreign_code_buffer

    if not isinstance(self.program, Program):
      raise TypeError(
        f"Invalid 'Program' object: '{self.program}', expected type 'Program'"
      )

    if not isinstance(self.foreign_code_buffer, list):
      raise TypeError(
        f"Invalid 'foreign_code_buffer' object: '{self.foreign_code_buffer}', expected type 'list'"
      )

  def emit_instr(
    self,
    opcode: str,
    oparg: int,
  ) -> int | None:
    
    if not opcode:
      raise ValueError(
        "instruction argument must not be falsy,"
          f"provided {opcode.__class__}"
      )

    if type(opcode) is not str:
      raise TypeError(
        "opcode argument must be of type 'str', "
          f"provided {opcode.__class__}"
      )

    if oparg is None:
      raise ValueError(
        "oparg argument should not be falsy, "
          f"provided '{oparg.__class__}'"
      )

    if type(oparg) is not int:
      raise TypeError(
        "oparg argument must be of type int, "
          f"provided '{oparg.__class__}'"
      )

    valid_opcodes = get_valid_opcodes()
    valid_opcode_names_list = valid_opcodes.keys()

    if (not opcode in valid_opcode_names_list):
      valid_opcode_names = ', '.join(valid_opcode_names_list)

      raise Exception(
        f"invalid opcode '{opcode}' provided, \
          expecting one from these:\n\t{valid_opcode_names}"
      )

    self.program.instructions.append(
      Instruction(
        opcode = valid_opcodes[opcode],
        op_arg = oparg
      )
    )

    return None


  def visitFrgnCode(self, ctx):
    self.foreign_code_buffer.append(
      Raw(
        text = ctx.getText()
      )
    )

  def visitFdsBlock(self, ctx):
    instr_start_index = len(self.program.instructions)
    
    for stmt in ctx.stmts:
      self.visit(stmt)

    self.emit_instr(
      opcode = "OP_HALT",
      oparg = 0
    )

    instr_end_index = len(self.program.instructions) - 1

    self.foreign_code_buffer.append(
      SectionCall(
        offset_start = instr_start_index,
        offset_end = instr_end_index
      )
    )

  def visitFdsInline(self, ctx):
    instr_start_index = len(self.program.instructions)
    
    self.visit(ctx.value)

    self.emit_instr(
      opcode = "OP_RET",
      oparg = 0
    )

    instr_end_index = len(self.program.instructions) - 1

    self.foreign_code_buffer.append(
      Embed(
        offset_start = instr_start_index,
        offset_end = instr_end_index
      )
    )


  def visitForeignBlock(self, ctx):
    self.foreign_code_buffer.append(
      Raw(
        text = ctx.getText()
      )
    )

  def visitAssignmentStmt(self, ctx):
    value = self.visit(ctx.value)
    
    if not isinstance(value, ForgeObject):
      raise TypeError(
        f"Invalid '{value}' of type '{type(value).__name__}', expected type 'ForgeObject'"
      )
    
    for target in ctx.targets:
      self.program.data = self.program.data._insert_dataobject(
        DataObject(
          type_=value.obtype,
          len_=len(value.to_bytes()),
          data_=value.to_bytes()
        )
      )

      self.emit_instr(
        opcode = "OP_PUSH",
        oparg = len(self.program.data.objects) - 1
      )

      self.emit_instr(
        opcode = "OP_STORE",
        oparg = int(target.text)
      )
  
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
    self.emit_instr(
      opcode = "OP_LOAD",
      oparg = int(ctx.getText()),
    )
  

  def visitThunk(self, ctx):
    self.foreign_code_buffer.append(
      Thunk(
        expr = ctx.getText()
      )
    )
  
"""
assignment:
	variable = VAR (EQUALS values += expr)+ # AssignmentStmt;
"""