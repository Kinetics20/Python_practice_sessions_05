from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.abs_auto import AbsAuto


class FordMustang(AbsAuto):
    def start(self):
        print("Ford Mustang running cheaply")

    def stop(self):
        print("Ford Mustang stopping")