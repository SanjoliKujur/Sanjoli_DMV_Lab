
import pygame
import sys


width = int(input("Enter window width: "))
height = int(input("Enter window height: "))
speed = int(input("Enter circle speed: "))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")


WHITE = (255, 255, 255)
RED = (255, 0, 0)

x, y = width // 2, height // 2
radius = 30

dx, dy = speed, speed

clock = pygame.time.Clock()


while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    x += dx
    y += dy

    
    if x - radius <= 0 or x + radius >= width:
        dx = -dx
    if y - radius <= 0 or y + radius >= height:
        dy = -dy

    
    pygame.draw.circle(screen, RED, (x, y), radius)

    pygame.display.update()
    clock.tick(60)
