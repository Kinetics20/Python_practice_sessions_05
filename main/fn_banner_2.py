from PIL import Image, ImageDraw
import random


width, height = 1584, 396
square_size = 48
colors = ["#ebedf0", "#9be9a8", "#40c463", "#30a14e", "#216e39"]

image = Image.new("RGB", (width, height), "#1A6EFF")
draw = ImageDraw.Draw(image)


for x in range(0, width, square_size):
    for y in range(0, height, square_size):
        color = random.choice(colors)
        draw.rectangle([x, y, x + square_size, y + square_size], fill=color)

image.save("banner.png")
