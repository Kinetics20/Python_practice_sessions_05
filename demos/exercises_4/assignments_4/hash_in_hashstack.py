import hashlib
import re

hash_target = "790d88483531ac32a12a57b233818ff698fb4ed7011f5c749f3b7493ba1ac5e1"
block_size = 512

with open("hashstack.bin", "rb") as f:
    block_number = 0
    while True:
        block = f.read(block_size)
        if not block:
            print("❌ No matching block found.")
            break

        if hashlib.sha256(block).hexdigest() == hash_target:
            print(f"\n✅ Matching block found! (block #{block_number})")

            try:
                decoded = block.decode()
            except UnicodeDecodeError:
                print("❌ Failed to decode the block as text.")
                break

            print("\n📦 Decoded block content:\n")
            print(decoded)

            match = re.search(r"Flag:\s+(.*)", decoded)
            if match:
                raw_flag = match.group(1)
                clean_flag = raw_flag.replace(" ", "")[::-1]
                print(f"\n🏁 Final flag: {clean_flag}")
            else:
                print("❗ 'Flag:' pattern not found in the text.")
            break

        block_number += 1
