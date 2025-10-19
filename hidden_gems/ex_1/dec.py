from functools import wraps


def my_decorator(func):
    @wraps(func)
    def inner(*args, **kwargs):
        """Docstring for inner."""
        return func(*args, **kwargs)
    return inner


@my_decorator
def magic():
    """Docstring for magic."""
    return 42

print(magic.__name__)
print(magic.__doc__)
print(magic.__annotations__)