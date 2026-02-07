def add_stars(fn):
    def wrapper_stars(name):
        return f'iii {fn(name)} ***'

    return wrapper_stars


def add_brackets(fn):
    def wrapper(name):
        return f'[ {fn(name)} ]'

    return wrapper


def add_upper(fn):
    def wrapper(name):
        return fn(name).upper()

    return wrapper


def add_reverse(fn):
    def wrapper(name):
        return fn(name)[::-1]

    return wrapper


@add_stars
@add_brackets
@add_upper
def greet_2(name):
    return f'Hello, {name}'


@add_upper
@add_brackets
@add_stars
def greet(name):
    return f'Hello, {name}'


print(greet_2.__name__)
print(greet_2('Daxi'))
print(greet('Marcus'))
