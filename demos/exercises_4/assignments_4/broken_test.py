import hashlib
import requests
import time

# Get challenge
response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
challenge = response.json()['challenge']
print(f"Challenge: {challenge}")

# Decode challenge from hex
try:
    challenge_bytes = bytes.fromhex(challenge)
    print(f"Challenge decoded: {challenge_bytes}")
except:
    print("Could not decode challenge as hex")
    challenge_bytes = challenge.encode()

# Test different patterns
patterns = ['000000', '0000', 'ffffff', 'ffff']

for pattern in patterns:
    print(f"\nTesting pattern: {pattern}")
    nonce = 0
    start_time = time.time()

    while nonce < 50000:  # Test only first 50k
        # Method 1: challenge_bytes + nonce_bytes
        nonce_bytes = nonce.to_bytes(4, 'big')
        candidate_bytes = challenge_bytes + nonce_bytes
        hash_val = hashlib.sha256(candidate_bytes).hexdigest()

        if hash_val.startswith(pattern):
            print(f"FOUND! Pattern: {pattern}, Nonce: {nonce}, Hash: {hash_val}")

            # Create PoW token - challenge + nonce as hex
            pow_token = challenge + nonce.to_bytes(4, 'big').hex()
            print(f"PoW token: {pow_token}")

            # Test if server accepts it
            test_url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
            test_params = {
                'offset': 0,
                'size': 32,
                'pow': pow_token
            }

            try:
                test_response = requests.get(test_url, params=test_params, timeout=30)
                if test_response.status_code == 200:
                    print(f"✓ Server accepts this PoW!")
                    print(f"Response: {test_response.json()}")
                    exit(0)  # Success!
                else:
                    print(f"✗ Server rejected: {test_response.status_code}")
                    print(f"Response: {test_response.text}")
            except Exception as e:
                print(f"✗ Server error: {e}")
            break

        nonce += 1

        if nonce % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")

    if nonce >= 50000:
        print(f"  No solution found in first 50k attempts")

# Also try method 2: challenge_hex + nonce_hex
print("\n" + "=" * 50)
print("TRYING METHOD 2: challenge_hex + nonce_hex")

for pattern in patterns:
    print(f"\nTesting pattern: {pattern}")
    nonce = 0
    start_time = time.time()

    while nonce < 50000:
        # Method 2: challenge_hex + nonce_hex
        nonce_hex = f"{nonce:08x}"  # 8 hex digits
        candidate_hex = challenge + nonce_hex
        candidate_bytes = bytes.fromhex(candidate_hex)
        hash_val = hashlib.sha256(candidate_bytes).hexdigest()

        if hash_val.startswith(pattern):
            print(f"FOUND! Pattern: {pattern}, Nonce: {nonce}, Hash: {hash_val}")

            # PoW token is the full hex string
            pow_token = candidate_hex
            print(f"PoW token: {pow_token}")

            # Test if server accepts it
            test_url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
            test_params = {
                'offset': 0,
                'size': 32,
                'pow': pow_token
            }

            try:
                test_response = requests.get(test_url, params=test_params, timeout=30)
                if test_response.status_code == 200:
                    print(f"✓ Server accepts this PoW!")
                    print(f"Response: {test_response.json()}")
                    exit(0)  # Success!
                else:
                    print(f"✗ Server rejected: {test_response.status_code}")
                    print(f"Response: {test_response.text}")
            except Exception as e:
                print(f"✗ Server error: {e}")
            break

        nonce += 1

        if nonce % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")

    if nonce >= 50000:
        print(f"  No solution found in first 50k attempts")