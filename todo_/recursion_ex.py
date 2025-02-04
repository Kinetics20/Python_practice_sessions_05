import types


def sum_(n):
    if n == 0:
        return n
    else:
        return n + sum_(n - 1)

def sum_1(n, acc=0):
    if n == 0:
        return acc
    else:
        return sum_(n - 1, acc + n)


def tramp(gen, *arg, **kwarg):
    g = gen(*arg, **kwarg)

    while isinstance(g, types.GeneratorType):
        g = next(g)

    return g


def f(n):
    if n <= 1:
        return n
    else:
        return f(n-1) + f(n-2)


def ft(n, curr=0, next_=1):
    if n == 0:
        yield curr
    else:
        yield from ft(n-1,next_, curr + next_ )

print(tramp(ft, 100))
print(f( 10))

def fib(n):
  a, b = 0, 1
  for _ in range(n):
    a, b = b, a + b
  return a

def remove(txt: str, char: str) -> str:
    if char:
        return remove(
            txt.replace(char[0], ''),
            char[1:]

        )
    return txt


import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)

print(sum_(1000))