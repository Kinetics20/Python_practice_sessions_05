from hidden_gems.ex_1.design_patterns_oop.factory.after.autos.abs_auto import AbsAuto


class NullCar(AbsAuto):
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('NUnknown car "%s".' % self._carname)

    def stop(self):
        pass