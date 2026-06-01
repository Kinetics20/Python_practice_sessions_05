from abc import ABCMeta

# class SwordMeta(type):
#     def __subclasscheck__(cls, subclass):
#         if callable(getattr(subclass, 'swipe', None)) and callable((getattr(subclass, 'sharpen', None))):
#             return True
#         return super().__subclasscheck__(subclass)
#
#     def __instancecheck__(cls, instance):
#         return issubclass(type(instance), cls)


class Sword(metaclass=ABCMeta):
    """A virtual base class for sword-like object."""
    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Sword:
            return (
                    callable(getattr(subclass, 'swipe', None)) and callable((getattr(subclass, 'sharpen', None)))
            ) or NotImplemented
        return NotImplemented


class BroadSword:
    def swipe(self):
        return 'Swoosh!'

    def sharpen(self):
        return 'Sharpening the broad sword.'


class SamuraiSword:
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

print(issubclass(BroadSword, Sword))
# print(issubclass(SamuraiSword, Sword))
# print(issubclass(Sabre, Sword))
# print(issubclass(Riffle, Sword))
