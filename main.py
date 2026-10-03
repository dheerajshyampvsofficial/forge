import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
  sys.path.insert(0, str(PROJECT_ROOT))

from bytecode import Program
from bytecode.data import Data, DataObject
from bytecode.instruction import Instruction
from bytecode.inst_types import OP_LOAD, OP_RET

from interpreter import Interpreter

BYTECODE_FILE = PROJECT_ROOT / "my_first_program.fbc"
STRING_TYPE = 2


def build_program() -> Program:
  message = "Hello,world!".encode("utf-8")

  return Program(
    data=Data(
      objects=(
        DataObject(type_=STRING_TYPE, len_=len(message), data_=message),
      )
    ),
    instructions=[
      Instruction(opcode=OP_LOAD, op_arg=0),
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
  sys.exit(main(sys.argv[1:]))