from Unit_tests.codewars_functions_ import identity_1


def sth():
    for i in range(10):
        print('Home')
        yield from range(i)


a = sth()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

for item in a:
    print(item)


def gc():
    id = 0

    def next_():
        nonlocal id
        id += 1
        return id

    return next_


def gg():
    id_ = 0

    while True:
        yield id_
        id_ += 1

id_gen = gg()

x1 = [1, 2, 3]
y1 = [1, 2, 3]

r = map(lambda a, b: a * b, x1, y1)
print(list(r))

print(range(10))
print([range(10)])
print(list(range(10)))
print([x for x in range(10)])