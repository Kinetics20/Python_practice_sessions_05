from contextlib import contextmanager


@contextmanager
def yolo():
    # __enter__
    print("entering")
    try:
        yield "y"
    except Exception:
        print("error exiting")
    finally:
        print("exiting")


with yolo() as y:
    print(y)
    raise ValueError()
