
from dataclasses import dataclass
from enum import Enum

class ForgeAST_NodeType(Enum):
  GENERIC = 0
  REGION = 1

class ForgeAST_Node:
  def __init__(self):
    self.ntype = ForgeAST_NodeType.GENERIC

class ForgeAST_RegionNode(ForgeAST_Node):
  def __init__(self, name: str, body: list[ForgeAST_Node]):
    self.ntype = ForgeAST_NodeType.REGION
    self.name = name
    self.body = body