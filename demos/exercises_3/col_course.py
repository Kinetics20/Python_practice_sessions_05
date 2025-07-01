import zlib
import random
import string

def find_collision():
    crc_digits = {}
    crc_letters = {}

    digits = string.digits
    letters = string.ascii_lowercase

    while True:
        len_digits = random.randint(4, 8)
        len_letters = random.randint(4, 8)

        pwd_digits = ''.join(random.choices(digits, k=len_digits))
        pwd_letters = ''.join(random.choices(letters, k=len_letters))

        crc_d = zlib.crc32(pwd_digits.encode())
        crc_l = zlib.crc32(pwd_letters.encode())

        if crc_d not in crc_digits:
            crc_digits[crc_d] = pwd_digits

        if crc_l not in crc_letters:
            crc_letters[crc_l] = pwd_letters

        if crc_d in crc_letters:
            if crc_digits[crc_d] != crc_letters[crc_d]:
                print("Found collisions:")
                print(f"Digits password: {crc_digits[crc_d]} (CRC32: {crc_d})")
                print(f"Letters password: {crc_letters[crc_d]} (CRC32: {crc_d})")
                return crc_digits[crc_d], crc_letters[crc_d]

        if crc_l in crc_digits:
            if crc_letters[crc_l] != crc_digits[crc_l]:
                print("Found collisions:")
                print(f"Digits password: {crc_digits[crc_l]} (CRC32: {crc_l})")
                print(f"Letters password: {crc_letters[crc_l]} (CRC32: {crc_l})")
                return crc_digits[crc_l], crc_letters[crc_l]


collision_digits, collision_letters = find_collision()
