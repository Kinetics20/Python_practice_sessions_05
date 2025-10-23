from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.abs_auto import AbsAuto


class CadillacCTS(AbsAuto):
    def start(self):
        print("CadillacCTS running cheaply")

    def stop(self):
        print("CadillacCTS stopping")