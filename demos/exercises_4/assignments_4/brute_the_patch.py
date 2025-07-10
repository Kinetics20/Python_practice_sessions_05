import hashlib
import json
import zipfile


def read_file_data():
    """Reads data from files"""
    with open('broken.zip.bin', 'rb') as f:
        data = bytearray(f.read())

    with open('hashes.json', 'r') as f:
        correct_hashes = json.load(f)

    return data, correct_hashes


def calculate_sha256(block):
    """Calculates SHA256 for given block"""
    return hashlib.sha256(block).hexdigest()


def repair_file(data, correct_hashes):
    """Repairs corrupted file using bruteforce"""
    print(f"File size: {len(data)} bytes")
    print(f"Number of 32-byte blocks: {len(data) // 32}")
    print(f"Number of correct hashes: {len(correct_hashes)}")

    if len(data) % 32 != 0:
        print("WARNING: File size is not a multiple of 32!")

    for block_index in range(0, len(data), 32):
        block_end = min(block_index + 32, len(data))
        current_block = data[block_index:block_end]

        if len(current_block) < 32:
            current_block = bytearray(current_block)
            current_block.extend([0] * (32 - len(current_block)))

        current_hash = calculate_sha256(current_block)
        block_num = block_index // 32

        print(f"Checking block {block_num}: ", end="")

        if current_hash in correct_hashes:
            print("OK")
            continue

        print("CORRUPTED - repairing...")

        repaired = False

        for byte_pos in range(len(current_block)):
            if repaired:
                break

            original_byte = current_block[byte_pos]

            for new_byte_value in range(256):
                if new_byte_value == original_byte:
                    continue  # Skip original value

                current_block[byte_pos] = new_byte_value

                new_hash = calculate_sha256(current_block)

                if new_hash in correct_hashes:
                    print(f"  Repaired! Position {byte_pos}: {original_byte} -> {new_byte_value}")

                    if block_index + byte_pos < len(data):
                        data[block_index + byte_pos] = new_byte_value

                    repaired = True
                    break

            current_block[byte_pos] = original_byte

        if not repaired:
            print(f"  ERROR: Could not repair block {block_num}")

    return data


def save_and_extract(repaired_data):
    """Saves repaired file and tries to extract it"""
    with open('repaired.zip', 'wb') as f:
        f.write(repaired_data)

    print("\nRepaired file saved as 'repaired.zip'")

    try:
        with zipfile.ZipFile('repaired.zip', 'r') as zip_file:
            print("ZIP contents:")
            for file_info in zip_file.filelist:
                print(f"  - {file_info.filename}")

            zip_file.extractall('extracted')
            print("Files extracted to 'extracted' folder")

            if 'flag.txt' in [f.filename for f in zip_file.filelist]:
                try:
                    with open('extracted/flag.txt', 'r') as f:
                        flag_content = f.read()
                    print(f"\nFLAG CONTENT:")
                    print(flag_content)
                except Exception as e:
                    print(f"Error reading flag: {e}")
                    try:
                        with open('extracted/flag.txt', 'rb') as f:
                            flag_content = f.read()
                        print(f"FLAG CONTENT (hex): {flag_content.hex()}")
                        print(f"FLAG CONTENT (decode attempt): {flag_content.decode('utf-8', errors='ignore')}")
                    except Exception as e2:
                        print(f"Error reading flag as binary: {e2}")

    except zipfile.BadZipFile:
        print("ERROR: Repaired file is not a valid ZIP archive")
    except Exception as e:
        print(f"Error during extraction: {e}")


def main():
    """Main function"""
    print("=== ZIP FILE REPAIR ===")

    data, correct_hashes = read_file_data()

    repaired_data = repair_file(data, correct_hashes)

    save_and_extract(repaired_data)

    print("\n=== COMPLETED ===")


if __name__ == "__main__":
    main()
