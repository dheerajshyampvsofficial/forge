from __future__ import annotations

import math

import cupy as cp

_THREADS_1D = 256


def launch_elementwise(kernel: cp.RawKernel, a: cp.ndarray, b: cp.ndarray, dtype: str) -> cp.ndarray:
    n = a.size
    out = cp.empty(a.shape, dtype=dtype)
    if n == 0:
        return out
    blocks = math.ceil(n / _THREADS_1D)
    kernel((blocks,), (_THREADS_1D,), (a, b, out, cp.int32(n)))
    return out
