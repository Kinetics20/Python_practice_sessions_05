from dataclasses import dataclass, field

# @dataclass(frozen=False)
# class User:
#     name: str
#     age: int
#
# u1 = User(name='John', age=42)
# u2 = User(name='Mike', age=17)
# print(u1.name, u2.age)


# @dataclass(order=True)  # __eq__, __lt__, __gt__, __le__, __ge__ (name, age)
# class User:
#     name: str
#     age: int
#
# u1 = User(name='John', age=42)
# u2 = User(name='Mike', age=17)
# print(u1 < u2)


# @dataclass(slots=True)  #  __slots__ = ['name', 'age']
# class User:
#     name: str
#     age: int

# u1 = User(name='John', age=42)
# u2 = User(name='Mike', age=17)


# @dataclass(frozen=True)
# class User:
#     name: str
#     tags: list[str] = field(default_factory=list)


@dataclass
class Email:
    raw: str
    domain: str = field(init=False)

    def __post_init__(self):
        self.domain = self.raw.split('@')[-1]

e = Email('ala@ma.kota.pl')

print(e)


@dataclass
class Point:
    x: int
    y: int

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)

class PointStd:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def __repr__(self) -> str:
        return f'{type(self).__name__}(x={self.x}, y={self.y})'

    def __eq__(self, other: object) -> bool:
        return (self.x, self.y) == (other.x, other.y)


class TempClass:
    def __init__(self, temp_c):
        self.temp_c = temp_c

    @property
    def temp_c(self):
        return self._temp_c

    @temp_c.setter
    def temp_c(self, value):
        if value < -273.15:
            raise ValueError('Temperature below absolute zero')
        self._temp_c = value


@dataclass
class Temperature:
    temp_c: int

    def __post_init__(self):
        if self.temp_c < -273.15:
            raise ValueError('Temperature below absolute zero')


t = Temperature(temp_c=-100)
t.temp_c = -50_000_000
# print(t.temp_c)

d = TempClass(temp_c=-100)
d.temp_c = -200




p3 = PointStd(x=1, y=2)
p4 = PointStd(x=1, y=2)
# print(repr(p1))
# print(repr(p2))
# print(p1 == p2)
# print(p3 == p4)