from __future__ import annotations

import time
from functools import wraps
from typing import (
    Any,
    Callable,
)


def time_it(func: Callable) -> Any:
    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {(end - start) * 1000:04f} ms")
        return res

    return inner
