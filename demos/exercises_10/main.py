import pygame


def logic():
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            return False

    return True


def draw(screen):
    screen.fill((0, 255, 0))


pygame.init()
screen = pygame.display.set_mode((800, 600))

while True:
    if not logic():
        break
    draw(screen)
    pygame.display.flip()

pygame.quit()
