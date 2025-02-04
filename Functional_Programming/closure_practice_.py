def sentence(name):
    # ad = 'Jenny'
    def inner(city):
        return f'I am {name} and I come from {city}'

    return inner

new_sentence = sentence('Mike Tyson')
print(new_sentence.__closure__[0].cell_contents)
# print(new_sentence.__closure__[1].cell_contents)
print([x.cell_contents for x in new_sentence.__closure__])

sent = new_sentence('New York')
sent_2 = new_sentence('Chicago')
#
# print(sent)
# print(sent_2)

# new_sentence = sentence('Mike Tyson')('Warsaw')


# Factory function

def power_10(n):
    return n ** 10

def power_11(n):
    return n ** 11

def p_out(exponent):
    def inner(base):
        return exponent ** base

    return inner

z = p_out(2)
z8 = p_out(3)
# print(z, z8)

z_1 = z(1)
# print(z_1)
z_2 = z(2)
z_8_2 = z8(2)
print(z_2)
print(z_8_2)
z_3 = z(3)
# print(z_3)
print(z.__closure__[0].cell_contents)
