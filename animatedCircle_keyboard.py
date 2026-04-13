import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Circle with Keyboard")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x, y = WIDTH // 2, HEIGHT // 2
radius = 30
speed = 5

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    # Boundary check
    if x - radius < 0:
        x = radius
    if x + radius > WIDTH:
        x = WIDTH - radius
    if y - radius < 0:
        y = radius
    if y + radius > HEIGHT:
        y = HEIGHT - radius

    pygame.draw.circle(screen, BLUE, (x, y), radius)

    pygame.display.update()
    clock.tick(60)