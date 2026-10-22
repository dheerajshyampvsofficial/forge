from __future__ import annotations

from typing import Union

import numpy as np
import cupy as cp

from cuda_jit.compiler import get_kernel
from cuda_jit.launcher import launch_elementwise
from cuda_jit.translate import supported_ops, supported_dtypes

_NUMPY_DTYPES: dict[str, np.dtype] = {
    "float32": np.dtype("float32"),
    "float64": np.dtype("float64"),
    "int32":   np.dtype("int32"),
}

_INTEGER_DTYPES = {"int32"}

Scalar = Union[int, float]


def _validate_op(op: str) -> None:
    if op not in supported_ops():
        raise ValueError(f"Unknown op '{op}'. Supported ops: {', '.join(sorted(supported_ops()))}.")


def _validate_dtype(dtype: str) -> None:
    if dtype not in supported_dtypes():
        raise TypeError(f"Unsupported dtype '{dtype}'. Supported dtypes: {', '.join(sorted(supported_dtypes()))}.")


def scalar_binop(op: str, a: Scalar, b: Scalar, dtype: str = "float32") -> Scalar:
    _validate_op(op)
    _validate_dtype(dtype)

    if op == "div" and dtype in _INTEGER_DTYPES and b == 0:
        raise ZeroDivisionError("Integer division by zero.")

    np_dtype = _NUMPY_DTYPES[dtype]
    a_arr = cp.array([a], dtype=np_dtype)
    b_arr = cp.array([b], dtype=np_dtype)

    out = launch_elementwise(get_kernel("binop", op, dtype), a_arr, b_arr, dtype)
    return int(out.item()) if dtype in _INTEGER_DTYPES else float(out.item())
