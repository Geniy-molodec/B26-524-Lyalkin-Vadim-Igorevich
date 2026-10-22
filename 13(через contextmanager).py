import time
from contextlib import contextmanager

@contextmanager
def Timer():
    start = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start
        print(f"Время выполнения: {elapsed} сек")
def some_function():
    time.sleep(1)
with Timer():
    some_function()