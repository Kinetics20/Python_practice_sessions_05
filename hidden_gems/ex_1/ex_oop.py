class A:
    magic = 42

# print(A.magic)

def yolo(obj):
    obj.xd = 42

Magic = type('Magic', (object, ), {
    'magic': 42,
    '__init__': lambda obj: setattr(obj, 'xd', 42),
    'true_magic': classmethod(lambda obj: setattr(obj, 'xd', 42)),
})
m = Magic()
print(m.magic)
print(m.xd)
# print(vars(Magic))
# print(vars(A))
