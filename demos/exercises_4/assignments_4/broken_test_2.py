import hashlib
import requests
import time


def test_pow_method():
    print("Getting fresh challenge...")
    response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
    challenge = response.json()['challenge']
    print(f"Challenge: {challenge}")

    # Decode challenge from hex
    challenge_bytes = bytes.fromhex(challenge)
    print(f"Challenge decoded: {challenge_bytes.hex()}")

    print("Searching for PoW with pattern 0000...")
    nonce = 0
    start_time = time.time()

    while True:
        # Method 1: challenge_bytes + nonce_bytes
        nonce_bytes = nonce.to_bytes(4, 'big')
        candidate_bytes = challenge_bytes + nonce_bytes
        hash_val = hashlib.sha256(candidate_bytes).hexdigest()

        if hash_val.startswith('0000'):
            elapsed = time.time() - start_time
            print(f"FOUND! Nonce: {nonce}, Hash: {hash_val} (took {elapsed:.1f}s)")

            # Create PoW token - challenge + nonce as hex
            pow_token = challenge + nonce.to_bytes(4, 'big').hex()
            print(f"PoW token: {pow_token}")

            # IMMEDIATELY test if server accepts it
            print("Testing server acceptance...")
            test_url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
            test_params = {
                'offset': 0,
                'size': 32,
                'pow': pow_token
            }

            try:
                test_response = requests.get(test_url, params=test_params, timeout=30)
                if test_response.status_code == 200:
                    print(f"✓ SUCCESS! Server accepts this PoW method!")
                    print(f"Response: {test_response.json()}")
                    return True, pow_token
                else:
                    print(f"✗ Server rejected: {test_response.status_code}")
                    print(f"Response: {test_response.text}")
                    return False, None
            except Exception as e:
                print(f"✗ Server error: {e}")
                return False, None

        nonce += 1

        if nonce % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")

            # Safety check - if taking too long, challenge might expire
            if elapsed > 60:
                print("Taking too long, challenge might expire!")
                return False, None


# Test the method
success, token = test_pow_method()
if success:
    print(f"\n✓ CONFIRMED: PoW method works!")
    print(f"Pattern: 0000")
    print(f"Method: challenge_bytes + nonce_bytes -> hash")
    print(f"Token format: challenge_hex + nonce_hex")
else:
    print(f"\n✗ PoW method failed")