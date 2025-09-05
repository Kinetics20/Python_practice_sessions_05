# FORBIDDEN: ()

class X:
    __init__ = lambda x, y: None
    __lt__ = print

@X
class Y:
    pass

Y < 'Sth wrong!'