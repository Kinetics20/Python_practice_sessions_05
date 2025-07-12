import hashlib
import requests
import time
import struct
from pathlib import Path


def get_fresh_pow_token():
    """Gets a new PoW token"""
    print("Getting fresh PoW token...")

    # Get challenge
    response = requests.get("https://py10-day4-577570284557.europe-west1.run.app/ex4/get-pow")
    challenge_hex = response.json()['challenge']
    challenge_bytes = bytes.fromhex(challenge_hex)

    print(f"Challenge: {challenge_hex}")
    print("Mining PoW token...")

    # Find PoW
    nonce = 0
    start_time = time.time()

    while True:
        nonce_bytes = struct.pack('<I', nonce)
        candidate_bytes = challenge_bytes + nonce_bytes
        hash_bytes = hashlib.sha256(candidate_bytes).digest()

        if hash_bytes[:3] == b'\xff\xff\xff':
            elapsed = time.time() - start_time
            pow_token = candidate_bytes.hex()
            print(f"PoW found! Nonce: {nonce}, Time: {elapsed:.1f}s")
            return pow_token

        nonce += 1

        if nonce % 50000 == 0:
            elapsed = time.time() - start_time
            print(f"  Checked {nonce} in {elapsed:.1f}s...")


def get_server_hash(offset, size, pow_token):
    """Gets hash of file fragment from server"""
    url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-hash"
    params = {
        'offset': offset,
        'size': size,
        'pow': pow_token
    }

    print(f"Getting hash for offset {offset}, size {size}...")
    response = requests.get(url, params=params, timeout=60)

    if response.status_code == 200:
        return response.json()['hash']
    else:
        print(f"Error getting hash: {response.status_code} - {response.text}")
        return None


def get_server_data(offset, pow_token):
    """Gets 32 bytes of data from server"""
    url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-data"
    params = {
        'offset': offset,
        'pow': pow_token
    }

    print(f"Getting data for offset {offset}...")
    response = requests.get(url, params=params, timeout=60)

    if response.status_code == 200:
        return bytes.fromhex(response.json()['data'])
    else:
        print(f"Error getting data: {response.status_code} - {response.text}")
        return None


def fix_broken_png():
    """Main function to fix PNG file"""

    # Load broken file
    broken_file = Path("brokenflag.png")
    if not broken_file.exists():
        print("ERROR: brokenflag.png not found!")
        return

    with open(broken_file, 'rb') as f:
        broken_data = bytearray(f.read())

    file_size = len(broken_data)
    print(f"File size: {file_size} bytes")
    print(f"Blocks to check: {(file_size + 31) // 32}")

    # Get PoW token
    pow_token = get_fresh_pow_token()
    token_start_time = time.time()

    # Check each 32-byte block
    corrections_made = 0

    for offset in range(0, file_size, 32):
        # Check if token is about to expire (115 seconds margin)
        if time.time() - token_start_time > 115:
            print("Token about to expire, getting new one...")
            pow_token = get_fresh_pow_token()
            token_start_time = time.time()

        # Calculate block size (last block might be smaller)
        block_size = min(32, file_size - offset)

        # If block is not full, pad to 32 bytes for comparison
        if block_size < 32:
            padded_size = 32
        else:
            padded_size = 32

        # Get local fragment
        local_block = broken_data[offset:offset + block_size]
        if len(local_block) < 32:
            local_block += b'\x00' * (32 - len(local_block))  # Pad with zeros

        # Calculate hash of local fragment
        local_hash = hashlib.sha256(local_block).hexdigest()

        # Get hash from server
        server_hash = get_server_hash(offset, padded_size, pow_token)

        if server_hash is None:
            print(f"Failed to get server hash for offset {offset}")
            continue

        print(f"Offset {offset}: Local={local_hash[:8]}..., Server={server_hash[:8]}...")

        # If hash differs, get correct data
        if local_hash != server_hash:
            print(f"MISMATCH at offset {offset}! Getting correct data...")

            correct_data = get_server_data(offset, pow_token)
            if correct_data is None:
                print(f"Failed to get correct data for offset {offset}")
                continue

            # Replace corrupted data
            end_offset = min(offset + 32, file_size)
            broken_data[offset:end_offset] = correct_data[:end_offset - offset]
            corrections_made += 1

            print(f"Corrected block at offset {offset}")
        else:
            print(f"Block at offset {offset} is OK")

    print(f"\nTotal corrections made: {corrections_made}")

    # Save fixed file
    fixed_file = "fixed_flag.png"
    with open(fixed_file, 'wb') as f:
        f.write(broken_data)

    print(f"Fixed file saved as: {fixed_file}")

    # Check if it's really a PNG
    if broken_data.startswith(b'\x89PNG\r\n\x1a\n'):
        print("✓ File has correct PNG header")
    else:
        print("✗ File doesn't have PNG header")

    return fixed_file


def verify_fix():
    """Check if fixed file is correct"""
    try:
        from PIL import Image
        img = Image.open("fixed_flag.png")
        print(f"✓ Image opened successfully: {img.size} pixels, mode: {img.mode}")
        img.show()  # Show image
    except ImportError:
        print("PIL not available, can't verify image")
    except Exception as e:
        print(f"Error opening image: {e}")


if __name__ == "__main__":
    print("=== PNG File Repair Tool ===")
    print("This will compare brokenflag.png with server and fix differences")
    print("WARNING: This process will take 30-60 minutes!")

    input("Press Enter to start...")

    start_time = time.time()

    try:
        fixed_file = fix_broken_png()

        if fixed_file:
            elapsed = time.time() - start_time
            print(f"\n=== COMPLETED in {elapsed / 60:.1f} minutes ===")
            print(f"Fixed file: {fixed_file}")

            # Check correctness
            verify_fix()

    except KeyboardInterrupt:
        print("\n\nProcess interrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()