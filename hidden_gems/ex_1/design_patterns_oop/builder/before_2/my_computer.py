from hidden_gems.ex_1.design_patterns_oop.builder.before_2.computer import Computer


class MyComputer:
    def build_computer(self):
        computer = self._computer = Computer()

        computer.case = 'Coolermaster'
        computer.mainboard = 'MSI'
        computer.cpu = 'Intel Core i9'
        computer.memory = '2 X 16GB'
        computer.hard_drive = 'SSD 2TB'
        computer.video_card = 'GeForce RTX4080'

    def get_computer(self):
        return self._computer