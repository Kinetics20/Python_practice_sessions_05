import bic_code


class ShippingContainer:
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

    def __init__(self, owner_code, contents, **kwargs):
        self.owner_code = owner_code
        self.contents = contents
        self.bic = self._make_bic_code(
            owner_code=owner_code,
            serial=type(self)._generate_serial()
        )

    @classmethod
    def create_empty(cls, owner_code, **kwargs):
        return cls(owner_code, contents=[], **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, items, **kwargs):
        return cls(owner_code, contents=list(items), **kwargs)


class RefrigeratedShippingContainer(ShippingContainer):
    MAX_CELSIUS = 4.0

    def __init__(self, owner_code, contents, *, celsius, **kwargs):
        super().__init__(owner_code, contents, **kwargs)
        if celsius > type(self).MAX_CELSIUS:
            raise ValueError(f'Temperature too hot')
        self._celsius = celsius

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return bic_code.create(
            owner_code=owner_code,
            serial=str(serial).zfill(6),
            category='R'
        )

    @property
    def celsius(self):
        return self._celsius


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

r1 = RefrigeratedShippingContainer.create_with_items('MAE', ['fishes'], celsius=2)
print(r1.bic)
print(r1.celsius)
# print(r1._make_bic_code('MAE', 1337))
