from __future__ import annotations

import threading
from typing import Optional

import cupy as cp

from cuda_jit.translate import translate_binop

_cache: dict[tuple[str, Optional[str], str], cp.RawKernel] = {}
_cache_lock = threading.Lock()


def get_kernel(kind: str, op: Optional[str], dtype: str) -> cp.RawKernel:
    key = (kind, op, dtype)
    with _cache_lock:
        if key in _cache:
            return _cache[key]
        if kind == "binop":
            if op is None:
                raise ValueError("op must not be None for kind='binop'.")
            source = translate_binop(op, dtype)
            func_name = f"{op}_{dtype}"
        else:
            raise ValueError(f"Unknown kernel kind '{kind}'.")
        kernel = cp.RawKernel(source, func_name)
        _cache[key] = kernel
        return kernel


def cache_size() -> int:
    with _cache_lock:
        return len(_cache)


def clear_cache() -> None:
    with _cache_lock:
        _cache.clear()
