def make_mask(start_bit, end_bit):
    # Since users might interpret start_bit and end_bit differently,
    # we need to support both options.
    if start_bit > end_bit:
        start_bit, end_bit = end_bit, start_bit
    mask_len = end_bit - start_bit + 1
    mask = (1 << mask_len) - 1
    mask <<= start_bit
    return mask


def clear_bitfield(bitfield_value, start_bit, end_bit):
    return bitfield_value & ~make_mask(start_bit, end_bit)


# Using values from exercise 5.
for value, good_result in [
    ((0b01100101, 0, 1), 0b01100100),
    ((0b01100101, 2, 2), 0b01100001),
    ((0b01100101, 3, 5), 0b01000101),
    ((0b01100101, 6, 6), 0b00100101),
    ((0x71, 0, 1), 0x70),
    ((0x71, 2, 2), 0x71),
    ((0x71, 3, 5), 0x41),
    ((0x71, 6, 6), 0x31),
    ((0x33, 0, 1), 0x30),
    ((0x33, 2, 2), 0x33),
    ((0x33, 3, 5), 0x03),
    ((0x33, 6, 6), 0x33),
    ((0x7f, 0, 1), 0x7c),
    ((0x7f, 2, 2), 0x7b),
    ((0x7f, 3, 5), 0x47),
    ((0x7f, 6, 6), 0x3f),
    ((3, 0, 1), 0),
    ((3, 2, 2), 3),
    ((3, 3, 5), 3),
    ((3, 6, 6), 3),
]:
    result = clear_bitfield(*value)
    print(f"clear_bitfield{value} --> 0b{result:b} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected 0b{good_result:b}]")
