from abc import ABC, abstractmethod

from hidden_gems.ex_1.design_patterns_oop.builder.after.computer import Computer


class AbsBuilder(ABC):
    def get_computer(self):
        if not getattr(self, '_computer'):
            raise AttributeError('Build new computer first!')

        return self._computer

    def new_computer(self):
        self._computer = Computer()

    @abstractmethod
    def get_case(self):
        pass

    @abstractmethod
    def build_mainboard(self):
        pass

    @abstractmethod
    def install_mainboard(self):
        pass

    @abstractmethod
    def install_hard_drive(self):
        pass

    @abstractmethod
    def install_video_card(self):
        pass
