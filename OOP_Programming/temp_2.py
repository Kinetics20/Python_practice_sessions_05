class Temp:
    def __init__(self, temp):
        self._temp = temp

    def get_temp(self):
        return self._temp

    def set_temp(self, value):
        self._temp = value

    def del_temp(self):
        del self._temp

    temp = property(get_temp, set_temp, del_temp, 'temp')


t = Temp(10)
print(t.get_temp())
t.set_temp(999)
t.del_temp()
print(t)