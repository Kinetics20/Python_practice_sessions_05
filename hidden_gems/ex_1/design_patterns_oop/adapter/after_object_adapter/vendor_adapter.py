from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.abs_adapter import AbsAdapter


class VendorAdapter(AbsAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return f'{self._adaptee.number} {self.adaptee.street}'
