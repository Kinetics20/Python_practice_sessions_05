class Temperature:
    def __init__(self, temp):
        self._temp_c = temp

    @property
    def temp_c(self):
        return f'({self._temp_c:.2f} °C'

    @temp_c.setter
    def temp_c(self, new_temp):
        if new_temp < -273.15:
            raise ValueError('Temperature in Celsius cannot be below absolute zero')
        self._temp_c = new_temp

    @property
    def temp_k(self):
        return f'{self._temp_c + 273.15:.2f} K'

    @temp_k.setter
    def temp_k(self, new_temp):
        try:
            self.temp_c = (new_temp - 273.15)
        except ValueError:
            raise ValueError('Temperature in Kelvin cannot be below 0')

    @property
    def temp_f(self):
        raise AttributeError('Temperature in Fahrenheit is write only')
        # return f'{(self._temp_c * 1.8) + 32:.2f} °F'

    @temp_f.setter
    def temp_f(self, value):
        self.temp_c = (value - 32) / 1.8

    def __str__(self):
        return str(self.temp_c)

    def __format__(self, format_spec):
        match format_spec:
            case 'c':
                return self.temp_c
            case 'k':
                return self.temp_k
            case 'f':
                return self.temp_f
            case _:
                return str(self)


t = Temperature(0)
# print(t.temp_c)
#
# t.temp_c = 0
# print(t.temp_c)
#
# print(t.temp_k)
# t.temp_k = 0
# print(t.temp_f)
#
# t.temp_f = 0
# print(t.temp_c)

# print(t)

# print(f'{t:c}')
# print(f'{t:f}')
# print(f'{t:k}')
print(format(t, 'c'))
print(format(t, 'k'))
print('{:f}'.format(t))
