class Example:
    def __new__(cls, jeff):
        self = super().__new__(cls)
        if jeff > 42:
            cls.magic = lambda self: 'higher'
        else:
            cls.magic = lambda self: 'lower'
        return self

    def __init__(self, jeff):
        pass


x = Example(43)
print(x)
print(x.magic())
