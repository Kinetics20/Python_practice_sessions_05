#!/usr/bin/env python3
import re


def parse(s):
    """
    Parse an HTTP header line of the form:
    Header-Name: key1=value1; key2=value2; ...

    Returns a tuple (header_name, [[key, value], ...]) or None if invalid.
    """

    parts = s.split(':', 1)
    if len(parts) != 2:
        return None
    header, rest = parts[0].strip(), parts[1].strip()
    if not header or not rest:
        return None

    pairs = []
    for item in rest.split(';'):
        item = item.strip()
        if not item:
            continue
        if '=' not in item:
            return None
        key, value = item.split('=', 1)
        key = key.strip()
        value = value.strip()
        if not key or not value:
            return None
        pairs.append([key, value])

    return (header, pairs)


func = parse
final_results = []
for args, expected_result in [
    (('Header: key=value',),
     ('Header', [['key', 'value']])),

    (('Header: key1=value1; key2=value2; key3=value3',),
     ('Header', [['key1', 'value1'], ['key2', 'value2'], ['key3', 'value3']])),

    (('X-Theme: bg=#ffffff; fg=#000000',),
     ('X-Theme', [['bg', '#ffffff'], ['fg', '#000000']])),

    (('X-Encoding-Settings: charset=utf-8',),
     None),

    (('X-Encoding-Settings: charset=utf-8; encoding=base64',),
     None),

    (('X-Language: en=0.5; pl=0.3; de=0.2',),
     None),
]:
    actual_result = func(*args)
    final_results.append(actual_result)
    if expected_result is not None:
        print(f"Testing {args}: ", end="")
        if actual_result == expected_result:
            print("GOOD!")
        else:
            print(f"Wrong! Expected result: {expected_result}, "
                  f"Actual result: {actual_result}")
    else:
        print(f"Running main test {args}...")

import json
import hashlib

tmp = json.dumps(final_results)
hash = hashlib.sha512(tmp.encode()).digest()

GOOD_HASH = "38db2d1dc58e50aebcc4c9bbc8b86f50c357311c"
ENC_FLAG = ("940431019773d688dc5daf5ff7c6d25227d7f7b9e665"
            "f7ff206c4017dfba4eb13184df050559a6a26c6e228e")

if hash[:20].hex() == GOOD_HASH:
    print("Congratz! Here's the flag:")
    flag = bytes([f ^ h for f, h in zip(bytes.fromhex(ENC_FLAG), hash[20:])])
    print(flag.decode().strip())
else:
    print("One or more results were wrong!")
