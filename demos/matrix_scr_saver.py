import random
W, H = 80, 30
DECAY = 10

buf = bytearray(W * H)
droplets: list = []

def iterate():
    global droplets

    for y in range(H):
        for x in range(W):
            v = buf[x + y * W]
            v -= DECAY
            if v < 0:
                v = 0
            buf[x + y * W] = v
    while len(droplets) < int(W * 1.5):
        droplet = [
            random.randint(0, W-1),
            0,
            1 + random.random() * 1.5,
        ]
        droplets.append(droplet)

    new_droplets = []
    for droplet in droplets:
        x, y, speed = droplet
        next_y = y + speed

        skip_droplet = False
        for i in range(int(y), int(next_y) + 1):
            if i >= H:
                skip_droplet = True
                break
            buf[x + i * W] = 255

        if not skip_droplet:
            droplet[1] = next_y
            new_droplets.append(droplet)



    droplets = new_droplets
CHARSET = '0123456789'

def draw():
    o = ['\x1b[2J\x1b[1;1H']

    for y in range(H):
        for x in range(W):
            v = buf[x + y * W]

            if v >= 128:
                r = (v - 128) * 2
                g = 255
                b = (v - 128) * 2
            else:
                r = 0
                g = v * 2
                b = 0

            ch = CHARSET[(x * 15267 + y * 91263) % len(CHARSET)]
            o.append(f'\x1b[38;2;{r};{g};{b}m{ch}\x1b[m')
