import hashlib
import requests
import time

# Get challenge
response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
challenge = response.json()['challenge']
print(f"Challenge: {challenge}")

# Test different patterns
patterns = ['000000', '0000', 'ffffff', 'ffff']

for pattern in patterns:
    print(f"\nTesting pattern: {pattern}")
    nonce = 0
    start_time = time.time()

    while nonce < 50000:  # Test only first 50k
        candidate = f"{challenge}{nonce}"
        hash_val = hashlib.sha256(candidate.encode()).hexdigest()

        if hash_val.startswith(pattern):
            print(f"FOUND! Pattern: {pattern}, Nonce: {nonce}, Hash: {hash_val}")

            # Test if server accepts it
            test_url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
            test_params = {
                'offset': 0,
                'size': 32,
                'pow': candidate
            }

            try:
                test_response = requests.get(test_url, params=test_params, timeout=30)
                if test_response.status_code == 200:
                    print(f"✓ Server accepts this PoW!")
                    break
                else:
                    print(f"✗ Server rejected: {test_response.status_code}")
            except Exception as e:
                print(f"✗ Server error: {e}")
            break

        nonce += 1

        if nonce % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")

    if nonce >= 50000:
        print(f"  No solution found in first 50k attempts")