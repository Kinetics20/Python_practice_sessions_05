#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
# def get_opinion(number):
#   if number < 0:
#     return 'meh'
#   if number == 41:
#     return 'almost'
#   if number == 42:
#     return 'yes!'
#   if not number & 1:
#     return 'even'
#   return '???'

# def get_opinion(number):
#   match number:
#     case n if n < 0:
#         return 'meh'
#     case 41:
#       return 'almost'
#     case 42:
#       return 'yes!'
#     case n if n % 2 == 0:
#       return 'even'
#     case _:
#       return '???'

# def get_opinion(number):
#   special_cases = {41: 'almost', 42: 'yes!'}
#
#   if number < 0:
#     return 'meh'
#   if number in special_cases:
#     return special_cases[number]
#   if number % 2 == 0:
#     return 'even'
#   return '???'

def get_opinion(n):
  return (
    'meh' if n < 0 else
    'almost' if n == 41 else
    'yes!' if n == 42 else
    'even' if n % 2 == 0 else
    '???'
  )

# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = get_opinion
final_results = []
for args, expected_result in [
  ((-1,), "meh"),
  ((1,), "???"),
  ((2,), "even"),
  ((3,), "???"),
  ((41,), "almost"),
  ((42,), "yes!"),
  ((-712,), None),
  ((0,), None),
  ((768,), None),
  ((41,), None),
  ((42,), None),
  ((333,), None),
  ((17,), None),
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

GOOD_HASH = "2d65807b7f942f9efaa9657d9209a2e876c5aae6"
ENC_FLAG = ("67563c9239b4a267d03ce282c40e838094d74b66ac32"
            "b9ed2d4b6b380e018f69e108c62241a1a0eda2d14277")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

