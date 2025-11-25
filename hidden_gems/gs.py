from collections.abc import Iterable


class X:
    def __init__(self, tags: Iterable[str] | None = None):
        self.tags = tags

    @property
    def tags(self) -> list[str]:
        return self._tags

    @tags.setter
    def tags(self, value: Iterable[str] | None) -> None:
        if value is None:
            self._tags = []
        else:
            self._tags = list(value)

c = X(['ala', '1111', 'home'])
print(c, c.tags)
c.tags = '42'
print(c, c.tags)