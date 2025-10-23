from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.factories.ford_factory import FordFactory
from hidden_gems.ex_1.design_patterns_oop.abstract_factory.after.factories.gm_factory import GMFactory

for factory in FordFactory, GMFactory:
    car = factory.create_economy()
    car.start()
    car.stop()