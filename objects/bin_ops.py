from .object import ForgeObject, ForgeNotImplemented
from .obj_func_type_defs import binary_func
from typing import Callable


def __binop(func):
  def wrapper(left: ForgeObject, right: ForgeObject, op_slot: int):
    if not isinstance(left, ForgeObject):
      raise TypeError(
        f"Binary operation expected a 'ForgeObject' as left operand, got '{type(left).__name__}'"
      )
    
    if not isinstance(right, ForgeObject):
      raise TypeError(
        f"Binary operation expected a 'ForgeObject' as right operand, got '{type(right).__name__}'"
      )

    if not isinstance(op_slot, int) or not (0 < op_slot <= 3):
      raise ValueError(
        f"Binary operation expected 'op_slot' to be an int in the range of 1 to 3, got '{op_slot}'"
      )
    
    slot_l: binary_func | None = None
    slot_r: binary_func | None = None

    res = ForgeNotImplemented

    if hasattr(left, "binop_methods"):
      slot_l = left.binop_methods().get(f"0x{op_slot:x}", None)
    
    if hasattr(right, "binop_methods"):
      slot_r = right.binop_methods().get(f"0x{op_slot:x}", None)
    
    if slot_r is None:
      if slot_l is not None:
        res = slot_l(left, right)
    elif slot_l is None:
      if slot_r is not None:
        res = slot_r(left, right)
    
    if not (isinstance(res, ForgeObject) or res is None):
      raise TypeError(
        f"Binary operation expected a 'ForgeObject' or 'None' as return value, got '{type(res).__name__}'"
      )
    
    func(left, right, res)

  return wrapper


@__binop
def ForgeBinOp_Add(left: ForgeObject, right: ForgeObject, res: ForgeObject):
  if not (isinstance(left, ForgeObject) and isinstance(right, ForgeObject)):
    raise TypeError(
      f"BinOp expected operands of type 'ForgeObject', got '{type(left).__name__}' and '{type(right).__name__}'"
    )
  
  if not isinstance(res, ForgeObject):
    raise TypeError(
      f"BinOp returned an object of type '{type(res).__name__}', expected 'ForgeObject'"
    )
  
  if res == ForgeNotImplemented:
    raise Exception(
      f"unsupported operands for the '+' binary operation: '{left.type_str()}' and '{right.type_str()}'"
    )
  
  return res
