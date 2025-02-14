def make_mask(start_bit, end_bit):
    # Since users might interpret start_bit and end_bit differently,
    # we need to support both options.
    if start_bit > end_bit:
        start_bit, end_bit = end_bit, start_bit

    mask_len = end_bit - start_bit + 1
    mask = (1 << mask_len) - 1
    mask <<= start_bit

    return mask


def read_bitfield(bitfield_value, start_bit, end_bit):
    # Since users might interpret start_bit and end_bit differently,
    # we need to support both options.
    if start_bit > end_bit:
        start_bit, end_bit = end_bit, start_bit

    value = bitfield_value & make_mask(start_bit, end_bit)
    value >>= start_bit

    return value


# Using values from exercise 5.
for value, good_result in [
    ((0b01100101, 0, 1), 1),
    ((0b01100101, 2, 2), 1),
    ((0b01100101, 3, 5), 4),
    ((0b01100101, 6, 6), 1),
    ((0x71, 0, 1), 1),
    ((0x71, 2, 2), 0),
    ((0x71, 3, 5), 6),
    ((0x71, 6, 6), 1),
    ((0x33, 0, 1), 3),
    ((0x33, 2, 2), 0),
    ((0x33, 3, 5), 6),
    ((0x33, 6, 6), 0),
    ((0x7f, 0, 1), 3),
    ((0x7f, 2, 2), 1),
    ((0x7f, 3, 5), 7),
    ((0x7f, 6, 6), 1),
    ((3, 0, 1), 3),
    ((3, 2, 2), 0),
    ((3, 3, 5), 0),
    ((3, 6, 6), 0),
]:
    result = read_bitfield(*value)
    print(f"read_bitfield{value} --> 0b{result:b} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected 0b{good_result:x}]")
