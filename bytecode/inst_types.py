OP_LOAD = 0x01
OP_ADD = 0x02
OP_MATMUL = 0x03
OP_RET = 0x04

def get_valid_opcodes():
  return dict(
    (key, value)
    for key, value in globals().items()
      if key.startswith("OP_")
        and key.isupper()
  )

def get_valid_opcodes_range():
  return tuple(
    value
      for key, value in globals().items()
        if key.startswith("OP_")
          and key.isupper()
  )