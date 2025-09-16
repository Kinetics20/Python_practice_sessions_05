
def upper(fn):
    def inner(name):
        return fn(name.title())

    return inner


def reverse(fn):
    def inner(name):
        return fn(name[::-1])

    return inner

@reverse
@upper
def hello(name):
    return f'Hello, {name}!'

@upper
@reverse
def bye(name):
    return f'Bye, {name}!'

print(hello('John'))
print(bye('John'))