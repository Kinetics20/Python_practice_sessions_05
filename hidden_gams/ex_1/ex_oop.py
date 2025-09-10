class A:
    magic = 42

# print(A.magic)

def yolo(obj):
    obj.xd = 42

Magic = type('Magic', (object, ), {
    'magic': 42,
    '__init__': yolo
})
m = Magic()
print(m.magic)
print(m.xd)
# print(vars(Magic))
# print(vars(A))
