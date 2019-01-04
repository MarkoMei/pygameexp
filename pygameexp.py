import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My First Pygame App")

x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keysPressed = pygame.key.get_pressed()

    if keysPressed[pygame.K_LEFT]:
        x -= vel
    if keysPressed[pygame.K_RIGHT]:
        x += vel
    if keysPressed[pygame.K_UP]:
        y -= vel
    if keysPressed[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()