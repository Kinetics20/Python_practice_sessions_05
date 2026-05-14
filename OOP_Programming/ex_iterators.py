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
        return  result

# counter = CountIterator(10, 2)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

#Iterator cycle

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
            if self._index >  len(self._iterables):
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
