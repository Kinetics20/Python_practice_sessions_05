# 2 < value < 10

class X:
    def __init__(self, value: str):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if not (2 < len(value) < 10):
            raise ValueError('Value must be between 2 and 10 characters')
        self._value = value


x = X('Mike')
x.value = 'Home swe'
x._value = 'Home swe sddfsdfsdfsdf'
print(x.value)
print(vars(x))
print(vars(X))
