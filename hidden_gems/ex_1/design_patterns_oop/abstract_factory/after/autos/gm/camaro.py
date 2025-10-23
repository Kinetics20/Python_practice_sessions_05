from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.abs_auto import AbsAuto


class ChevyCamaro(AbsAuto):
    def start(self):
        print("ChevyCamaro running cheaply")

    def stop(self):
        print("ChevyCamaro stopping")