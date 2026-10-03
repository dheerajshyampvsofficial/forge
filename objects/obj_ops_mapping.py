from .num_obj import ForgeNumObject
from .bin_ops import ForgeBinOp_Add

ForgeObject_ResolverFromBytes = {
  "0x3": ForgeNumObject.from_bytes
}

ForgeEval_BinaryOps = {
  "0x1": ForgeBinOp_Add
}
