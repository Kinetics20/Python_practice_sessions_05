from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.abs_auto import AbsAuto


class ChevySpark(AbsAuto):
    def start(self):
        print("ChevySpark running cheaply")

    def stop(self):
        print("ChevySpark stopping")