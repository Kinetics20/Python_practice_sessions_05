from hidden_gems.ex_1.design_patterns_oop.adapter.after_object_adapter.abs_adapter import AbsAdapter


class CustAdapter(AbsAdapter):
    @property
    def name(self):
        return self._adaptee.name

    @property
    def address(self):
        return self._adaptee.address