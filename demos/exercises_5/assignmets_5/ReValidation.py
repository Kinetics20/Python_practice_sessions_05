#!/usr/bin/env python3
import re


def validate(s):
    """
    Validate a log entry of the format:
    HH:MM:SS LEVEL CODE "Explanation"

    - HH: 00-23
    - MM, SS: 00-59
    - LEVEL: one or more uppercase letters
    - CODE: one uppercase letter followed by 1 to 4 digits
    - Explanation: text in double quotes, may include any characters except a double quote
    """
    pattern = re.compile(
        r'^(?:[01]\d|2[0-3]):'  # Hour 00-23
        r'(?:[0-5]\d):'  # Minute 00-59
        r'(?:[0-5]\d) '  # Second 00-59 and space
        r'[A-Z]+ '  # ERROR LEVEL (uppercase letters)
        r'[A-Z][0-9]{1,4} '  # ERROR CODE (1 letter + 1-4 digits)
        r'"[^\"]*"$'  # Explanation in quotes, no internal quotes
    )
    return bool(pattern.match(s))


func = validate
final_results = []
for args, expected in [
    (('12:33:01 WARNING W715 "Funny smell detected but I have no nose."',), True),
    (('00:27:17 ERROR Z1 "Something awful has happened."',), True),
    (('17:52:49 INFO I2412 "User changed clock from 24h to 12h."',), True),
    (('This is totally wrong',), False),
    (('00;27;17 ERROR E2 "Wait, where is the error?"',), False),
    (('99:99:99 ERROR E999 "Timestamp is not valid in this entry."',), False),
    (('1x:-::1"1 X-Y-Z ???? So"Many"Things"Wrong"Here',), False),
    (('07:51:41 DEBUG D65 "Just a debug message."',), None),
    (('21|23|25 debug X123 "Just a debug message."',), None),
    (('04:41:12 DEBUG 555 "Just a debug message."',), None),
    (('16:38:26 DEBUG D12 "Just a debug message."',), None),
    (('23:28:01 INFO C1?3 "Just a debug message."',), None),
    (('03:11:53 INFO C7 "Just a debug message."',), None),
    (('11:23:25 INFO I55 "Just a debug message."',), None),
    (('19:55:37 ERROR A219 Oh no an error.',), None),
    (('22:52:29 ERROR A220 "Oh no an error."',), None),
    (('01:91:03 ERROR A230 "Oh no an error."',), None),
    (('01:11:03 X123 "Just a debug message."',), None),
    (('01:11:03 ERROR "Just a debug message."',), None),
    (('01:11:03 ERROR X123',), None),
    (('20:47:39 INFO I2025 "Regex is fun."',), None),
]:
    result = func(*args)
    final_results.append(result)
    if expected is not None:
        print(f"Testing {args}: ", end="")
        if result == expected:
            print("GOOD!")
        else:
            print(f"Wrong! Expected: {expected}, got: {result}")
    else:
        print(f"Running main test {args}...")

import json, hashlib

summary = json.dumps(final_results)
h = hashlib.sha512(summary.encode()).digest()

GOOD_HASH = "d0005f495c306f7e84551a4c74b82775185ede67"
ENC_FLAG = (
    "f17e7089182a1dc151b90cdbdc8e143a3ad85329ba9009f7d51e70f48c37ef06"
    "3050a036f5aeacfab80f0d65"
)

if h[:20].hex() == GOOD_HASH:
    print("Congrats! Here's the flag:")
    flag = bytes([f ^ h for f, h in zip(bytes.fromhex(ENC_FLAG), h[20:])])
    print(flag.decode().strip())
else:
    print("One or more results were wrong!")
