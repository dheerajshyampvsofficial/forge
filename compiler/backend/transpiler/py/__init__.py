from compiler.backend import ForgeTranspiler
from pathlib import Path


import ast


curr_dir = Path(__file__).resolve().parent
py_template_file = curr_dir.parent / "templates" / "py.tmpl"


class PyASTManager(ast.NodeTransformer):
  def __init__(self, rootAST: ast.AST, segmentsAST: ast.AST):
    if not isinstance(rootAST, ast.AST):
      raise TypeError(
        f"root ast parameter must be of type 'ast.AST', provided {rootAST.__class__.__name__}"
      )
    
    if not isinstance(segmentsAST, ast.AST):
      raise TypeError(
        f"segments ast parameter must be of type 'ast.AST', provided {rootAST.__class__.__name__}"
      )
    
    self.rootAST = rootAST
    self.segmentsAST = segmentsAST

  def to_code(self):
    return ast.unparse(
      self.rootAST
    )
    

class PyTranspiler(ForgeTranspiler):
  def __init__(self, segmentProcessor: ForgeSegmentProcessor):
    super().__init__(segmentProcessor)

    if not py_template_file.exists():
      raise FileNotFoundError(
        f"Python template file not found at {py_template_file} to perform transpilation"
      )

    with open(py_template_file, "r") as f:
      self.py_template_text = f.read()
      if not self.py_template_text.endswith("\n"):
        self.py_template_text += "\n"
    
    segmentsCode = segmentProcessor.flush()

    if not segmentsCode:
      raise Exception("No code segments generated")
    if not isinstance(segmentsCode, str):
      raise Exception("Code segments are not strings")
    
    self.__segmentsProcessedAST = ast.parse(
      segmentsCode
    )

    self.__py_ast: ast.AST | None = ast.parse(
      self.py_template_text
    )

    self.__py_ast_manager = PyASTManager(
      rootAST = self.__py_ast,
      segmentsAST = self.__segmentsProcessedAST    
    )

    del segmentsCode


  def flush(self) -> str | None:
    return self.__process()
  

  def __process(self) -> str | None:
    if self.__py_ast is None:
      return self.__py_ast_manager.to_code()
    return None