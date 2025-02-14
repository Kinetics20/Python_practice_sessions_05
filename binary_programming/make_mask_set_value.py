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


def set_bitfield(bitfield_value, start_bit, end_bit, value_to_set):
    # Since users might interpret start_bit and end_bit differently,
    # we need to support both options.
    if start_bit > end_bit:
        start_bit, end_bit = end_bit, start_bit
    bitfield_value = clear_bitfield(bitfield_value, start_bit, end_bit)
    return bitfield_value | (value_to_set << start_bit)


# Test cases
for value, good_result in [
    ((0b01100101, 0, 1, 3), 0b01100111),
    ((0b01100101, 2, 2, 1), 0b01100101),
    ((0b01100101, 3, 5, 7), 0b01111101),
    ((0b01100101, 6, 6, 1), 0b01100101),
    ((0b01100101, 0, 1, 0), 0b01100100),
    ((0b01100101, 2, 2, 0), 0b01100001),
    ((0b01100101, 3, 5, 0), 0b01000101),
    ((0b01100101, 6, 6, 0), 0b00100101),
]:
    result = set_bitfield(*value)
    print(f"set_bitfield{value} --> 0b{result:b} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected 0b{good_result:b}]")
