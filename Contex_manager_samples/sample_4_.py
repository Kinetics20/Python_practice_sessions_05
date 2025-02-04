from contextlib import contextmanager


@contextmanager
def propagator(name, propagate=True):
    try:
        yield
        print(f"{name}: done")
    except Exception:
        print(f"{name}: received exception")
        if propagate:
            raise


with propagator("outer", True), propagator("inner", True):
    raise Exception("yolo")
