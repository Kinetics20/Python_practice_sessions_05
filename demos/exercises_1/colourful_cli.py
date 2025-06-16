def print_ansi_colors():
    print("Primary colours ANSI (0–15):\n")

    for color_code in range(16):

        color_text = f"\033[38;5;{color_code}m"

        color_bg = f"\033[48;5;{color_code}m"

        reset = "\033[0m"

        print(f"{color_bg}{color_text} Kod {color_code:<2} {reset}", end="  ")

        if (color_code + 1) % 8 == 0:
            print()


if __name__ == "__main__":
    print_ansi_colors()
