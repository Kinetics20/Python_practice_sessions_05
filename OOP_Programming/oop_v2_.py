class A:
    @staticmethod
    def magic():
        print(f'class A')

class B:
    @staticmethod
    def magic():
        print(f'class B')

class C(A):
    @staticmethod
    def magic():
        print(f'class C')

class X(B, C, A):
    pass
    # @staticmethod
    # def magic(self):
    #     print(f'class X')


x = X()
# print(X.__mro__)
x.magic()

print(dir(tuple))
# print(help('ala'.title))
print(help((2,).count))
