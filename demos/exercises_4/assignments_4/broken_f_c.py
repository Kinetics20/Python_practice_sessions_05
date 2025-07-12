import hashlib
import requests
import time
import struct


def test_pow_correct():
    print("Getting fresh challenge...")
    response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
    challenge_hex = response.json()['challenge']
    print(f"Challenge (hex): {challenge_hex}")

    # Decode hex challenge to bytes
    challenge_bytes = bytes.fromhex(challenge_hex)
    print(f"Challenge (bytes): {challenge_bytes}")
    print(f"Challenge length: {len(challenge_bytes)} bytes")

    print("Searching for PoW with top 24 bits = 1...")
    nonce = 0
    start_time = time.time()

    while True:
        # Create candidate: challenge_bytes + nonce as 4-byte little-endian
        nonce_bytes = struct.pack('<I', nonce)  # 4-byte little-endian
        candidate_bytes = challenge_bytes + nonce_bytes

        # Calculate SHA256 hash
        hash_bytes = hashlib.sha256(candidate_bytes).digest()

        # Check if top 24 bits are 1 (first 3 bytes should be 0xFF)
        if hash_bytes[:3] == b'\xff\xff\xff':
            elapsed = time.time() - start_time
            hash_hex = hash_bytes.hex()
            print(f"FOUND! Nonce: {nonce}, Hash: {hash_hex} (took {elapsed:.1f}s)")

            # PoW token is the full candidate as hex string
            pow_token = candidate_bytes.hex()
            print(f"PoW token: {pow_token}")

            # Test if server accepts it
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
            if elapsed > 100:  # Increased timeout since this is harder
                print("Taking too long, challenge might expire!")
                return False, None


def test_pow_alternative():
    """Alternative implementation with 8-byte nonce"""
    print("\nTrying alternative with 8-byte nonce...")
    response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
    challenge_hex = response.json()['challenge']
    challenge_bytes = bytes.fromhex(challenge_hex)

    nonce = 0
    start_time = time.time()

    while True:
        # Try with 8-byte nonce
        nonce_bytes = struct.pack('<Q', nonce)  # 8-byte little-endian
        candidate_bytes = challenge_bytes + nonce_bytes

        hash_bytes = hashlib.sha256(candidate_bytes).digest()

        if hash_bytes[:3] == b'\xff\xff\xff':
            elapsed = time.time() - start_time
            hash_hex = hash_bytes.hex()
            print(f"FOUND! Nonce: {nonce}, Hash: {hash_hex} (took {elapsed:.1f}s)")

            pow_token = candidate_bytes.hex()
            print(f"PoW token: {pow_token}")

            # Test server
            test_url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
            test_params = {'offset': 0, 'size': 32, 'pow': pow_token}

            try:
                test_response = requests.get(test_url, params=test_params, timeout=30)
                if test_response.status_code == 200:
                    print(f"✓ SUCCESS with 8-byte nonce!")
                    return True, pow_token
                else:
                    print(f"✗ Server rejected: {test_response.status_code}")
                    return False, None
            except Exception as e:
                print(f"✗ Server error: {e}")
                return False, None

        nonce += 1

        if nonce % 10000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")

            if elapsed > 100:
                print("Taking too long!")
                return False, None


# Test both methods
print("=== Testing 4-byte nonce method ===")
success, token = test_pow_correct()

if not success:
    print("\n=== Testing 8-byte nonce method ===")
    success, token = test_pow_alternative()

if success:
    print(f"\n✓ CONFIRMED: PoW method works!")
    print(f"Final token: {token}")
else:
    print(f"\n✗ Both methods failed")

    # Debug info
    print("\nDebug info:")
    response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
    challenge_hex = response.json()['challenge']
    challenge_bytes = bytes.fromhex(challenge_hex)
    print(f"Challenge hex: {challenge_hex}")
    print(f"Challenge bytes: {challenge_bytes}")
    print(f"Challenge length: {len(challenge_bytes)} bytes")

    # Show what top 24 bits = 1 means
    print(f"\nTop 24 bits = 1 means hash should start with: {b'\\xff\\xff\\xff'.hex()}")
    print("This is much harder than finding 0000 pattern!")
