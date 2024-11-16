import pygame

window = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Доганялки")

background = pygame.transform.scale(pygame.image.load("background.png"), (700, 500))

ufo = pygame.transform.scale(pygame.image.load("ufo.png"), (120, 120))
ghost = pygame.transform.scale(pygame.image.load("ghost.png"), (160, 160))

running = True
clock = pygame.time.Clock()
fps = 60

ufo_x = 100
ufo_y = 100

ghost_x = 200
ghost_y = 200

speed = 5

while running:
    window.blit(background, (0, 0))
    window.blit(ufo, (ufo_x, ufo_y))
    window.blit(ghost, (ghost_x, ghost_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and ufo_y > 0:
        ufo_y -= speed
    if keys[pygame.K_s] and ufo_y < 495:
        ufo_y += speed
    if keys[pygame.K_a] and ufo_x > 0:
        ufo_x -= speed
    if keys[pygame.K_d] and ufo_x < 695:
        ufo_x += speed

    if keys[pygame.K_UP] and ghost_y > 5:
        ghost_y -= speed
    if keys[pygame.K_DOWN] and ghost_y < 495:
        ghost_y += speed
    if keys[pygame.K_LEFT] and ghost_x > 5:
        ghost_x -= speed
    if keys[pygame.K_RIGHT] and ghost_x < 695:
        ghost_x += speed
    
    pygame.display.update()
    clock.tick(fps)
pygame.quit()