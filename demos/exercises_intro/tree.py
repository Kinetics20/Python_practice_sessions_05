import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def festive_tree(height):
    decorations = ['🎄', '⭐', '❄️', '🎁', '🎅', '🦌', '🍬', '🔔']
    tree = []
    for i in range(height):
        width = 2 * i + 1
        row = ''.join(random.choice(decorations) for _ in range(width))
        line = ' ' * (height - i - 1) + row
        tree.append(line)
    tree.append(' ' * (height - 1) + '🪵')
    return tree


height = 12
frames = 30
delay = 0.3

for _ in range(frames):
    clear()
    tree = festive_tree(height)
    print('\n'.join(tree))
    time.sleep(delay)
