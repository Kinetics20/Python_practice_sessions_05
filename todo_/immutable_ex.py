
from abc import ABC
from dataclasses import dataclass


class Immutable(ABC):
    __slots__ = ('__attrs__',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__attrs__ = frozenset()

    def __setattr__(self, name, value):
        if name == '__attrs__':
            super().__setattr__(name, value)
            return

        if name in self.__attrs__:
            raise AttributeError(f'{name} is immutable')
        else:
            super().__setattr__(name, value)
            self.__attrs__ |= {name}

    def __delattr__(self, name):
        if name in self.__attrs__:
            raise AttributeError(f'{name} is immutable')
        else:
            raise AttributeError(name)


@dataclass(frozen=True)
class Point:
    x: int
    y: int
    name: str = 'Point'

    def __post_init__(self):
        if self.name.strip() == '':
            raise ValueError('Point name is required')




p = Point(x=1, y=2, name='')
print(p)
p.x = 42
print(p)