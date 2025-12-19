from collections.abc import MutableSequence


class ModTwoSequence(MutableSequence):
    _list: list = []

    @staticmethod
    def _validate(value):
        if value % 2 != 0:
            raise ValueError

    def insert(self, index, value):
        self._validate(value)
        type(self)._list.insert(index, value)

    def __getitem__(self, index):
        # for idx, element in enumerate(type(self)._list):
        #     if idx == index:
        #         return element
        # raise IndexError(f'Index out of range: {index}')

        return type(self)._list[index]

    def __setitem__(self, index, value):
        self._validate(value)
        type(self)._list[index] = value

    def __delitem__(self, index):
        del type(self)._list[index]

    def __len__(self):
        return len(type(self)._list)

    def __repr__(self):
        return repr(type(self)._list)


my_seq = ModTwoSequence()
my_seq.insert(0, 40)
my_seq.insert(1, 42)
my_seq.insert(2, 44)
my_seq.insert(3, 46)
# my_seq.insert(1, 41)

print(my_seq, len(my_seq))
print(my_seq[2])
my_seq[2] = 1000
print(my_seq, len(my_seq))
del my_seq[2]
print(my_seq, len(my_seq))


