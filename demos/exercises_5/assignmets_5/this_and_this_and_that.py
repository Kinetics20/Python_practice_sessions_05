#!/usr/bin/env python3
import re


def extract(s):
    """
    Extract fields from a log entry of the format:
    HH:MM:SS LEVEL CODE "Explanation"

    Returns a dictionary with keys:
      - level: string (e.g., "WARNING")
      - code: tuple (letter, number) e.g. ("A", 123)
      - msg: string (Explanation without quotes)

    Returns None if the input does not match the expected format.
    """
    pattern = re.compile(
        r'^(?:[01]\d|2[0-3]):'
        r'(?:[0-5]\d):'
        r'(?:[0-5]\d) '
        r'(?P<level>[A-Z]+) '
        r'(?P<letter>[A-Z])'
        r'(?P<number>\d{1,4}) '
        r'"(?P<msg>[^"]*)"$'
    )
    m = pattern.match(s)
    if not m:
        return None

    return {
        "level": m.group('level'),
        "code": (m.group('letter'), int(m.group('number'))),
        "msg": m.group('msg')
    }


func = extract
final_results = []
for args, expected in [
    (('12:33:01 WARNING W715 "Funny smell detected but I have no nose."',), {
        "level": "WARNING",
        "code": ("W", 715),
        "msg": "Funny smell detected but I have no nose."
    }),
    (('00:27:17 ERROR Z1 "Something aweful has happened."',), {
        "level": "ERROR",
        "code": ("Z", 1),
        "msg": "Something aweful has happened."
    }),
    (('07:51:41 DEBUG D65 "Just a debug message."',), {
        "level": "DEBUG",
        "code": ("D", 65),
        "msg": "Just a debug message."
    }),
    (('16:38:26 DEBUG D12 "Just a debug message."',), None),
    (('03:11:53 INFO C7 "Just a debug message."',), None),
    (('11:23:25 INFO I55 "Just a debug message."',), None),
    (('22:52:29 ERROR A220 "Oh no an error."',), None),
    (('20:47:39 INFO I2025 "Regex is fun."',), None),
]:
    result = func(*args)
    final_results.append(result)
    if expected is not None:
        print(f"Testing {args}: ", end="")
        if result == expected:
            print("GOOD!")
        else:
            print(f"Wrong! Expected result: {expected}, Actual result: {result}")
    else:
        print(f"Running main test {args}...")

import json
import hashlib

summary = json.dumps(final_results)
h = hashlib.sha512(summary.encode()).digest()

GOOD_HASH = "e38dfc0c682ca13b51e2578bfd29cb72e3992166"
ENC_FLAG = (
    "d7fc259802342701d194a316d460454b49225b8095a1"
    "a85b669f96200e363b1607e0738c343b84597bea8167"
)

if h[:20].hex() == GOOD_HASH:
    print("Congrats! Here's the flag:")
    flag = bytes([f ^ h for f, h in zip(bytes.fromhex(ENC_FLAG), h[20:])])
    print(flag.decode().strip())
else:
    print("One or more results were wrong!")
