#!/usr/bin/python3

# Stwórz odpowiednią funkcję poniżej.
def dict_conv(num_1, num_2, word):
  return {
    'success': True,
    'result': num_1 + num_2,
    'comment': word
  }










# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = dict_conv
final_results = []
for args, expected_result in [
  ((1, 2, "liczby"), {
    "success": True,
    "result": 3,
    "comment": "liczby"
  }),
  (("ala", "ma", "kota"), {
    "comment": "kota",
    "result": "alama",
    "success": True,
  }),
  ((777, 333, "this is a comment"), None),
  (("asdf", "xyz", "wow it can concat too"), None),
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
GOOD_HASH = "f10d9480b063e6d0d7a07c72ef69da973a117ba9"
ENC_FLAG = ("734cf1aa700139791a8324112fea5a89ea12747e257a"
            "d0642492e630992ba1aef5b383cd72668f57fca46790")


if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

