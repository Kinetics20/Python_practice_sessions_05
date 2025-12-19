from hidden_gems.ex_1.design_patterns_oop.decorator.after.cars.abs_car import AbsCar


class Luxury(AbsCar):
    @property
    def description(self):
        return 'Luxury'

    @property
    def cost(self):
        return 18000.00

    @property
    def premium(self):
        return 2.0