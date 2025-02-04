import math


class TriangleError(Exception):
    def __init__(self, message: str, sides: list[float]):
        super().__init__(message)
        self._sides = sides

    @property
    def sides(self):
        return self._sides


    def __str__(self):
        return f'{self.args[0]} for sides {self.sides}'

    def __repr__(self):
        return f'{type(self).__name__}({self.args[0]!r}, {self.sides!r})'


def triangle_area(a: float, b: float, c: float) -> float:
    sides: list[float] = sorted((a, b, c))

    if sides[2] >= sides[0] + sides[1]:
        raise TriangleError('Invalid triangle', sides=sides)


    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

# print(triangle_area(3, 4, 5))
# print(triangle_area(1, 2, 3))
# print(triangle_area(1, 1, 3))

try:
    triangle_area(1, 1, 3)
except TriangleError as e:
    print(repr(e))