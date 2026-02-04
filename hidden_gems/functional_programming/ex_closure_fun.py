def add_stars(fn):
    def wrapper(name):
        return f'***{fn(name)}***'

    return wrapper


def remove_spaces(fn):
    def wrapper(name):
        return fn(name.strip())

    return wrapper


@add_stars
@remove_spaces
def sth(name):
    return f'This is a {name}'


# print(sth('  Mike  '))

def odd(fn):
    def wrapper(x):
        return [i for i in fn(x) if not i % 2]

    return wrapper


def power(fn):
    def wrapper(x):
        return [i ** i for i in fn(x)]

    return wrapper


def higher_3(fn):
    def wrapper(x):
        return [i for i in fn(x) if i > 3]

    return wrapper


@odd
@power
@higher_3
def generator_list(num):
    return list(range(num))


print(generator_list(10))
print(globals())
print('-|-' * 20)
print(locals())
