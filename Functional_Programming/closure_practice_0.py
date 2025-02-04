def add(a, b):
    return a + b

# print(add(1, 2))
add.sth = 4200
add.sth_2 = 'Home'

# print(add.sth)
# print(add.sth_2)
# print(add(1, 2))

add.add = add
# print(add.add.add.add.add.add.add(3, 3))

def outer(num_1):
    def inner(num_2, num_3):
        return (num_2 * num_3) // num_1

    return inner

t_o = outer(10)
t_n_1 = t_o(13, 8)
print(t_n_1)
t_n_2 = t_o(130, 8)
print(t_n_2)

