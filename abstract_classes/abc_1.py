from abc import ABCMeta, ABC, abstractmethod


class SwordMeta(type):

    def __instancecheck__(cls, instance):
        return issubclass(type(instance), cls)

    def __subclasscheck__(cls, subclass):
        if (
            hasattr(subclass, 'swipe') and callable(subclass.swipe)
            and
            hasattr(subclass, 'sharpen') and callable(subclass.sharpen)
        ):
            return True
        return super().__subclasscheck__(subclass)


class Sword(ABC):
    """Abstract Base Class"""

    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def sharpen(self):
        raise NotImplementedError


    def thrust(self):
        print('Thrust!', type(self).__name__)


class BroadSword(Sword):
    def swipe(self):
        print('Swoosh!', type(self).__name__)

    def sharpen(self):
        print('Shrink!', type(self).__name__)


class SamuraiSword(Sword):
    def swipe(self):
        print('Slice!', type(self).__name__)

    def sharpen(self):
        print('Shrink!', type(self).__name__)

class Rifle:
    def fire(self):
        print('Bang!!', type(self).__name__)

class Sabre(Sword):
    def swipe(self):
        print('Swipe!', type(self).__name__)

    def sharpen(self):
        print('Sharpen!', type(self).__name__)



class LightSabre:
    def swipe(self):
        print('Ffffkrrrrshhzzzwooooom..wooom..wooom!', type(self).__name__)

samurai_sword = SamuraiSword()

sabre = Sabre()
print(issubclass(LightSabre, Sword))
print(issubclass(SamuraiSword, Sword))
print(isinstance(sabre, Sword))
samurai_sword.thrust()