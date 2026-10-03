from antlr4 import InputStream, CommonTokenStream, TerminalNode
from bytecode import Program, Data

from .frontend.fds_lexer import fds_lexer
from .frontend.fds_parser import fds_parser
from .frontend.fds_visitor import FDSVisitor

class ForgeCompiler:
  def __init__(self):
    self.input_text: str
  
  def format_tree(self, node, parser, indent=0):
    pad = "  " * indent

    if isinstance(node, TerminalNode):
        return pad + node.getText()

    rule = parser.ruleNames[node.getRuleIndex()]
    children = list(node.getChildren())

    if not children:
        return f"{pad}({rule})"

    lines = [f"{pad}({rule}"]

    for child in children:
        lines.append(self.format_tree(child, parser, indent + 1))

    lines[-1] += ")"
    return "\n".join(lines)

  def parse(self):
    input_stream = InputStream(self.input_text)
    lexer = fds_lexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    token_stream.fill()

    parser = fds_parser(token_stream)

    tree = parser.start()

    # print(self.format_tree(tree, parser))

    program = Program(data = Data())
    
    visitor = FDSVisitor(
      program = program
    )
    
    visitor.visit(tree)
    
    return program