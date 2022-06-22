import pygame, sys, pymunk 


def create_coin(space, pos):
    body = pymunk.Body( 1, 100, body_type = pymunk.Body.DYNAMIC) 
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_coin(coins):
    for coin in coins:
        pos_x = int(coin.body.position.x)
        pos_y = int(coin.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), 50)


def static_blocker(space, pos):
    body = pymunk.Body(body_type = pymunk.Body.STATIC)
    body.position = pos
    shape = pymunk.Circle(body, 50)
    space.add(body, shape)
    return shape

def draw_static_blocker(blockers):
     for b in blockers:
        pos_x = int(b.body.position.x)
        pos_y = int(b.body.position.y)
        pygame.draw.circle(screen, (0,0,0), (pos_x, pos_y), 50)


pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
space = pymunk.Space()
space.gravity = (10, 300)
coins = []

blockers = []
blockers.append(static_blocker(space, (500, 500)))
blockers.append(static_blocker(space, (250, 400)))
blockers.append(static_blocker(space, (880, 600)))
blockers.append(static_blocker(space, (280, 700)))
blockers.append(static_blocker(space, (580, 300)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            coins.append(create_coin(space, event.pos))

    screen.fill((217, 217, 217)) # background color
    draw_coin(coins)
    draw_static_blocker(blockers)
    space.step(1/50)
    pygame.display.update()
    clock.tick(120)