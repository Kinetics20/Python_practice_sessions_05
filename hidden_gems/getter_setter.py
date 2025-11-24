from collections.abc import Iterable


class X:
    def __init__(self, tags: Iterable[str] | None = None):
        self.tags: list[str] = tags
        # self._tags = 2137

    @property
    def tags(self) -> list[str]:
        print('getter')
        return self._tags

    @tags.setter
    def tags(self, value: Iterable[str] | None) -> None:
        print('setter', value)
        if value is None:
            self._tags = []
        else:
            self._tags = list(value)
        # self._tags2 = value


z = X('ala')
y = X()
z.tags = 'John'
print(z.tags)