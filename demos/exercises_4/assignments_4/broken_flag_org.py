import hashlib
import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor

BASE_URL = "https://py10-day4-577570284557.europe-west1.run.app"
FILENAME = "brokenflag.png"
OUTPUT_FILE = "fixedflag.png"
BLOCK_SIZE = 32
THREADS = 3


def get_pow_token():
    """Fetch a PoW challenge and find a valid token (SHA256 starts with ffffff)."""
    resp = requests.get(f"{BASE_URL}/ex4/get-pow").json()
    challenge = bytes.fromhex(resp["challenge"])

    while True:
        suffix = os.urandom(8)
        token = challenge + suffix
        if hashlib.sha256(token).hexdigest().startswith("ffffff"):
            return token.hex()


def get_remote_hash(offset, size, pow_token):
    """Get SHA256 hash of a valid block on the server."""
    time.sleep(10)
    resp = requests.get(
        f"{BASE_URL}/ex4/get-hash",
        params={"offset": offset, "size": size, "pow": pow_token}
    )
    return resp.text.strip()


def get_remote_data(offset, pow_token):
    """Get the actual 32-byte valid block from the server."""
    time.sleep(30)
    resp = requests.get(
        f"{BASE_URL}/ex4/get-data",
        params={"offset": offset, "pow": pow_token}
    )
    return bytes.fromhex(resp.text.strip())


def process_block(offset, original_block):
    """Check if a block is corrupted; if yes, fetch a valid one."""
    print(f"[ ] Offset {offset}: thread started")

    pow_token = get_pow_token()
    remote_hash = get_remote_hash(offset, BLOCK_SIZE, pow_token)
    local_hash = hashlib.sha256(original_block).hexdigest()

    if local_hash != remote_hash:
        print(f"[!] Offset {offset}: mismatch detected, downloading correct block")
        pow_token = get_pow_token()
        fixed_block = get_remote_data(offset, pow_token)
        return (offset, fixed_block)
    else:
        print(f"[=] Offset {offset}: block is OK")
        return (offset, original_block)


def main():
    with open(FILENAME, "rb") as f:
        original_data = f.read()

    total_size = len(original_data)
    print(f"[INFO] File size: {total_size} bytes ⇒ {total_size // BLOCK_SIZE} blocks")

    blocks = [
        (offset, original_data[offset:offset + BLOCK_SIZE])
        for offset in range(0, total_size, BLOCK_SIZE)
    ]

    fixed_data = bytearray(original_data)

    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        futures = [executor.submit(process_block, offset, block) for offset, block in blocks]
        for future in futures:
            offset, data = future.result()
            fixed_data[offset:offset + BLOCK_SIZE] = data

    with open(OUTPUT_FILE, "wb") as f:
        f.write(fixed_data)

    print(f"[✅] Fixed file saved as {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
