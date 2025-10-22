from .abs_auto import AbsAuto


class JeepSahara(AbsAuto):
    def start(self):
        print('Jeep Sahara running smoothly')

    def stop(self):
        print('Jeep Sahara shutting down')