import types


def tramp(gen, *args, **kwargs):
    g = gen(*args, **kwargs)

    while isinstance(g, types.GeneratorType):
        g = next(g)

    return g


# big O: 2 ** n
def f(n):
    if n <= 0:
        return n
    else:
        return f(n - 1) + f(n - 2)


# print(f(5))

def ft(n, curr=0, next_=1):
    if n == 0:
        yield curr
    else:
        yield ft(n - 1, next_, curr + next_)

import sys
sys.set_int_max_str_digits(20899)
# print(tramp(ft, 100_000))
# print(f(10))


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# print(fib(100_000))


def remove(text: str, chars: str) -> str:
    if chars:
        return remove(
            text.replace(chars[0], ''),
            chars[1:]
        )
    return text

# print(remove('ala ma kota ?!', '?!'))

