#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
def answer_question(question):
  return 42


# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = answer_question
final_results = []
for args, expected_result in [
  (("What is the Answer to the Ultimate Question of Life, the Universe,"
    " and Everything?",), 42),
  (("What do you get when you multiply six by nine?",), None),
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
GOOD_HASH = "b600dea838270afa49783cd2c91844ae4948fc3a"
ENC_FLAG = ("9c6e1c44cabffdd6ed5a7284426a0df1599176f5a21f"
            "051a163429f9ad516fc6e681802583e60459c1642f40")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

