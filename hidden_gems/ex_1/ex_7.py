value_ = [[i] for i in range(1000000)]
another_ = [[i] for i in range(1000000)]

class Magic:
    __slots__ = ['value', 'another']

    def __init__(self, value, another):
        self.value = value
        self.another = another

def main():
    import tracemalloc
    tracemalloc.start()
    m = [Magic(value_, another_) for i in range(10000)]
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(peak/ 10 ** 3, 'MB')
main()
# m.value = 1111
# print(m.value)
# print(vars(m))
# print(m.__dict__)