import bic_code


class ShippingContainer:
    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return bic_code.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
        )

    def __init__(self, owner_code, length_ft, contents, **kwargs):
        self.owner_code = owner_code
        self.length_ft = length_ft
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=type(self)._generate_serial()
        )

    @property
    def volume_ft3(self):
        return type(self).HEIGHT_FT * type(self).WIDTH_FT * self.length_ft

    @classmethod
    def create_empty(cls, owner_code, length_ft, **kwargs):
        return cls(owner_code, length_ft, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, **kwargs):
        return cls(owner_code, length_ft, contents=list(items), **kwargs)


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    def __init__(self, owner_code, length_ft, contents, *, celsius, **kwargs):
        super().__init__(owner_code, length_ft, contents, **kwargs)

        self.celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return bic_code.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    @property
    def volume_ft3(self):
        return super().volume_ft3 - type(self).FRIDGE_VOLUME_FT3

    @property
    def celsius(self):
        return f'{self._celsius}°C'

    @celsius.setter
    def celsius(self, value):
        if value > type(self).MAX_CELSIUS:
            raise ValueError(f'Temperature too hot')
        self._celsius = value

    @property
    def temp_f(self):
        return f'{(self._celsius * 9 / 5 + 32):.1f}°F'

    @temp_f.setter
    def temp_f(self, value):
        self.celsius = (value - 32) * 5 / 9

    @property
    def temp_k(self):
        return f'{(self._celsius + 273.15):.1f}°K'

    @temp_k.setter
    def temp_k(self, value):
        self.celsius = value - 273.15

    def __str__(self):
        return f'Owner_code: {self.owner_code}, Bic: {self.bic}, Contents: {self.contents}, Temperature C: {self.celsius}, Temperature F: {self.temp_f}, Temperature K: {self.temp_k}'


# s1 = ShippingContainer('MAE', ['apple', 'banana'])
# s2 = ShippingContainer('MAE', ['tools'])
#
# print(ShippingContainer.next_serial)
#
# s3 = ShippingContainer.create_empty('YML')
# s4 = ShippingContainer.create_with_items('MAE', {'apple', 'banana'})
#
# print(ShippingContainer.next_serial)
# print(s3.bic)

r1 = RefrigeratedShippingContainer.create_with_items('MAE', 20, ['fishes'], celsius=2)
print(r1.bic)
print(r1.celsius)
# print(r1._make_bic_code('MAE', 1337))
print(r1)
print(r1.volume_ft3)
