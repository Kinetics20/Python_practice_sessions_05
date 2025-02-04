from datetime import datetime


def reverse(fn):
    def inner(name):
        result = fn(name.swapcase()[::-1])
        return result
    return inner

def upper(fn):
    def inner(name):
    # def inner(*args, **kwargs):
    #     print(f'Function {fn.__name__} was called at {datetime.now()}')
        # result = fn(*args, **kwargs)
        result = fn(name.capitalize())
        return result
        # return 'dupa'
    return inner



# @reverse
@upper
@reverse
def say_hello(name):

    return f'Hello {name}'

@upper
def say_buy(name):

    return f'Bye {name}'


# print(say_hello('jaroslaw'))
# print(say_buy('Lech'))

# memoizing

def cache(fn):
    memo = {}
    print('cache', 20 * '-')
    def wrapper(*args):
        if args not in memo:
            print('save', 20 * '#')
            memo[args] = fn(*args)
        return memo[args]

    return wrapper

@cache
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(10))
print(factorial(10))


class X:
    def __init__(self):
        self._value = 42

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        self._value = new_val
