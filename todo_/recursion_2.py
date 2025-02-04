def sum_(n, acc=0):
    if n == 0:
        return acc
    else:
        return sum_(n - 1, acc + n)

print(sum_(10))
