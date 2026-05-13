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