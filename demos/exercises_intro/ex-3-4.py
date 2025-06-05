#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
def rect(w, h):
  for _ in range(h):
    print('*' * w)





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
func = rect
final_results = []
for args, expected_output in [
  ((1, 1), "*\n"),
  ((2, 3), "**\n**\n**\n"),
  ((3, 2), "***\n***\n"),
  ((4, 4), None),
  ((1, 1), None),
  ((5, 3), None),
  ((3, 5), None),
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

GOOD_HASH = "e54b1c7cdb82135d014783dbdd3c91b9106dceb6"
ENC_FLAG = ("0a6cb91cf0c5626aa1057072cef3b6c1841130412e5a"
            "0874821d016b63629579cfa622b916ec8700f634435e")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

