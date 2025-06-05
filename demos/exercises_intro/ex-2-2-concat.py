#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
def concat(a, b, c):
  return c + 2*b + a



# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = concat
final_results = []
for args, expected_result in [
  (("ala", "ma", "kota"), "kotamamaala"),
  (("a", "b", "c"), "cbba"),
  (("asdf", "xyz", "qwerty"), None),
  (("1234", " ", "???"), None),
]:
  if expected_result is not None:
    print(f"Testing {args}: ", end="")
    actual_result = func(*args)
    if actual_result == expected_result:
      print("GOOD!")
    else:
      print(f"Wrong! Expected result: {expected_result}, "
            f"Actual result: {actual_result}")
  else:
    final_results.append(func(*args))

# Kod rozszyfrowujący flagę... jeśli wszystkie testy przeszły :)
import json
import hashlib
tmp = json.dumps(final_results)
hash = hashlib.sha512(tmp.encode()).digest()
GOOD_HASH = "820da424a0e2e3a523ad6f278635fb14aeede385"
ENC_FLAG = ("b1d63c5a40658f2300d535cf67605ae933ea77eb81b9"
            "b17581d6604d27691dee68c02c7b235b71a75491cef4")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

