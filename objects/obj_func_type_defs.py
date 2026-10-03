
from typing import Callable, TypeAlias
from .object import ForgeObject

binary_func: TypeAlias = Callable[[ForgeObject, ForgeObject], ForgeObject | None]