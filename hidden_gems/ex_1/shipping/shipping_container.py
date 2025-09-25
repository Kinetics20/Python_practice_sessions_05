from hidden_gems.ex_1.shipping import iso6346


class ShippingContainer(object, metaclass=type):
    next_serial = 1337

    @classmethod
    def _generate_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
        )

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=ShippingContainer._generate_serial()
        )


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        self.celsius = celsius

    @property
    def celsius(self):
        return f'{self._celsius}°C'

    @celsius.setter
    def celsius(self, value):
        if not (-273.16 < value < RefrigeratedShippingContainer.MAX_CELSIUS):
            raise ValueError('Invalid Temperature!')
        self._celsius = value


    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


    @staticmethod
    def _make_bic_code(owner_code, serial):
        return iso6346.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )


# r1 = RefrigeratedShippingContainer('MAE', ['penguin'])
# print(r1.bic)

r0 = RefrigeratedShippingContainer('YML', ['onion'], celsius=3.0)
r1 = RefrigeratedShippingContainer.create_empty('YML', celsius=3.0)
r2 = RefrigeratedShippingContainer.create_with_items('YML', ['ice', 'fishes'], celsius=3.0)
r0.celsius = 2
print(r0.celsius)
