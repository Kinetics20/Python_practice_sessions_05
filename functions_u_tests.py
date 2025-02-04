def divide(a, b):
    return a / b


if divide(20, 5) == 4.0:
    print('OK')
else:
    raise AssertionError('Sth is wrong')

if divide(20, 5) != 10.0:
    print('OK')
else:
    raise AssertionError('Sth is wrong')

try:
    divide(20, 0)
    raise AssertionError('Sth is wrong')
except ZeroDivisionError:
    print('OK')
