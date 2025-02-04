def outer_fn():
    x = 42
    az = 1024

    # def z():
    #     return 1024

    def inner_fn():
        nonlocal x
        # return f'Answer for all questions : {x}'
        y = az * 2 + x
        x += 1
        # y = x * 2 + z()
        return y

    return inner_fn


result_fn = outer_fn()
# dunder -> double underscores
print(result_fn.__closure__[0].cell_contents)
print(result_fn.__closure__[1].cell_contents)

result = result_fn()
print(result_fn.__closure__[0].cell_contents)
print(result_fn.__closure__[1].cell_contents)
print(result)




