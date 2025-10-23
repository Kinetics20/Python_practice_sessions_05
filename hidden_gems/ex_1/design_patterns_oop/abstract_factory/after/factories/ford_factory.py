from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.ford.fiesta import FordFiesta
from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.ford.lincoln import LincolnMKS
from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.autos.ford.mustang import FordMustang
from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.factories.abs_factory import AbsFactory



class FordFactory(AbsFactory):
    @staticmethod
    def create_economy():
        return FordFiesta()

    @staticmethod
    def create_sport():
        return FordMustang()

    @staticmethod
    def create_luxury():
        return LincolnMKS()