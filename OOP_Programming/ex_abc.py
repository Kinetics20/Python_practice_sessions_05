from abc import ABCMeta, ABC, abstractmethod

# class SwordMeta(type):
#     def __subclasscheck__(cls, subclass):
#         if callable(getattr(subclass, 'swipe', None)) and callable((getattr(subclass, 'sharpen', None))):
#             return True
#         return super().__subclasscheck__(subclass)
#
#     def __instancecheck__(cls, instance):
#         return issubclass(type(instance), cls)


class Sword(ABC):
    # """A virtual base class for sword-like object."""
    # @classmethod
    # def __subclasshook__(cls, subclass):
    #     if cls is Sword:
    #         return (
    #                 callable(getattr(subclass, 'swipe', None)) and callable((getattr(subclass, 'sharpen', None)))
    #         ) or NotImplemented
    #     return NotImplemented
    @abstractmethod
    def swipe(self):
        raise NotImplementedError

    @abstractmethod
    def sharpen(self):
        raise NotImplementedError

    @abstractmethod
    def parry(self):
        return f'{type(type).__name__} blocks the attack.'


class BroadSword(Sword):
    def swipe(self):
        return 'Swoosh!'

    def sharpen(self):
        return 'Sharpening the broad sword.'

    def parry(self):
        base_message = super().parry()
        return base_message + ' The heavy guard holds.'


class SamuraiSword(Sword):
    def swipe(self):
        return 'Slash!'

    def sharpen(self):
        return 'Sharpening the samurai sword.'


class Sabre(Sword):
    pass


class Riffle:
    def fire(self):
        return 'Bang!'


# def thrust(self):
#     return f'{type(self).__name__} thrust!'
#
# Sword.thrust = thrust
#
# broad_sword = BroadSword()
#
# print(isinstance(broad_sword, BroadSword))
# print(BroadSword.__mro__)
# print(broad_sword.thrust())


bs = BroadSword()
print(bs.parry())

print(issubclass(BroadSword, Sword))
# print(issubclass(SamuraiSword, Sword))
# # print(issubclass(Sabre, Sword))
# print(issubclass(Riffle, Sword))
