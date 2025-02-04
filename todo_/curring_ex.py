# def add(a, b):
#     return a + b
#
# def f(a):
#     def _(b):
#         return a + b
#     return _

# print(f(1)(2))

def g(a, b):
    return a + b
def y(a, b):
    return a - b

def f(fn):
    def _(a):
        def __(b):
            return fn(a, b)
        return __
    return _


print(f(g)(1)(2))
print(f(y)(1)(2))


