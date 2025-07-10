block_size = 8192
block_count = 10

shuffled_to_original = {
    0: 9,
    3: 4,
    1: 2,
    7: 7,
    4: 5,
    2: 1,
    8: 3,
    5: 0,
    9: 6,
    6: 9,
}

with open("shuffled.png.bin", "rb") as f:
    blocks = [f.read(block_size) for _ in range(block_count)]

ordered_blocks = [b"" for _ in range(block_count)]

for shuffled_index, original_index in shuffled_to_original.items():
    ordered_blocks[original_index] = blocks[shuffled_index]

with open("unshuffled.png", "wb") as out:
    for block in ordered_blocks:
        out.write(block)

print("✅ File 'unshuffled.png' successfully created.")
