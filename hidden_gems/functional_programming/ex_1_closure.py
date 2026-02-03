from collections.abc import Callable


def full_sentence(name):
    x = 42

    def sentence(city):
        value = x
        return f'My name is {name} and I live in {city}.'

    return sentence


# fs = full_sentence('Mike')
# print(fs)
# res = fs('London')
# res2 = fs('New York')
# print(res)
# print(res2)
# print(fs.__closure__[0].cell_contents)
# print(fs.__closure__[1].cell_contents)
# print(fs.__closure__)
# print(fs.__code__.co_freevars)


# uuid - universal unique id / 26 digits /

# def gen_id(id_ = 1):
#
#     def next_id(new_id = None):
#         nonlocal id_
#
#         if new_id is not None:
#             id_ = new_id
#
#
#         res = id_
#         id_ += 1
#         return res
#     return next_id


def gen_id(id_ = 1):
    def next_id(new_id=None):
        if new_id is not None:
            next_id.id_ = new_id

        res = next_id.id_

        next_id.id_ += 1

        return res
    next_id.id_ = id_
    return next_id


# next_gen = gen_id(42)
# print(next_gen())
# print(next_gen())
# print(next_gen(999))
# print(next_gen())
# print(next_gen.__closure__[0].cell_contents)


# factory function

def power_factory(exp: int) -> Callable:
    def power(x: int) -> int:
        return x ** exp
    return power

power4 = power_factory(4)
power5 = power_factory(5)
# print(power4(2))
# print(power5(2))

def min_length_validator(min_len: int) -> Callable[[str], bool]:
    def validate(value: str) -> bool:
        return len(value) >= min_len
    return validate

is_strong_pass = min_length_validator(14)
# is_strong_pass('1234567890qwerty')
print(is_strong_pass('1234567890'))

def memoize(fn: Callable[[int], int]) -> Callable[[int], int]:
    cache: dict[int, int] = {}

    def inner(x: int) -> int:
        if x not in cache:
            cache[x] = fn(x)

        return cache[x]
    return inner

@memoize
def square(x: int) -> int:
    print('computing ...')
    return x * x

print(square(10))
print(square(10))

# memoized_square = memoize(square)
# print(memoized_square(10))
# print(memoized_square(10))
# print(memoized_square.__closure__[0].cell_contents)
# print(memoized_square.__code__.co_freevars)