import sys
import re
import cupy as cp

from cuda_jit.compiler import get_kernel
from cuda_jit.launcher import launch_elementwise
from cuda_jit.ops import _validate_op, _validate_dtype, _INTEGER_DTYPES


def parse_input(arg_str: str):
    tokens = [t for t in re.split(r'[,\s]+', arg_str.strip()) if t]
    if len(tokens) < 3:
        print("Usage: python execute.py \"<op> <a>,<b> [dtype]\"")
        sys.exit(1)

    op, a_raw, b_raw = tokens[0].lower(), tokens[1], tokens[2]
    dtype = tokens[3].lower() if len(tokens) >= 4 else "float32"

    a = float(a_raw) if "." in a_raw or "float" in dtype else int(a_raw)
    b = float(b_raw) if "." in b_raw or "float" in dtype else int(b_raw)
    return op, a, b, dtype


def fmt(val):
    return int(val) if isinstance(val, (int, float)) and val == int(val) else val


def main():
    if len(sys.argv) < 2:
        print("Usage: python execute.py \"<op> <a>,<b> [dtype]\"")
        sys.exit(1)

    op, a, b, dtype = parse_input(" ".join(sys.argv[1:]))

    _validate_op(op)
    _validate_dtype(dtype)
    if op == "div" and dtype in _INTEGER_DTYPES and b == 0:
        raise ZeroDivisionError("Integer division by zero.")

    props = cp.cuda.runtime.getDeviceProperties(0)
    dev_name = props["name"].decode() if isinstance(props["name"], bytes) else props["name"]

    a_gpu = cp.array([a], dtype=dtype)
    b_gpu = cp.array([b], dtype=dtype)
    kernel = get_kernel("binop", op, dtype)

    start_event = cp.cuda.Event()
    end_event = cp.cuda.Event()

    start_event.record()
    out = launch_elementwise(kernel, a_gpu, b_gpu, dtype)
    end_event.record()
    end_event.synchronize()

    elapsed_ms = cp.cuda.get_elapsed_time(start_event, end_event)
    result = int(out.item()) if dtype in _INTEGER_DTYPES else float(out.item())

    print(f"Task:      {op}({fmt(a)}, {fmt(b)}) [{dtype}]")
    print(f"GPU:       {dev_name} (256 threads)")
    print(f"Time:      {elapsed_ms:.3f} ms")
    print(f"Result:    {fmt(result)}")


if __name__ == "__main__":
    main()
