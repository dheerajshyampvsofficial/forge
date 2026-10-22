_OP_SYMBOLS: dict[str, str] = {
    "add": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
}

_DTYPE_TYPES: dict[str, str] = {
    "float32": "float",
    "float64": "double",
    "int32":   "int",
}

_BINOP_TEMPLATE = """\
extern "C" __global__
void {func_name}(const {T}* a, const {T}* b, {T}* out, int n) {{
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) out[i] = a[i] {SYMBOL} b[i];
}}
"""


def translate_binop(op: str, dtype: str) -> str:
    if op not in _OP_SYMBOLS:
        raise ValueError(f"Unknown op '{op}'. Supported ops: {', '.join(sorted(_OP_SYMBOLS))}.")
    if dtype not in _DTYPE_TYPES:
        raise TypeError(f"Unsupported dtype '{dtype}'. Supported dtypes: {', '.join(sorted(_DTYPE_TYPES))}.")
    return _BINOP_TEMPLATE.format(
        func_name=f"{op}_{dtype}",
        T=_DTYPE_TYPES[dtype],
        SYMBOL=_OP_SYMBOLS[op],
    )


def supported_ops() -> tuple[str, ...]:
    return tuple(_OP_SYMBOLS)


def supported_dtypes() -> tuple[str, ...]:
    return tuple(_DTYPE_TYPES)
