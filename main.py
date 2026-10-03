import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
  sys.path.insert(0, str(PROJECT_ROOT))

from bytecode import Program
from bytecode.data import Data, DataObject
from bytecode.instruction import Instruction
from bytecode.inst_types import OP_LOAD, OP_BINOP, OP_RET
from compiler import ForgeCompiler
from objects.num_obj import ForgeNumObject

from interpreter import Interpreter

BYTECODE_FILE = PROJECT_ROOT / "my_first_program.fbc"

def build_program() -> Program:
  numObj1 = ForgeNumObject(
    value = float(300)
  )

  numObj2 = ForgeNumObject(
    value = float(300)
  )

  return Program(
    data=Data(
      objects=(
        DataObject(
          type_=numObj1.obtype,
          len_=len(numObj1.to_bytes()),
          data_=numObj1.to_bytes()
        ),
        DataObject(
          type_=numObj2.obtype,
          len_=len(numObj2.to_bytes()),
          data_=numObj2.to_bytes()
        )
      )
    ),
    instructions=[
      Instruction(opcode=OP_LOAD, op_arg=0),
      Instruction(opcode=OP_LOAD, op_arg=1),
      Instruction(opcode=OP_BINOP, op_arg=1),
      Instruction(opcode=OP_RET, op_arg=0),
    ],
  )

def generate_bytecode(path: Path = BYTECODE_FILE) -> None:
  program_bytes = build_program()._export()

  tmp_path = path.with_suffix(path.suffix + ".tmp")
  tmp_path.write_bytes(program_bytes)
  tmp_path.replace(path)

def read_bytecode(path: Path = BYTECODE_FILE) -> Program | None:
  try:
    program_bytes = path.read_bytes()
  except FileNotFoundError:
    print(f"Bytecode file '{path}' not found. Run with --generate first.", file=sys.stderr)
    return None

  try:
    program = Program.from_bytes(program_bytes)
  except Exception as e:
    print(e, file=sys.stderr)
    return None

  return program


def main(argv: list[str]) -> int:
  if "--generate" in argv:
    generate_bytecode()

  program = read_bytecode()
  if program is None:
    return -1

  interpreter = Interpreter(
    program = program
  )

  interpreter.run()


if __name__ == "__main__":
  # sys.exit(main(sys.argv[1:]))
  global input_text

  with open(PROJECT_ROOT / "compiler/samples/one.fds") as f:
    input_text = f.read()
  
  compiler = ForgeCompiler()
  compiler.input_text = input_text
  compiler.parse()

  sys.exit(0)