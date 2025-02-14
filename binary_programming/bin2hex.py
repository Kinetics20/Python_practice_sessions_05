def bin2hex(binstr):
    mapping = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F",
    }

    # Add leading zeroes, but only if needed.
    binstr_len = len(binstr)
    padded_len = binstr_len
    if binstr_len % 4 != 0:
        padded_len += 4 - binstr_len % 4
    padded_binstr = binstr.rjust(padded_len, "0")

    output = []
    for i in range(0, padded_len, 4):
        output.append(mapping[padded_binstr[i:i+4]])

    return ''.join(output)


for value, good_result in [
    ("0", "0"),
    ("1", "1"),
    ("1010", "A"),
    ("11111", "1F"),
    ("00001110", "0E"),
]:
    result = bin2hex(value)
    print(f"bin2hex({value}) --> {result} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected {good_result}]")
