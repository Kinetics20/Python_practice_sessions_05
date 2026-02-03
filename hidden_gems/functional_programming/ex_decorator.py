from datetime import datetime


def upper(fn):
    def inner(name):
        # print(f'Function {fn.__name__} was called at {datetime.now()}')
        result = fn(name.title())
        return result
    return inner

def reverse(fn):
    def wrapper(name):
        return fn(name[::-1])
    return wrapper

@reverse
@upper
def say_hellow(name):
    return f'Hello {name}'

@reverse
@upper
def say_bye(name):
    return f'Bye {name}'

# print(say_hellow('mike'))
# print(say_bye('lech'))


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