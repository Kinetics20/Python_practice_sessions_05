class ContextManagerCustom:
    def __enter__(self):
        print("Entering context manager")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context manager")
        if exc_type is not None:
            print(f"Exception occurred: {exc_type.__name__}")
            return False
        return True

with ContextManagerCustom() as cm:
    raise Exception("Some exception")