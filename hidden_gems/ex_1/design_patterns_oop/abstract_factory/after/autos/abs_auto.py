from abc import ABC, abstractmethod


class AbsAuto(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass