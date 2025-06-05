#!/usr/bin/python3

# Uzupełnij poniższą funkcję.
# def weirdsum(a):
#   return sum(value * index for index, value in enumerate(a))

def weirdsum(a):
  total = 0
  for i in range(len(a)):
    total += a[i] * i
  return total

# -----------------------------------------------------------------------------
# Wszystko poniżej tego miejsca możesz zostawić bez zmian.
# Ale możesz na to patrzeć! Wręcz zachęcam :)

# Kod testujący.
func = weirdsum
final_results = []
for args, expected_result in [
  (([2,6,3,1],), 15),
  (([5,5,5,5],), 30),
  (([0,0,0,0,0,0,0],), 0),
  (([-1,1,-1,1,-1,1],), 3),
  (([125,182,1264,8912,1235,8581],), None),
  (([1,8912,7,1235,12,8581],), None),
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

GOOD_HASH = "0faa69b263bbe594e0832873cf3843f935cf964f"
ENC_FLAG = ("2db94f9ff7a641d82bbf28cf25334c774a3391efe63c"
            "4c8162c5470c894c34c9615acabce98a1a4befb76004")

if hash[:20].hex() == GOOD_HASH:
  print("Congratz! Here's the flag:")
  flag = bytes([f ^ h for f, h in zip(b''.fromhex(ENC_FLAG), hash[20:])])
  print(flag.decode().strip())
else:
  print("Results of main tests were wrong!")

