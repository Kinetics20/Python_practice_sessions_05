from hidden_gems.ex_1.design_patterns_oop.factory.after.autos.abs_auto import AbsAuto


class ChevyVolt(AbsAuto):
    def start(self):
        print('Chevrolet Volt running smoothly')

    def stop(self):
        print('Chevrolet Volt shutting down')