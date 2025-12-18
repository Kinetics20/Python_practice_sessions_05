from hidden_gems.ex_1.design_patterns_oop.adapter.after_class_adapter.customer import Customer
from hidden_gems.ex_1.design_patterns_oop.adapter.after_class_adapter.vendor import Vendor


class VendorAdapter(Vendor, Customer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def address(self):
        return f'{self.number} {self.street}'