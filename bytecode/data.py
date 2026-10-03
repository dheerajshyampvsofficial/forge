import struct

from dataclasses import dataclass
from typing import ClassVar, Final

DATA_STRUCT_: Final = struct.Struct("<I")

@dataclass(frozen=True)
class DataObject:
  type_: int = -1
  len_: int = 0
  data_: bytes | None = None

  STRUCT_: ClassVar[struct.Struct] = struct.Struct("<II")

  def _export(self) -> bytes:
    if not (type(self.type_) is int):
      raise TypeError("type member type of 'DataObject' must be of type 'int'")

    if not (0 <= self.type_ <= 0xFFFFFFFF):
      raise ValueError("type must be an unsigned 32-bit integer")

    if self.type_ <= 1:
      raise ValueError("Generic DataObject is not allowed to be exported as bytes")

    if (self.data_ is None):
      raise TypeError("data should not be None")

    if not isinstance(self.data_, bytes):
      raise TypeError("data must be bytes")

    if not type(self.len_) is int:
      raise TypeError("len member type of DataObject must be of type 'int'")

    if self.len_ != len(self.data_):
      raise ValueError("len member value must be equal to actual data member contents size")

    if self.len_ == 0:
      raise ValueError("zero-length DataObject payloads are not allowed")

    if not 0 <= self.len_ <= 0xFFFFFFFF:
      raise ValueError("len must be an unsigned 32-bit integer")

    return self.STRUCT_.pack(self.type_, self.len_) + self.data_

  @classmethod
  def _parse_data_object_in_large_buffer(cls, do_buffer: bytes, offset: int) -> tuple["DataObject", int]:
    if type(offset) is not int:
      raise TypeError("offset must be a int")

    if offset < 0:
      raise ValueError("offset must be non-negative")
    
    do_header_end = offset + cls.STRUCT_.size

    if len(do_buffer) < do_header_end:
      raise ValueError("truncated DataObject found - header")

    type_, len_ =  cls.STRUCT_.unpack_from(do_buffer, offset)

    if type_ <= 1:
      raise ValueError("invalid DataObject type")

    if len_ == 0:
      raise ValueError("zero-length DataObject payloads are not allowed")

    payload_end = do_header_end + len_
    if len(do_buffer) < payload_end:
      raise ValueError("truncated DataObject found - objects")

    return cls(
      type_=type_,
      len_=len_,
      data_= do_buffer[do_header_end : payload_end]
    ), payload_end

  @classmethod
  def from_bytes(cls, do_bytes: bytes) -> "DataObject":
    if not isinstance(do_bytes, bytes):
      raise TypeError("do_bytes must be of type bytes")

    obj, end = cls._parse_data_object_in_large_buffer(do_bytes, 0)
    if end != len(do_bytes):
      raise ValueError("trailing bytes after DataObject")
    return obj

@dataclass(frozen=True)
class Data:
  objects: tuple[DataObject, ...] | None = None

  def _export(self) -> bytes:
    if not self.objects:
      raise ValueError("'Data' must contain at least one 'DataObject'")

    if not isinstance(self.objects, tuple):
      raise TypeError("'objects' member must be a tuple")

    if not all(isinstance(obj, DataObject) for obj in self.objects):
      raise TypeError("contents in objects tuple of 'Data' class, must be of type 'DataObject'")

    if len(self.objects) > 100:
      raise ValueError("Data cannot contain more than 100 objects")

    raw_objects = b"".join(obj_._export() for obj_ in self.objects)
    return DATA_STRUCT_.pack(len(self.objects)) + raw_objects

  @classmethod
  def from_bytes(cls, data_bytes: bytes) -> "Data":
    if not isinstance(data_bytes, bytes):
      raise TypeError("data_bytes must be bytes")

    if len(data_bytes) < DATA_STRUCT_.size:
      raise ValueError("truncated Data object - header")

    obj_count_offset = DATA_STRUCT_.size

    obj_count = DATA_STRUCT_.unpack_from(
      data_bytes, 0
    )[0]

    if obj_count <= 0:
      raise ValueError("Data must contain at least one 'DataObject'")

    if obj_count > 100:
      raise ValueError("DataObject's count exceeds maximum of 100")

    obj_offset = obj_count_offset
    objects = []

    for _ in range(obj_count):
      dataObject, obj_offset = DataObject._parse_data_object_in_large_buffer(
        data_bytes,
        obj_offset
      )
      objects.append(dataObject)

    if obj_offset != len(data_bytes):
      raise ValueError("invalid trailing bytes after the final 'DataObject'")

    return cls(objects=tuple(objects))
  