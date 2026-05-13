# numbers = [2, 4, 6]
from git import index

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# while True:
#     try:
#         item = next(iterator)
#         print(item)
#     except StopIteration:
#         break

# for item in numbers:
#     print(item)

# class MyIterator:
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if not has_more_items():
#             raise StopIteration
#         item = get_the_next_item()
#         return item
#
# class MyIterable:
#     def __iter__(self):
#         iterator = MyIterator(self)
#         return iterator

numbers = [2, 4, 6, 8, 10]


class GreaterThanFive:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            if self._index >= len(self._data):
                raise StopIteration

            item = self._data[self._index]
            self._index += 1
            if item > 5:
                return item


class LessThanEight:
    def __init__(self, data):
        self._data = data
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            if self._index >= len(self._data):
                raise StopIteration

            item = self._data[self._index]
            self._index += 1
            if item < 8:
                return item

class Numbers:
    def __init__(self, col, *, iterator = LessThanEight):
        self.col = col
        self._iterator = iterator

    def __iter__(self):
        return self._iterator(self.col)


n = Numbers(numbers)
n2 = Numbers(numbers, iterator=GreaterThanFive)

# for item in n:
#     print(item)
# print('\n')
#
# for item in n2:
#     print(item)

# iterator repeat

class RepeatIterator:
    def __init__(self, elem, times):
        self._elem = elem
        self._remaining = times

    def __iter__(self):
        return self

    def __next__(self):
        if self._remaining <= 0:
            raise StopIteration

        self._remaining -= 1

        return self._elem

it = RepeatIterator('SQL', 3)

for item in it:
    print(item)

