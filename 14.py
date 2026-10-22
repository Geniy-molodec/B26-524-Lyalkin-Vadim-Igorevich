from contextlib import contextmanager

@contextmanager
def log_operation(filename, operation):
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(f"START: {operation}\n")
        try:
            yield
        except Exception:
            f.write(f"ERROR: {operation}\n")
            raise
        else:
            f.write(f"END: {operation}\n")