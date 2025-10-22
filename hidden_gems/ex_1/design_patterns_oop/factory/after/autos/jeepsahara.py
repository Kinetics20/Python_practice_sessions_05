from hidden_gems.ex_1.design_patterns_oop.factory.after.autos.abs_auto import AbsAuto


class JeepSahara(AbsAuto):
    def start(self):
        print('Jeep Sahara running smoothly')

    def stop(self):
        print('Jeep Sahara shutting down')