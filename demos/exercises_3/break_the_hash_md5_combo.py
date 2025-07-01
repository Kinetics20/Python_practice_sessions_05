import os
from check_h import check_hash


target = "e903d2c82106d626f4986799ce2b55a4"
hash_type = "md5"


base_path = os.path.dirname(os.path.abspath(__file__))
wordlist_path = os.path.join(base_path, "wordlist.txt")


with open(wordlist_path) as f:
    words = [line.strip() for line in f if line.strip()]


found = False
for w1 in words:
    for w2 in words:
        for number in range(100):  # 00 - 99
            candidate = f"{w1}{w2}{number:02d}"
            if check_hash(candidate, target, hash_type):
                print(f"✅ Found password: {candidate}")
                found = True
                break
        if found:
            break
    if found:
        break

if not found:
    print("❌ Password didn't find.")
