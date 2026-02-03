def add_stars(fn):
    def wrapper_stars(name):
            return f'***{fn(name)}***'
    return wrapper_stars


def add_brackets(cb):
    def wrapper(name):
        return f'[ {cb(name)} ]'
    return wrapper


def uppercase(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper


@add_stars
@add_brackets
@uppercase
def greet(name):
    return f'Hello, {name}'

@uppercase
@add_brackets
@add_stars
def greet_2(name):
    return f'Hello, {name}'

print(greet.__name__)
print(greet('Mike'))
print(greet_2('Johny'))