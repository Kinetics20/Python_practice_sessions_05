from collections import OrderedDict

# print(issubclass(OrderedDict, dict))

od = OrderedDict()
# print(od)

od = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
od.move_to_end('key1')
# print(od)

# od_ = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od_)
# lst_item = od_.popitem()
# print(lst_item)
# print(od_)

# od_ = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od_)
# fst_item = od_.popitem(last=False)
# print(fst_item)
# print(od_)

# Expected sequence of A/B test phases
expected_sequence = OrderedDict([
    ('baseline', 'Original version without changes'),
    ('change1', 'Increased front size for better readability'),
    ('change2', 'Changed call-to-action button color'),
    ('final', 'Added customer testimonials')
])

# Actual sequence followed in one of the test setups
actual_sequence_test = OrderedDict([
    ('baseline', 'Original version without changes'),
    ('change2', 'Changed call-to-action button colour'),
    ('change1', 'Increased front size for better readability'),
    ('final', 'Added customer testimonials')
])

print('Test 1 sequence correct:', expected_sequence == actual_sequence_test)

