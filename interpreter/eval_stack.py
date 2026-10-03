from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class EvalStack:
  __len: int = 0
  __top: int = -1
  __data: list = field(default_factory=list)

  __MAX_SIZE: ClassVar[int] = 2 ** 22

  def __post_init__(self):
    if type(self.__len) is not int:
      raise TypeError(
        "Evaluation Stack's len member must be of type int"
      )

    if type(self.__top) is not int:
      raise TypeError(
        "Evaluation Stack's top member must be of type int"
      )

    if not (-1 <= self.__top < self.__len):
      raise ValueError(
        f"Evaluation Stack's current index should be in the range of -1 to {(self.__len - 1)}, provided {self.__top}"
      )

    if type(self.__data) is not list:
      raise TypeError(
        "Evaluation Stack's data member must be of type list"
      )

  def push(self, elem: bytes):
    if not isinstance(elem, bytes):
      raise TypeError(
        f"push method expects an input of type 'bytes', got {type(elem).__name__}"
      )

    if self.__top >= self.__MAX_SIZE - 1:
      raise Exception("Evaluation stack max limit reached.")

    self.__top += 1
    self.__data.insert(self.__top, elem)

  def pop(self, idx: int | None = None):
    if idx is None:
      idx = self.__top

    if type(idx) is not int:
      raise TypeError(
        f"Evaluation Stack's pop method expects an input of type 'int' or 'None', got {type(idx).__name__}"
      )

    if not (-1 < idx <= self.__top):
      raise ValueError(
        f"Evaluation Stack's pop method expects a value within the range of 0 to {self.__top}, provided {idx}."
      )

    value = self.__data.pop(idx)
    self.__top -= 1
    return value