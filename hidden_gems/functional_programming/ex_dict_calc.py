def dict_calc(a, b, operation):
    dict_opr = {
        'add': lambda: a + b,
        'multiply': lambda: a * b,
        'substraction': lambda: a - b,
        'divide': lambda: None if b == 0 else a / b
    }

    return None if operation not in dict_opr else dict_opr[operation]()


def calculate(a, operation, b):
    if operation == "/" and b == 0:
        return None

    dict_operation = {
        '+': lambda: a + b,
        '-': lambda: a - b,
        '*': lambda: a * b,
        '/': lambda: a / b,
    }

    return dict_operation.get(operation, lambda: None)()


print(dict_calc(2, 5, 'add'))
print(dict_calc(2, 5, 'multiply'))
print(dict_calc(2, 5, 'substraction'))
print(dict_calc(2, 5, 'divide'))
print(dict_calc(2, 5, 'ala'))
print(dict_calc(2, 5, 0))
