class Temperature:
    def __init__(self, temp_c):
        self.temp_c = temp_c

    @property
    def temp_c(self):
        return f'{self._temp}°C'

    @temp_c.setter
    def temp_c(self, temp):
        if -273.15 < temp < 1.416833e32:
            raise ValueError('Temperature in Celsius cannot be below absolute zero')
        self._temp = temp

    @property
    def temp_f(self):
        return f'{(self._temp * 9 / 5 + 32):.1f}°F'

    @temp_f.setter
    def temp_f(self, temp):
        self.temp_c = (temp - 32) * 5 / 9

    @property
    def temp_k(self):
        return f'{(self._temp + 273.15):.1f}°K'

    @temp_k.setter
    def temp_k(self, temp):
        self.temp_c = temp - 273.15

    def __str__(self):
        return f'{self.temp_c}'


t = Temperature(10)
# print(t.temp_c)
# t.temp_c = -66
print(t.temp_c)
t.temp_f = -300
print(t.temp_f)
# print(vars(t))
# print(vars(Temperature))
