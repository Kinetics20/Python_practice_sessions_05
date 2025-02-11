from PIL import Image, ImageDraw
import random


width, height = 1584, 396
square_size = 12
green_palette = ["#9be9a8", "#40c463", "#30a14e", "#216e39"]

ocean_top = (26, 110, 255)
ocean_bottom = (0, 82, 158)

whale_grid = [
    "     XXXXX             ",
    "   XXXXXXXXXXX        ",
    "  XXXXXXXXXXXXXXX     ",
    " XXXXXXXXXXXXXXXXX    ",
    "XXXXXXXXXXXXXXXXXXX   ",
    "XXXXXXXXXXXXXXXXXXXX  ",
    "XXXXXXXXXXXXXXXXXXXX  ",
    "XXXXXXXXXXXXXXXXXXX   ",
    " XXXXXXXXXXXXXXXXX    ",
    "  XXXXXXXXXXXXXXX     ",
    "   XXXXXXXXXXX        ",
    "     XXXXXXX          ",
]

whale_start_x = 15
whale_start_y = 8


image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)


for y in range(0, height, square_size):
    for x in range(0, width, square_size):
        grid_x = x // square_size
        grid_y = y // square_size


        is_whale = False
        if whale_start_y <= grid_y and grid_y < whale_start_y + len(whale_grid):
            whale_row = grid_y - whale_start_y
            whale_col = grid_x - whale_start_x
            if 0 <= whale_col < len(whale_grid[whale_row]) and whale_grid[whale_row][whale_col] == "X":
                is_whale = True


        if is_whale:
            color = random.choice(green_palette)
        else:
            blend = y / height
            r = max(0, min(255, int(ocean_top[0] + (ocean_bottom[0] - ocean_top[0]) * blend)))
            g = max(0, min(255, int(ocean_top[1] + (ocean_bottom[1] - ocean_top[1]) * blend)))
            b = max(0, min(255, int(ocean_top[2] + (ocean_bottom[2] - ocean_top[2]) * blend)))
            color = (r, g, b)


        draw.rectangle([x, y, x + square_size, y + square_size], fill=color)


image.save("linkedin_banner.png")
