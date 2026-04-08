import bic_code

class ShippingContainer:
    next_serial = 1317


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


    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = ShippingContainer._generate_serial()

    @classmethod
    def create_empty(cls, owner_code):
        return cls(owner_code, contents=[])

    @classmethod
    def create_with_items(cls, owner_code, items):
        return cls(owner_code, contents=list(items))


s1 = ShippingContainer('MAE', ['apple', 'banana'])
s2 = ShippingContainer('MAE', ['tools'])
print(s1.serial)
print(s2.serial)
print(ShippingContainer.next_serial)

s3 = ShippingContainer.create_empty('MAE')
s4 = ShippingContainer.create_with_items('MAE', {'apple', 'banana'})
