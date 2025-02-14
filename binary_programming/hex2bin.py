def hex2bin(hexstr):
    mapping = {
        "0": "0000", "1": "0001", "2": "0010", "3": "0011",
        "4": "0100", "5": "0101", "6": "0110", "7": "0111",
        "8": "1000", "9": "1001", "A": "1010", "B": "1011",
        "C": "1100", "D": "1101", "E": "1110", "F": "1111",
        "a": "1010", "b": "1011", "c": "1100", "d": "1101",
        "e": "1110", "f": "1111",
    }

    output = []
    for nibble in hexstr:
        output.append(mapping[nibble])

    result = ''.join(output).lstrip("0")
    if result == '':
        return "0"

    return result


for value, good_result in [
    ("0", "0"),
    ("000001", "1"),
    ("A", "1010"),
    ("BeE7", "1011111011100111"),
    ("000000F0", "11110000"),
]:
    result = hex2bin(value)
    print(f"hex2bin({value}) --> {result} ", end="")
    if result == good_result:
        print("[OK]")
    else:
        print(f"[ERROR! Expected {good_result}]")
