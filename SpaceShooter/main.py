import pygame
import sys

pygame.init()

WIDTH = 700
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
player = pygame.image.load("player (1).png")
x_sprite = 275
y_sprite = 450

while True:
    screen.blit(player, (x_sprite, y_sprite), (0, 0, WIDTH, HEIGHT))
    pygame.display.flip()
    clock = pygame.time.Clock().tick(10)
    screen.fill(0)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_sprite += 15
      
    if keys[pygame.K_LEFT]:
        x_sprite -= 15
