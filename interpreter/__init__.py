from __future__ import annotations
from bytecode import Program
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
          elem = self.program.data.objects[oparg]
          self.__eval_stack.push(elem._export())

          print(self.__eval_stack)

        case inst_types.OP_RET:
          pass

        case _:
          raise ValueError("invalid opcode found")
