import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        res = func(*args, **kwargs)  # call func
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f'-----------------\nfinished {func.__name__} in {run_time:.4f} sec')
        return res

    return wrapper_timer
