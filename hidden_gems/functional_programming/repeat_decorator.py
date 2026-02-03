def repeat(_func=None, *, times=1):
    def decorator_repeat(fn):
        def wrapper(name):
            result = None
            for _ in range(times):
                result = fn(name)
            return result

        return wrapper

    if _func is None:
        return decorator_repeat
    return decorator_repeat(_func)


@repeat(times=3)
def greet(name):
    print(f'Hello, {name}')


@repeat
def greet_2(name):
    print(f'Hello, {name}')


greet('Mike')
greet_2('Johny')
