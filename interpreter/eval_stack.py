from dataclasses import dataclass, field
from typing import ClassVar
from objects.object import ForgeObject
from objects.obj_ops_mapping import ForgeObject_ResolverFromBytes

import bytecode.data as bc_data


@dataclass
class EvalStack:
  __len: int = 0
  __top: int = -1
  __data: list = field(default_factory=list)

  __MAX_SIZE: ClassVar[int] = 100

  def __post_init__(self):
    if type(self.__len) is not int:
      raise TypeError(
        f"Evaluation Stack's len member must be of type int, got {self.__len.__class__.__name__}"
      )

    if type(self.__top) is not int:
      raise TypeError(
        f"Evaluation Stack's top member must be of type int, got {self.__top.__class__.__name__}"
      )

    if type(self.__MAX_SIZE) is not int:
      raise TypeError(
        f"Evaluation Stack's MAX_SIZE member must be of type int, got {self.__MAX_SIZE.__class__.__name__}"
      )

    if self.__MAX_SIZE != 100:
      raise ValueError(
        f"Evaluation Stack's MAX_SIZE must bes strictly equal to 100, got {self.__MAX_SIZE}"
      )

    if not(0 <= self.__len <= self.__MAX_SIZE):
      raise ValueError(f"Evaluation stack length must be strictly in the range of 0 to {self.__MAX_SIZE}, got {self.__len}")

    if not (-1 <= self.__top < self.__len):
      raise ValueError(
        f"Evaluation Stack's current index should be in the range of -1 to {(self.__len - 1)}, provided {self.__top}"
      )

    if type(self.__data) is not list:
      raise TypeError(
        f"Evaluation Stack's data member must be of type list, got {self.__data.__class__.__name__}"
      )
    
    for idx, elem in enumerate(self.__data):
      if type(elem) is not bc_data.DataObject:
        raise TypeError(
          f"Evaluation Stack's data member must contain elements of type 'DataObject', got {elem.__class__.__name__} at index {idx}"
        )
  
  def is_empty(self) -> bool:
    return self.__len == 0
  
  def __push_forge_object(self, obj: ForgeObject):
    if self.__len >= self.__MAX_SIZE:
      raise Exception("Evaluation stack max limit reached.")
    
    self.__top += 1
    self.__len += 1

    self.__data.insert(self.__top, obj)
  
  def __push_data_object_as_forge_object(self, elem: bc_data.DataObject):
    if type(elem) is not bc_data.DataObject:
      raise TypeError(
        f"push method expects an input of type 'DataObject', got {type(elem).__name__}"
      )
    
    self.__push_forge_object(ForgeObject.from_bytes(
      fo_bytes=elem.data_,
      resolver=ForgeObject_ResolverFromBytes[f"0x{elem.type_:x}"]
    ))

  def push(self, elem: bc_data.DataObject | ForgeObject):
    """
    Pushes the DataObject provided to the top.
    Current Implementation: top increases along with the len
    Next Implementation idea: gets peek() capability, so, top does not always gets incremented with len during push, allowing forward/backward seeking access to stack elements.
    """

    if isinstance(elem, bc_data.DataObject):
      self.__push_data_object_as_forge_object(elem)
    elif isinstance(elem, ForgeObject):
      self.__push_forge_object(elem)
    else:
      raise TypeError(
        f"push method expects an input of type 'DataObject' or 'ForgeObject', got {type(elem).__name__}"
      )
    

  def pop(self) -> ForgeObject:
    """
    Pops the topmost DataObject from it.
    Current Implementation: top reduces along with the len
    Next Implementation idea: gets peek() capability, so, top does not always gets decremented with len during pop, allowing non-destructive access to stack elements.
    """

    idx = (self.__len - 1) if self.__len != 0 else -1

    if not (-1 < idx < self.__len):
      raise ValueError(
        f"Evaluation Stack's pop method expects a value within the range of 0 to {(self.__len - 1)}, provided {idx}."
      )

    value = self.__data.pop(idx)

    if not isinstance(value, ForgeObject):
      raise TypeError(
        f"pop method must return an element of type 'ForgeObject', but got {type(value).__name__} at {idx}."
      )

    self.__top -= 1
    self.__len -= 1
    
    return value

  def _format(self, indent_level: int = 0) -> str:
    indent = "  " * indent_level
    field_indent = "  " * (indent_level + 1)
    return (
      f"Evaluation Stack(\n"
      f"{field_indent}len = {self.__len},\n"
      f"{field_indent}top = {self.__top},\n"
      f"{field_indent}data = {self.__data}\n"
      f"{indent})"
    )

  def __str__(self) -> str:
    return self._format()