# iterator tee

class TeeSharedState:
    def __init__(self, iterable):
        self.source = iter(iterable)
        self.buffer = []


class TeeIterator:
    def __init__(self, shared_state):
        self._shared_state = shared_state
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._shared_state.buffer):
            item = self._shared_state.buffer[self._index]
        else:
            item = next(self._shared_state.source)
            self._shared_state.buffer.append(item)

        self._index += 1
        return item


def tee(iterable, n=2):
    state = TeeSharedState(iterable)
    return tuple(TeeIterator(state) for _ in range(n))


a, b = tee('ABC', 2)


# for item in a:
#     print(item)
#
# print('\n')
#
# for item in b:
#     print(item)


# iterator count

class CountIterator:
    def __init__(self, start=0, step=1):
        self._current = start
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self._current
        self._current += self._step
        return result


# counter = CountIterator(10, 2)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# Iterator cycle

class CycleIterator:
    def __init__(self, iterable):
        self._items = list(iterable)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._items) == 0:
            raise StopIteration

        item = self._items[self._index]
        self._index += 1

        if self._index == len(self._items):
            self._index = 0

        return item


# c = CycleIterator('ABCD')
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))


class ChainIterator:
    def __init__(self, *iterables):
        self._iterables = iterables
        self._index = 0
        self._current_iterator = iter(self._iterables[self._index]) if self._iterables else None

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            if self._index > len(self._iterables):
                raise StopIteration

            try:
                return next(self._current_iterator)
            except StopIteration:
                self._index += 1

                if self._index >= len(self._iterables):
                    raise StopIteration

                self._current_iterator = iter(self._iterables[self._index])


ci = ChainIterator("AB", "", [], "CD", [1, 2])


# print(next(ci))
# print(next(ci))
# print(next(ci))
# print(next(ci))
# print(next(ci))
# print(next(ci))


class IsliceIterator:
    def __init__(self, iterable, start, stop):
        self._iterator = iter(iterable)
        self._start = start
        self._stop = stop
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self._index < self._start:
            next(self._iterator)
            self._index += 1

        if self._index >= self._stop:
            raise StopIteration

        element = next(self._iterator)
        self._index += 1

        return element


# mii = IsliceIterator('abcdefgh', 2, 5)
# for item in mii:
#     print(item)


class CompressIterator:
    def __init__(self, data, selectors):
        self._data_iterator = iter(data)
        self._selectors_iterator = iter(selectors)

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            item = next(self._data_iterator)
            selector = next(self._selectors_iterator)

            if selector:
                return item


x = CompressIterator('abcdefgh', [1, 0, 1, 0, 1, 1, 0, 1])


# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


class FilterFalseIterator:
    def __init__(self, predicate, iterable):
        self._predicate = predicate
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):

        while True:
            item = next(self._iterator)

            if not self._predicate(item):
                return item


h = FilterFalseIterator(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])


# print(next(h))
# print(next(h))
# print(next(h))
# print(next(h))


class DropWhileIterator:
    def __init__(self, predicate, iterable):
        self._predicate = predicate
        self._iterator = iter(iterable)
        self._dropping = True

    def __iter__(self):
        return self

    def __next__(self):

        while self._dropping:
            item = next(self._iterator)

            if not self._predicate(item):
                self._dropping = False
                return item

        return next(self._iterator)


it = DropWhileIterator(lambda x: x < 5, [1, 2, 3, 5, 2, 1, 7])
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
