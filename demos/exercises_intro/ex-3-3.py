#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
def countchar(s, ch):
  return s.count(ch)


# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = countchar
final_results = []
for args, expected_result in [
  (("alamakota", "a"), 4),
  (("kotmaale", "a"), 2),
  (("niebieskieniebo", "i"), 4),
  (("pythonjestfajny", "p"), None),
  (("pythonjestfajny", "j"), None),
  (("pythonjestfajny", "f"), None),
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

GOOD_HASH = "6775d45ff5e6bcb22c57ffaa07a4d2185230b473"
ENC_FLAG = ("0ddad4d34d3fd8ae647155e3f73d4980f316f24e8219"
            "c123b5205764071bb92f8ab1ce0e4adc00a66384a131")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

