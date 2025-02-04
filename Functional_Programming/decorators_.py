
# def hello(name, a):
#     def inner():
#         return f'Hello {(" " + name.capitalize().swapcase()) * a}'
#     return inner
# x_fn = hello('ala ma kota', 3)
# print(x_fn())


def capitalize(fn):
    print('__capitalize__ outer')
    def inner(name):
        return fn(name.swapcase())
    return inner

def inverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner

# @inverse
@capitalize
@inverse
def hello(name):
    return f'Hello {name}'

@capitalize
def howdy(name):
    return f'howdy {name}'

# print(capitalize(inverse)(inverse(hello)('JoHn')))
print(hello('JoHn'))
print(howdy('PiPi is a ....'))




def multiply(fn):
    def inner(*args, c):
        return fn(*args) * c
    return inner

@multiply
def add(a, b):
    return a + b
result = add(1, 2, c=4)
# print(result)