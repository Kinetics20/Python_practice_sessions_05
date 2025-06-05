#!/usr/bin/python3

# Uzupełnij poniższą funkcję.


import json

def stats(fname):
    with open(fname, "r", encoding="utf-8") as f:
        data = json.load(f)

    typ = data["type"]
    days = data["days"]
    total = sum(entry["count"] for entry in days)

    print(f"Type: >{typ}<")
    print(f"Days: {len(days)} days")
    print(f"Total: {total} {typ}")


# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Muszę przechwycić to co jest wypisywane, żeby móc to sobie porównać.
# Kod testujący jest niżej.
import io
import sys
class StdOutHijacker:
  def __init__(self, original=sys.stdout):
    self._original = original
    self.buffer = io.StringIO()

  def attach(self):
    sys.stdout = self

  def detach(self):
    sys.stdout = self._original  # Detach.
    value = self.buffer.getvalue()
    self.buffer = io.StringIO()
    return value

  def write(self, data):
    self._original.write(data)
    self.buffer.write(data)

  def __getattr__(self, name):
    return getattr(self._original, name)

# Kod testujący.
hijacker = StdOutHijacker()
func = stats
final_results = []
for args, expected_output in [
  (("ghosts.json",), "Type: >ghosts<\nDays: 9 days\nTotal: 202 ghosts\n"),
  (("wraiths.json",), "Type: >wraiths<\nDays: 8 days\nTotal: 21 wraiths\n"),
  (("spectres.json",), None),
  (("ghouls.json",), None)
]:
  if expected_output is not None:
    print(f"---Testing {args}:")
    hijacker.attach()
    func(*args)
    actual_output = hijacker.detach()
    if actual_output == expected_output:
      print("---GOOD!\n")
    else:
      print("---Wrong! Expected output:")
      print(expected_output)
      print("---\n")
  else:
    print(f"---Testing {args}...")
    hijacker.attach()
    func(*args)
    actual_output = hijacker.detach()
    final_results.append(actual_output)
    print()


# Kod rozszyfrowujący flagę... jeśli wszystkie testy przeszły :)

import json
import hashlib
tmp = json.dumps(final_results)
hash = hashlib.sha512(tmp.encode()).digest()

GOOD_HASH = "767a8fe14396ea3bd3dac0370b25d82d405b8f81"
ENC_FLAG = ("0b696f1694bb8770d4417abe8beab5739af7d9a5f3ba"
            "11fa6564670f285e0488688e803afe60b5738fa930d4")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

