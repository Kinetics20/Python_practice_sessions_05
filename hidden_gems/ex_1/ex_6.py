import math


class A:
    def magic(self):
        print('class A')

class B(A):
    def magic(self):
        print('class B')

class C(B):
    def magic(self):
        print('class C')

class X(C, A):
    pass


# print(X.__mro__)


class Square:
    def __init__(self, a):
        self.area = a * a

    def __repr__(self):
        return f'Square(a={math.sqrt(self.area)})'