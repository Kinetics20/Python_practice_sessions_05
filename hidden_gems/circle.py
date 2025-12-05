import time
import math


def draw_rgb_xy(r, g, b, x, y, s):
    print(
        f'\x1b[38;2;{r};{g};{b}m\x1b[{y};{x}H{s}\x1b[m',
        end='',
        flush=True
    )


print('\x1b[2j\x1b[3J\x1b[1;1H', end='')
r = 0
g = 0
b = 0
rad = 10
ang = 0.0

while True:
    x = int(math.cos(ang) * rad * 2 + 42)
    y = int(-math.sin(ang) * rad + 12)
    draw_rgb_xy(255, 255, 255, x, y, chr(0x2588))
    ang += 0.1
    rad = 7 + math.sin(ang) * 4
    time.sleep(0.1)
