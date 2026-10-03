import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
  sys.path.insert(0, str(PROJECT_ROOT))

from compiler import ForgeCompiler
from interpreter import Interpreter

BYTECODE_FILE = PROJECT_ROOT / "my_first_program.fbc"

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


def main() -> int:

  program = read_bytecode()
  if program is None:
    return -1

  interpreter = Interpreter(
    program = program
  )

  interpreter.run()


if __name__ == "__main__":
  global input_text

  with open(PROJECT_ROOT / "compiler/samples/one.fds") as f:
    input_text = f.read()
    if not input_text.endswith("\n"):
      input_text += "\n"
  
  compiler = ForgeCompiler()
  compiler.input_text = input_text
  
  program, transpiled_code = compiler.compile()

  print(transpiled_code)
  print(
    '\n'.join(
      (
        f'{i}. {instruction!r}'
          for i, instruction in enumerate(
            program.instructions,
            0
          )
        )
    )
  )

