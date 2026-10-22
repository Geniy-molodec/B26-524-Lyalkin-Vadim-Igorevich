import time

class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Время выполнения: {self.elapsed} сек")
        return False
def some_function():
    time.sleep(1)
with Timer():
    some_function()