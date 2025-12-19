from collections.abc import MutableMapping


class ModTwoMapping(MutableMapping):
    _mapping: dict = {}

    @staticmethod
    def _validate(value):
        if value % 2 != 0:
            raise ValueError

    def __setitem__(self, key, value, /):
        self._validate(value)
        type(self)._mapping[key] = value

    def __delitem__(self, key, /):
        del type(self)._mapping[key]

    def __getitem__(self, key, /):
        return type(self)._mapping[key]

    def __len__(self):
        return len(type(self)._mapping)

    def __iter__(self):
        return iter(type(self)._mapping.values())

    def __repr__(self):
        return repr(type(self)._mapping)


m = ModTwoMapping()
m[0] = 42
m['Home'] = 666
print(m)
# for val in m:
#     print(val)
del m[0]
print(m)
print(m['Home'])
print(m.items())

