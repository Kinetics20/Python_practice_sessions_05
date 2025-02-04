class Odd:
    def __init__(self, iterable):
        self.iterable = iterable
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self.iterable):
            raise StopIteration(' _StopIteration_ ')

        for item in self.iterable[self._index:]:
            if self._index % 2 == 0:
                self._index += 1
                return item
            else:
                self._index += 1



class Iterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Odd(self.data)

for element in Iterable([1, 2, 3, 4, 5, 6]):
# for element in Iterable({'a': 1, 'b': 2, 'c': 3, 'd': 4}):
    print(element)