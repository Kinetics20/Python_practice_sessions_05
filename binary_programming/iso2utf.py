def iso_8859_2_to_utf_8_py(input_bytes):
    # Python idiomatic version.
    return input_bytes.decode("iso-8859-2").encode()


def iso_8859_2_to_utf_8(input_bytes):
    # ISO-8859-2 to UTF-8 bytes mapping (only for Polish letters).
    mapping = {
        0xA1: b'\xc4\x84',  # Ą
        0xA3: b'\xc5\x81',  # Ł
        0xA6: b'\xc5\x9a',  # Ś
        0xAC: b'\xc5\xb9',  # Ź
        0xAF: b'\xc5\xbb',  # Ż
        0xB1: b'\xc4\x85',  # ą
        0xB3: b'\xc5\x82',  # ł
        0xB6: b'\xc5\x9b',  # ś
        0xBC: b'\xc5\xba',  # ź
        0xBF: b'\xc5\xbc',  # ż
        0xC6: b'\xc4\x86',  # Ć
        0xCA: b'\xc4\x98',  # Ę
        0xD1: b'\xc5\x83',  # Ń
        0xD3: b'\xc3\x93',  # Ó
        0xE6: b'\xc4\x87',  # ć
        0xEA: b'\xc4\x99',  # ę
        0xF1: b'\xc5\x84',  # ń
        0xF3: b'\xc3\xb3',  # ó
    }

    output = []
    for b in input_bytes:
        if b < 128:
            output.append(bytes([b]))
            continue
        output.append(mapping[b])

    return b''.join(output)


data = bytes.fromhex("7a 61 bf f3 b3 e6 20 67 ea b6 6c b1 20 6a 61 bc f1 0a")
idiomatic = iso_8859_2_to_utf_8_py(data)
normal = iso_8859_2_to_utf_8(data)

print(idiomatic.hex(sep=" "))
print(normal.hex(sep=" "))
print("Match:", idiomatic == normal)
