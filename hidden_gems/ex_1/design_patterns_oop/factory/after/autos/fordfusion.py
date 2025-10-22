from hidden_gems.ex_1.design_patterns_oop.factory.after.autos.abs_auto import AbsAuto


class FordFusion(AbsAuto):
    def start(self):
        print('Cool Ford Fusion running smoothly')

    def stop(self):
        print('Ford Fusion shutting down')