# Credits:
#  Spaceship art:
#   Stephen Challener (Redshrike), hosted by OpenGameArt.org
#   CC-BY 3.0
#
#  Asteroid art:
#   Cmdr G
#   CC-BY 3.0


import pygame

PLAYER_SPEED = 500

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Asteroid:
    def __init__(self, state, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.frames = state.assets['asteroid']
        self.w = self.frames[0].get_width()
        self.h = self.frames[0].get_height()

    def logic(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        if self.x < 0 - self.w or self.y >= state.h or self.x >= state.w:
            return False

        return True

    def draw(self):
        pass



class GameState:
    def __init__(self, screen, assets):
        self.screen = screen
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.ship_w = assets['ship'].get_width()
        self.ship_h = assets['ship'].get_height()
        self.assets = assets
        self.player = Player(
            (self.w - self.ship_w) // 2,
            self.h - self.ship_h - 40
        )

    def logic(self, dt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return False

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.player.x -= PLAYER_SPEED * dt
            if self.player.x < 0:
                self.player.x = 0

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.player.x += PLAYER_SPEED * dt
            if self.player.x >= self.w - self.ship_w:
                self.player.x = self.w - self.ship_w

        return True

    def draw(self):
        self.screen.blit(self.assets['bg'], (0, 0))
        self.screen.blit(
            self.assets['ship'], (self.player.x, self.player.y)
        )


def init(screen):
    print('Loading...')

    asteroid_anim = []
    for i in range(60):
        fname = f'assets/Asteroid-A-10-{i:02}.png'
        asteroid_anim.append(pygame.image.load(fname))

    assets = {
        'bg': pygame.image.load('assets/bg5.png'),
        'boom': pygame.image.load('assets/exp2_0.png'),
        'asteroid': asteroid_anim,
        'ship': pygame.image.load('assets/shipsheetparts.png'),
    }

    state = GameState(screen, assets)

    return state


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
state = init(screen)
dt = 0

while True:
    if not state.logic(dt):
        break
    state.draw()
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
