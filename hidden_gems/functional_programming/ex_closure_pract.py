from functools import reduce


def odd_list(fn):
    def wrapper(*args):
        return [x for x in fn(*args) if x  % 2]
    return wrapper

def make_len(fn):
    def wrapper(*args):
        return len(fn(*args))
    return wrapper

def make_list(fn):
    def wrapper(*args):
        return list(range(fn(*args)))
    return wrapper

# @make_len
@odd_list
@make_list
def make_add(*args):
    return sum(args)

@odd_list
@make_list
def make_add_fn(*args):
    return reduce(lambda x, y: x * y, args)

def add_prefix(prefix):
    def wrapper(name):
        return f'{prefix} {name}'
    return wrapper

# print(make_add(1, 2, 3, 10))
# print(make_add_fn(1, 2, 3))

new_prefix = add_prefix('Howdy')
# print(new_prefix('Mike'))
# print(new_prefix('Agnes'))

def text_formatter(mode):
    def wrapper(text):
        if mode == 'upper':
            return text.upper()
        elif mode == 'lower':
            return text.lower()
        return text
    return wrapper

a = text_formatter('upper')('Home sweet home')
# print(a)

def add_exclamation(fn):
    def wrapper(*args):
        return f'{fn(*args)} !'
    return wrapper

def upper_result(fn):
    def wrapper(*args):
        return fn(*args).upper()
    return wrapper

@add_exclamation
@upper_result
def greet(name: str) -> str:
    return f"Hello, {name}"

# print(greet('John'))


def repeat(_fn=None, *, n=1):
    def decorator(fn):
        def wrapper(*args):
            res = []
            for _ in range(n):
                res.append(fn(*args))

            return ' | '.join(res)
        return wrapper

    if _fn is None:
        return decorator

    return decorator(_fn)


@repeat(n=3)
def say(text: str) -> str:
    return text

print(say('Hello'))