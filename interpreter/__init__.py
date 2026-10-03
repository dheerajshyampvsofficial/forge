from __future__ import annotations
from bytecode import Program
from typing import TYPE_CHECKING
from bytecode.data import DataObject
from objects.object import ForgeObject, ForgeNotImplemented
from objects.obj_ops_mapping import ForgeEval_BinaryOps
from .eval_stack import EvalStack

import bytecode.inst_types as inst_types


class Interpreter:

  def __init__(self, program: Program):
    self.program = program
    self.__eval_stack = EvalStack()

  def run(self):
    if self.program.header.payload_size == 0:
      return

    instructions = self.program.instructions

    for instr in instructions:
      opcode = instr.opcode
      oparg = instr.op_arg

      match opcode:
        case inst_types.OP_LOAD:
          objects_len = len(self.program.data.objects)
          max_idx = (objects_len - 1) if objects_len > 0 else 0

          if not (-1 < oparg <= max_idx):
            raise ValueError(
              f"LOAD instruction oparg: '{oparg}', is out of bounds for DataObjects tuple. Max-Index: '{max_idx}'"
            )

          elem = self.program.data.objects[oparg]
          self.__eval_stack.push(elem)

        case inst_types.OP_BINOP:
          if oparg not in range(1, 4):
            raise Exception(
              f"BinOp expects oparg between the range 1 to 3, got {oparg} instead."
            )
          
          right_operand: ForgeObject = self.__eval_stack.pop()
          left_operand: ForgeObject = self.__eval_stack.pop()

          binop = ForgeEval_BinaryOps.get(f"0x{oparg:x}", None)
          if binop is None:
            raise Exception(
              f"Unsupported binary operation: '{oparg}'"
            )
          
          res = binop(left_operand, right_operand, oparg)

          if not isinstance(res, ForgeObject):
            raise TypeError(
              f"BinOp handler returned an object of type '{type(res).__name__}', expected type 'ForgeObject'."
            )

          self.__eval_stack.push(res)

        case inst_types.OP_RET:
          if not self.__eval_stack.is_empty():
            print(f"Returning: '{self.__eval_stack.pop()}'")

        case _:
          raise ValueError("invalid opcode found")
