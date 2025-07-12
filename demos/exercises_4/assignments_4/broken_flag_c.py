import hashlib
import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue
import os

BASE_URL = "https://py10-day4-577570284557.europe-west1.run.app"


class PNGRepairer:
    def __init__(self, broken_file_path, max_workers=4):
        self.broken_file_path = broken_file_path
        self.max_workers = max_workers
        self.pow_token = None
        self.pow_expiry = 0
        self.session = requests.Session()
        self.lock = threading.Lock()

        # Load broken file
        with open(broken_file_path, 'rb') as f:
            self.broken_data = bytearray(f.read())

        self.file_size = len(self.broken_data)
        print(f"File size: {self.file_size} bytes")

        # Queue of blocks to check
        self.blocks_to_check = Queue()
        self.corrupted_blocks = []

    def get_pow_token(self):
        """Get new PoW token"""
        try:
            response = self.session.get(f"{BASE_URL}/ex4/get-pow", timeout=30)
            response.raise_for_status()
            data = response.json()

            challenge = data['challenge']
            print(f"PoW challenge: {challenge}")

            # Find nonce for challenge
            nonce = 0
            while True:
                candidate = f"{challenge}{nonce}"
                hash_val = hashlib.sha256(candidate.encode()).hexdigest()
                if hash_val.startswith('0000'):  # Adjust number of zeros as needed
                    pow_token = candidate
                    break
                nonce += 1

                if nonce % 10000 == 0:
                    print(f"Checked {nonce} combinations...")

            print(f"Found PoW: {pow_token}")
            with self.lock:
                self.pow_token = pow_token
                self.pow_expiry = time.time() + 110  # 110 seconds for safety

            return pow_token

        except Exception as e:
            print(f"Error getting PoW: {e}")
            return None

    def ensure_valid_pow(self):
        """Ensure we have a valid PoW token"""
        with self.lock:
            if not self.pow_token or time.time() > self.pow_expiry:
                print("Getting new PoW token...")
                return self.get_pow_token()
            return self.pow_token

    def get_hash_from_server(self, offset, size):
        """Get hash from server"""
        pow_token = self.ensure_valid_pow()
        if not pow_token:
            return None

        try:
            url = f"{BASE_URL}/ex4/get-hash"
            params = {
                'offset': offset,
                'size': size,
                'pow': pow_token
            }

            response = self.session.get(url, params=params, timeout=40)
            response.raise_for_status()

            return response.json()['hash']

        except Exception as e:
            print(f"Error getting hash for offset={offset}, size={size}: {e}")
            return None

    def get_data_from_server(self, offset):
        """Get 32 bytes of data from server"""
        pow_token = self.ensure_valid_pow()
        if not pow_token:
            return None

        try:
            url = f"{BASE_URL}/ex4/get-data"
            params = {
                'offset': offset,
                'pow': pow_token
            }

            response = self.session.get(url, params=params, timeout=40)
            response.raise_for_status()

            return bytes.fromhex(response.json()['data'])

        except Exception as e:
            print(f"Error getting data for offset={offset}: {e}")
            return None

    def find_corrupted_blocks_binary_search(self, start_offset, end_offset):
        """Find corrupted blocks using binary search"""
        if end_offset - start_offset <= 32:
            return [start_offset] if start_offset < self.file_size else []

        # Check hash of entire range
        size = end_offset - start_offset
        if size % 32 != 0:
            size = (size // 32) * 32

        if size <= 0:
            return []

        server_hash = self.get_hash_from_server(start_offset, size)
        if not server_hash:
            return []

        # Calculate hash from our data
        our_data = self.broken_data[start_offset:start_offset + size]
        our_hash = hashlib.sha256(our_data).hexdigest()

        if server_hash == our_hash:
            print(f"Block {start_offset}-{start_offset + size} is correct")
            return []

        print(f"Block {start_offset}-{start_offset + size} is corrupted, splitting...")

        # Split range in half
        mid_offset = start_offset + (size // 2)
        mid_offset = (mid_offset // 32) * 32  # Align to 32

        corrupted = []
        corrupted.extend(self.find_corrupted_blocks_binary_search(start_offset, mid_offset))
        corrupted.extend(self.find_corrupted_blocks_binary_search(mid_offset, end_offset))

        return corrupted

    def find_all_corrupted_blocks(self):
        """Find all corrupted blocks using binary search"""
        print("Starting search for corrupted blocks...")

        # Initial range is entire file aligned to 32
        aligned_size = (self.file_size // 32) * 32

        self.corrupted_blocks = self.find_corrupted_blocks_binary_search(0, aligned_size)

        print(f"Found {len(self.corrupted_blocks)} corrupted blocks: {self.corrupted_blocks}")
        return self.corrupted_blocks

    def repair_block(self, offset):
        """Repair single block"""
        print(f"Repairing block at offset {offset}")

        correct_data = self.get_data_from_server(offset)
        if correct_data:
            self.broken_data[offset:offset + 32] = correct_data
            print(f"Repaired block at offset {offset}")
            return True
        else:
            print(f"Failed to repair block at offset {offset}")
            return False

    def repair_all_blocks(self):
        """Repair all corrupted blocks"""
        if not self.corrupted_blocks:
            print("No blocks to repair")
            return

        print(f"Repairing {len(self.corrupted_blocks)} blocks...")

        # Use multithreading to repair blocks
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.repair_block, offset): offset
                       for offset in self.corrupted_blocks}

            for future in as_completed(futures):
                offset = futures[future]
                try:
                    success = future.result()
                    if success:
                        print(f"✓ Repaired block {offset}")
                    else:
                        print(f"✗ Failed to repair block {offset}")
                except Exception as e:
                    print(f"✗ Error repairing block {offset}: {e}")

    def save_repaired_file(self, output_path):
        """Save repaired file"""
        with open(output_path, 'wb') as f:
            f.write(self.broken_data)
        print(f"Saved repaired file: {output_path}")

    def verify_repair(self):
        """Verify repair by checking hash of entire file"""
        print("Verifying repair...")

        # Check hash of entire file
        aligned_size = (self.file_size // 32) * 32
        server_hash = self.get_hash_from_server(0, aligned_size)

        if server_hash:
            our_hash = hashlib.sha256(self.broken_data[:aligned_size]).hexdigest()
            if server_hash == our_hash:
                print("✓ File successfully repaired!")
                return True
            else:
                print("✗ File still contains errors")
                return False
        else:
            print("Failed to verify repair")
            return False


def main():
    repairer = PNGRepairer('brokenflag.png', max_workers=4)

    # Step 1: Find corrupted blocks
    corrupted_blocks = repairer.find_all_corrupted_blocks()

    if not corrupted_blocks:
        print("File contains no corrupted blocks!")
        return

    # Step 2: Repair corrupted blocks
    repairer.repair_all_blocks()

    # Step 3: Verify repair
    if repairer.verify_repair():
        # Step 4: Save repaired file
        repairer.save_repaired_file('repaired_flag.png')
        print("Repair completed successfully!")
    else:
        print("Repair did not complete successfully")


if __name__ == "__main__":
    main()