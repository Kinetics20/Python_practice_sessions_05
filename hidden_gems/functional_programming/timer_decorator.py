import time
import functools


def timer(func):
    functools.wraps(func)

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        execution_time = end_time - start_time
        print(f'[{func.__name__}] made in {execution_time:.4f} sek.')
        return result

    return wrapper


@timer
def heavy_computation(n):
    print('Counting primary number from n')
    time.sleep(0.5)
    return 997


heavy_computation(100)
