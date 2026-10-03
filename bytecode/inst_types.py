OP_LOAD = 0x01
OP_STORE = 0x02
OP_BINOP = 0x03
OP_PUSH = 0x04
OP_RET = 0x05
OP_HALT = 0x06

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