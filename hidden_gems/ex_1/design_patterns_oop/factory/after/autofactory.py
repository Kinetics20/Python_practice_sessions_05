from inspect import getmembers, isclass, isabstract

import autos


# from hidden_gems.ex_1.design_patterns_oop.factory.after import autos


class AutoFactory:
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))

        for name, _cls in classes:
            if issubclass(_cls, autos.AbsAuto):
                type(self).autos[name] = _cls

    def create_instance(self, car_name):
        if car_name in type(self).autos:
            return self.autos[car_name]()

        return autos.NullCar(car_name)


# if __name__ == '__main__':
#     af = AutoFactory()
#     print(af.autos)
