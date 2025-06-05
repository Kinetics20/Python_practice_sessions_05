#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
def list_me(a, b, c):
  return [a, b, c][::-1]



# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = list_me
final_results = []
for args, expected_result in [
  ((1, None, "sowa"), ["sowa", None, 1]),
  (("ala", "ma", "kota"), ["kota", "ma", "ala"]),
  (("asdf", 1234, True), None),
  ((1, 2, 3), None),
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

GOOD_HASH = "afa7a4831e62606c354974698bbfffe22c18b835"
ENC_FLAG = ("87e81e98005e1a494b51a9592a49c078aa6642456edf"
            "ee1ebaf54284ee299985c183856ea1623a4b9689619a")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

