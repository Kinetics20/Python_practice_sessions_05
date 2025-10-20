# Breath-first (level order)

class LevelOrderIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._sequence):
            raise StopIteration

        result = self._sequence[self._index]
        self._index += 1
        return result


expr_tree = ['*', '+', '-', 'a', 'b', 'c', 'd']

iterator = LevelOrderIterator(expr_tree)


# for element in iter(iterator):
#     print(element)


# Depth-first, pre-order traversal


def left_child(index):
    return 2 * index + 1


def right_child(index):
    return 2 * index + 2


def is_perfect_length(sequence):
    """True if sequence has length 2ⁿ - 1, otherwise False"""

    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)


class PreOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError('Not a perfect binary tree with lengths 2ⁿ - 1.')

        self._sequence = sequence
        self._stack = [0]

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        index = self._stack.pop()
        result = self._sequence[index]

        if right_child(index) < len(self._sequence):
            self._stack.append(right_child(index))

        if left_child(index) < len(self._sequence):
            self._stack.append(left_child(index))

        return result


expr_tree = ['*', '+', '-', 'a', 'b', 'c', 'd']

iterator2 = PreOrderIterator(expr_tree)
# print(' '.join(iterator2))

# In-order Traversal, Depth-first


class InOrderIterator:
    def __init__(self, sequence):
        if not is_perfect_length(sequence):
            raise ValueError('Not a perfect binary tree with lengths 2ⁿ - 1.')

        self._sequence = sequence
        self._stack = []
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if (self._index >= len(self._sequence)) and (len(self._stack) == 0):
            raise StopIteration

        while self._index < len(self._sequence):
            self._stack.append(self._index)
            self._index = left_child(self._index)

        index = self._stack.pop()
        result = self._sequence[index]
        self._index = right_child(index)

        return result

iterator3 = InOrderIterator(expr_tree)
# print(' '.join(iterator3))


class SkipMissingIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item


missing = object()

# r + p * q
expr_tree = ['*', 'r', '*', missing, missing, 'p', 'q']

iterator4 = SkipMissingIterator(InOrderIterator(expr_tree))
# print(' '.join(iterator4))


typesetting_table = {
    '-': '\u2212',
    '*': '\u00D7',
    '/': '\u00F7'
}


class TranslationIterator:
    def __init__(self, table, iterable):
        self._table = table
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)

# r + p * q
expr_tree = ['*', 'r', '/', missing, missing, 'p', 'q']

iterator5 = TranslationIterator(typesetting_table, SkipMissingIterator(InOrderIterator(expr_tree)))
print(' '.join(iterator5))