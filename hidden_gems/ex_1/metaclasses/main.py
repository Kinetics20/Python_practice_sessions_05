class Widget:
    pass


class Widget2(object, metaclass=type):
    pass


name = 'Widget3'
metaclass = type
bases = ()
kwargs: dict = {}
namespace = metaclass.__prepare__(name, bases, **kwargs)
Widget3 = metaclass.__new__(metaclass, name, bases, namespace, **kwargs)
metaclass.__init__(Widget3, name, bases, namespace, **kwargs)


# print(Widget3)
# w = Widget3()
# print(w)