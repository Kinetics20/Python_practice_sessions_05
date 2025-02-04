# TODO iterable protocol -> __iter__ -> iterator object
# TODO iterator protocol -> __iter__ & __next__ -> item | StopIteration
from collections.abc import Iterator

numbers = [1, 2, 3, 4, 5]
iterator = iter(numbers)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# for idx, number in enumerate(iterator):
#     print(idx, number)

class Range:
    def __init__(self, start: int, stop: int | None = None, step: int = 1, /) -> None:
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.stop = stop
        self.step = step

        self.item = start
        self.counter = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> int:
        if self.counter >= (self.stop - self.start) / self.step:
            raise StopIteration("Something is yes no")

        result = self.item
        self.counter += 1

        self.item += self.step

        return result


r1 = Range(20, 5, -1)
it = iter(r1)


print(r1 is it)

print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))
print(next(r1))

# class Odd:
#     def __init__(self, iterable):
#         self.iterable = iterable
#         self._index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for item in self.iterable[self._index:]:
#             if self._index % 2 == 0:
#                 self._index += 1
#                 return item
#             else:
#                 self._index += 1
#
#         if self._index >= len(self.iterable):
#             raise StopIteration('Yolo')
#
#
# class Iterable:
#     def __init__(self, data):
#         self.data = data
#
#     def __iter__(self):
#         return Odd(self.data)
#
#
# for element in Iterable([1, 2, 3, 4, 5, 6]):
#     print(element)

# r1 = Range(0, 5, -1)
# it = iter(r1)
# print(r1 is it)
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
# print(next(r1))
#
# # for element in Range(5):
# #     print(element)


