_U32_MAX = 0xFFFF_FFFF

def ensure_u32(name: str, value) -> int:
  if isinstance(value, bool) or not isinstance(value, int):
    raise TypeError(f"{name} must be an integer, got {type(value).__name__}")
  value = int(value)
  if not 0 <= value <= _U32_MAX:
    raise ValueError(f"{name} must be in 0..{_U32_MAX}, got {value}")
  return None