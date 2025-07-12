import hashlib
import requests
import time
import struct
from pathlib import Path
import json


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

    try:
        response = requests.get(url, params=params, timeout=60)

        if response.status_code == 200:
            return response.json()['hash']
        else:
            print(f"Error getting hash: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception getting hash: {e}")
        return None


def get_server_data(offset, pow_token):
    """Gets 32 bytes of data from server"""
    url = "https://py10-day4-577570284557.europe-west1.run.app/ex4/get-data"
    params = {
        'offset': offset,
        'pow': pow_token
    }

    try:
        response = requests.get(url, params=params, timeout=60)

        if response.status_code == 200:
            return bytes.fromhex(response.json()['data'])
        else:
            print(f"Error getting data: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception getting data: {e}")
        return None


def save_progress(progress_file, processed_blocks, corrections):
    """Save progress to file"""
    progress_data = {
        'processed_blocks': processed_blocks,
        'corrections': corrections,
        'timestamp': time.time()
    }
    with open(progress_file, 'w') as f:
        json.dump(progress_data, f)


def load_progress(progress_file):
    """Load progress from file"""
    try:
        with open(progress_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {'processed_blocks': set(), 'corrections': [], 'timestamp': 0}


def fix_broken_png():
    """Main function to fix PNG file - processes in batches"""

    # Load broken file
    broken_file = Path("brokenflag.png")
    if not broken_file.exists():
        print("ERROR: brokenflag.png not found!")
        return

    with open(broken_file, 'rb') as f:
        broken_data = bytearray(f.read())

    file_size = len(broken_data)
    total_blocks = (file_size + 31) // 32

    print(f"File size: {file_size} bytes")
    print(f"Total blocks to check: {total_blocks}")

    # Load progress
    progress_file = "repair_progress.json"
    progress = load_progress(progress_file)
    processed_blocks = set(progress['processed_blocks'])
    total_corrections = len(progress['corrections'])

    print(f"Previously processed blocks: {len(processed_blocks)}")
    print(f"Previous corrections: {total_corrections}")

    # Process in batches to stay within token time limit
    BATCH_SIZE = 6  # Conservative: 6 blocks * 10s = 60s + corrections time < 120s

    batch_num = 0

    for batch_start in range(0, file_size, BATCH_SIZE * 32):
        batch_end = min(batch_start + BATCH_SIZE * 32, file_size)
        batch_blocks = []

        # Collect blocks for this batch (skip already processed)
        for offset in range(batch_start, batch_end, 32):
            block_idx = offset // 32
            if block_idx not in processed_blocks:
                batch_blocks.append(offset)

        # Skip if all blocks in this batch are already processed
        if not batch_blocks:
            continue

        batch_num += 1
        print(f"\n=== BATCH {batch_num} ===")
        print(f"Processing blocks: {[b // 32 for b in batch_blocks]} (offsets: {batch_blocks})")

        # Get fresh token for this batch
        pow_token = get_fresh_pow_token()
        batch_start_time = time.time()

        # Process blocks in this batch
        batch_corrections = 0

        for offset in batch_blocks:
            # Check time - if getting close to token expiry, stop this batch
            elapsed = time.time() - batch_start_time
            if elapsed > 100:  # 100s safety margin
                print(f"Approaching token expiry ({elapsed:.1f}s), stopping batch")
                break

            block_idx = offset // 32
            block_size = min(32, file_size - offset)

            print(f"  Checking block {block_idx} (offset {offset})...")

            # Get local fragment
            local_block = broken_data[offset:offset + block_size]
            if len(local_block) < 32:
                local_block += b'\x00' * (32 - len(local_block))  # Pad with zeros

            # Calculate hash of local fragment
            local_hash = hashlib.sha256(local_block).hexdigest()

            # Get hash from server
            server_hash = get_server_hash(offset, 32, pow_token)

            if server_hash is None:
                print(f"    Failed to get server hash for offset {offset}")
                continue

            print(f"    Local={local_hash[:8]}..., Server={server_hash[:8]}...")

            # If hash differs, get correct data
            if local_hash != server_hash:
                print(f"    MISMATCH! Getting correct data...")

                correct_data = get_server_data(offset, pow_token)
                if correct_data is None:
                    print(f"    Failed to get correct data for offset {offset}")
                    continue

                # Replace corrupted data
                end_offset = min(offset + 32, file_size)
                broken_data[offset:end_offset] = correct_data[:end_offset - offset]
                batch_corrections += 1
                total_corrections += 1

                print(f"    ✓ Corrected block {block_idx}")
            else:
                print(f"    ✓ Block {block_idx} is OK")

            # Mark as processed
            processed_blocks.add(block_idx)

        print(f"Batch completed: {batch_corrections} corrections made")

        # Save progress after each batch
        save_progress(progress_file, list(processed_blocks), [])

        # Save intermediate file
        intermediate_file = "fixed_flag_progress.png"
        with open(intermediate_file, 'wb') as f:
            f.write(broken_data)

        print(f"Progress saved. Total processed: {len(processed_blocks)}/{total_blocks}")
        print(f"Total corrections so far: {total_corrections}")

        # Small delay between batches
        time.sleep(2)

    print(f"\n=== REPAIR COMPLETED ===")
    print(f"Total corrections made: {total_corrections}")
    print(f"Processed blocks: {len(processed_blocks)}/{total_blocks}")

    # Save final file
    fixed_file = "fixed_flag.png"
    with open(fixed_file, 'wb') as f:
        f.write(broken_data)

    print(f"Fixed file saved as: {fixed_file}")

    # Check if it's really a PNG
    if broken_data.startswith(b'\x89PNG\r\n\x1a\n'):
        print("✓ File has correct PNG header")
    else:
        print("✗ File doesn't have PNG header")

    # Clean up progress file
    try:
        Path(progress_file).unlink()
        Path("fixed_flag_progress.png").unlink(missing_ok=True)
    except:
        pass

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
    print("=== PNG File Repair Tool (Batch Processing) ===")
    print("This will compare brokenflag.png with server and fix differences")
    print("Processing in batches to respect PoW token time limits")
    print("WARNING: This process will take 30-60 minutes!")
    print("\nYou can interrupt and resume - progress is saved automatically")

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
        print("Progress has been saved. You can resume by running the script again.")
    except Exception as e:
        print(f"\nError: {e}")
        import traceback

        traceback.print_exc()