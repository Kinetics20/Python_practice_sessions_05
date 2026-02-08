from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, ParamSpec, overload
import time

P = ParamSpec('P')
R = TypeVar('R')


def cache_with_ttl(_func: Callable[P, R] | None = None, *, seconds: float = 180.0):
    def decorator(func: Callable[P, R]):
        cache: dict[Any, tuple[float, R]] = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()

            if key in cache:
                timestamp, value = cache[key]
                if now - timestamp < seconds:
                    return value

            res = func(*args, **kwargs)
            cache[key] = (now, res)

            return res

        return wrapper
    if _func is None:
        return decorator

    return decorator(_func)