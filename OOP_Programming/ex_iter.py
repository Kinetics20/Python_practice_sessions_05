# numbers = [2, 4, 6]
import datetime

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
    def __init__(self, col, *, iterator=LessThanEight):
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

# for item in it:
#     print(item)

from fractions import Fraction


# print(Fraction(1, 3) + Fraction(2, 3))

class RationalRange:
    def __init__(self, start, stop, num_steps):
        if num_steps != int(num_steps):
            raise ValueError(f'num_steps {num_steps} does not have integral value.')
        if num_steps < 1:
            raise ValueError(f'num_steps {num_steps} is not positive')

        self._start = Fraction(start)
        self._num_steps = num_steps
        self._step = Fraction(stop - start, num_steps)

    def __getitem__(self, index):
        if not (0 <= index < self._num_steps):
            raise IndexError
        return self._start + index * self._step


r = RationalRange(5, 13, 6)
# print(r[0])
# print(r[1])
# print(list(r))
# print([float(item) for item in r])
# print(sum(r))

# iter(callable, sentinel)

# with open("end_terminated_file.txt", "wt") as f:
#     f.write("291\n")
#     f.write("149\n")
#     f.write("17\n")
#     f.write("31\n")
#     f.write("547\n")
#     f.write("2069\n")
#     f.write("END\n")
#
# with open('end_terminated_file.txt', 'rt') as f:
#     lines = iter(lambda: f.readline().strip(), 'END')
#     readings = [int(line) for line in lines]
#
# print(readings)


# timestamps = iter(datetime.datetime.now, None)
#
# print(next(timestamps))
# print(next(timestamps))

import shutil
import time
from itertools import islice

timestamps = iter(datetime.datetime.now, None)
free_space_readings = iter(lambda: shutil.disk_usage('.').free, None)

# for timestamps, free_bytes in islice(zip(timestamps, free_space_readings), 5):
#     print(timestamps, f'{free_bytes / (1024 * 1024 * 1024):.2f} GiB')
#     time.sleep(1.0)

continents = {
    "Europe": {
        "Poland": "Warsaw",
        "Germany": "Berlin",
        "France": "Paris",
    },
    "Asia": {
        "Japan": "Tokyo",
        "China": "Beijing",
        "India": "New Delhi",
    },
    "Africa": {
        "Egypt": "Cairo",
        "Kenya": "Nairobi",
        "South Africa": "Pretoria",
    },
}


class CapitalsIterator:
    def __init__(self, continents):
        self._capitals = sorted((capital for countries in continents.values() for capital in countries.values()))

        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._capitals):
            raise StopIteration

        capital = self._capitals[self._index]
        self._index += 1
        return capital


i = CapitalsIterator(continents)

print(list(i))
