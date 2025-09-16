class X:
    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls, *args, **kwargs)
        self.magic = 42
        return self

    def __init__(self):
        print('__init__ X')
        self.value = 42

    def multiply_value(self, multiplier):
        return self.value * multiplier


x = X()
print(type(x))
print(x.magic)
