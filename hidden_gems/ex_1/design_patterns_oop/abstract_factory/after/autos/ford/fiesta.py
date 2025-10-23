from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.abs_auto import AbsAuto


class FordFiesta(AbsAuto):
    def start(self):
        print("Ford Fiesta running cheaply")

    def stop(self):
        print("Ford Fiesta stopping")