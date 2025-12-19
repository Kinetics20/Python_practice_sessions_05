from abc import ABC

from hidden_gems.ex_1.design_patterns_oop.decorator.after.cars.abs_car import AbsCar


class AbsDecorator(AbsCar, ABC):
    def __init__(self, car):
        self._car = car

    @property
    def car(self):
        return self._car

    @property
    def premium(self):
        return self._car.premium
