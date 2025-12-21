from collections import defaultdict
from timeit import timeit

# print(issubclass(defaultdict, dict))

# dd = defaultdict(list)
#
# dd['home'].append(42)
# print(dd['test'])
# print(dd)

# std_dict = {}
#
# std_dict.setdefault('key', 'Default')
# print(std_dict['key'])
#
# dd = defaultdict(lambda: 'Default')
# print(dd['key'])

# setup_defaultdict = """
# from collections import defaultdict
# dd = defaultdict(list)
# """
#
# stmt_defaultdict_append = '[dd[f"key_{i // 2}"].append(1) for i in range(2000000)]'
#
# time_defaultdict_append = timeit(stmt=stmt_defaultdict_append, setup=setup_defaultdict, number=10)
#
#
# setup_setdefault_dict = """
#
# std_dict = {}
# """
#
# stmt_setdefault_append = '[std_dict.setdefault(f"key_{i // 2}", []).append(1) for i in range(2000000)]'
#
# time_setdefault_append = timeit(stmt=stmt_setdefault_append, setup=setup_setdefault_dict, number=10)
#
# print(f'defaultdict: {time_defaultdict_append}\n', f'dict: {time_setdefault_append}')

items = [
    ('Apple', 5, 'Fruit'),
    ('Banana', 3, 'Fruit'),
    ('Hammer', 10, 'Tool'),
    ('Screwdriver', 10, 'Tool'),
    ('Laptop', 5000, 'Electronics'),
    ('Smartphone', 4000, 'Electronics'),
]

dd = defaultdict(int)
for _, price, item_type in items:
    dd[item_type] += price

print(dd)