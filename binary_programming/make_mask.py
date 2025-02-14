def make_mask(start_bit, end_bit):
    # Since users might interpret start_bit and end_bit differently,
    # we need to support both options.
    if start_bit > end_bit:
        start_bit, end_bit = end_bit, start_bit

    mask_len = end_bit - start_bit + 1
    mask = (1 << mask_len) - 1
    mask <<= start_bit

    return mask


for value, good_result in [
    ((0, 0), 1),
    ((7, 0), 0xff),
    ((0, 7), 0xff),
    ((7, 5), 0b1110_0000),
    ((3, 0), 0b0000_1111),
    ((4, 4), 0b0001_0000),
]:
    result = make_mask(*value)

    print(f"make_mask{value} --> 0b{result:b} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected 0b{good_result:x}]")
