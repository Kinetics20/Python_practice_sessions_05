class NullCar:
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('NUnknown car "%s".' % self._carname)

    def stop(self):
        pass