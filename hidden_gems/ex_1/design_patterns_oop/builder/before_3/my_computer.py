from hidden_gems.ex_1.design_patterns_oop.builder.before_3.computer import Computer


class MyComputer:
    def build_computer(self):
        computer = self._computer = Computer()
        self.get_case()
        self.build_mainboard()
        self.install_mainboard()
        self.install_hard_drive()
        self.install_video_card()

    def get_case(self):
        self._computer.case = 'Coolermaster'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI'
        self._computer.cpu = 'Intel Core i9'
        self._computer.memory = '2 X 16GB'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'SSD 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GeForce RTX4080'

    def get_computer(self):
        return self._computer
