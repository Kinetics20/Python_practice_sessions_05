import time
import functools


def timer(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        res = fn(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        print(f'[{fn.__name__}] calculated in {execution_time:.4f} sek.')

        return res

    return wrapper

@timer
def strong_computation(n):
    print(f'Counting primary number from {n}')
    time.sleep(0.5)
    return 997

strong_computation(1000)