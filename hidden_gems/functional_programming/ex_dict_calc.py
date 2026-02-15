def dict_calc(a, b, operation):
    dict_opr = {
        'add': lambda: a + b,
        'multiply': lambda: a * b,
        'substraction': lambda: a - b,
        'divide': lambda: a / b
    }

    return dict_opr[operation]()


print(dict_calc(2, 5, 'add'))
print(dict_calc(2, 5, 'multiply'))
print(dict_calc(2, 5, 'substraction'))
print(dict_calc(2, 5, 'divide'))
