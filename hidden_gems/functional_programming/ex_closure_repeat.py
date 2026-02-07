def repeat(_fn=None, *, times=1):
    def decorator_fn(fn):
        def wrapper(*args):
            res = None
            for _ in range(times):
                res = fn(*args)
            return res

        return wrapper

    if _fn is None:
        return decorator_fn

    return decorator_fn(_fn)


@repeat(times=3)
def greet(name):
    print(f'Hello, {name}')


@repeat
def greet_2(name):
    print(f'Hello, {name}')


greet('Mike')
greet_2('Anna')
