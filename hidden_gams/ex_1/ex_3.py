class X:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + X(other).x


x1 = X(1)
x2 = X(2)
print(x1 + 42)