# Dijkstra

def sum_(n):
    if n == 0:
        return n
    else:
        return n + sum_(n - 1)

# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(10000)

print(sum_(10))