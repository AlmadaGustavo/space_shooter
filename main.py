import pygame
import sys


pygame.init()

# Screen
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Sprites
player = pygame.image.load('assets/player (1).png')
player = pygame.transform.scale(player, (150, 150))
heart = pygame.image.load('assets/heart.png')
heart = pygame.transform.scale(heart, (100, 50))
x_sprite = 275
y_sprite = 450

# Colors
GREY = (212, 218, 212)
PURPLE = (153, 51, 153)

score = 0
life = 3

while True:
    screen.blit(player, (x_sprite, y_sprite), (0, 0, WIDTH, HEIGHT))
    pygame.display.flip()
    clock = pygame.time.Clock().tick(10)
    screen.fill(0)

    # Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_sprite += 15

    if keys[pygame.K_LEFT]:
        x_sprite -= 15

    # Hud
    pygame.draw.line(screen, GREY, [0, 70], [0, HEIGHT], 10)
    pygame.draw.line(screen, GREY, [WIDTH, 70], [WIDTH, HEIGHT], 10)

    pygame.draw.line(screen, PURPLE, [0, 0], [0, 69], 10)
    pygame.draw.line(screen, PURPLE, [WIDTH, 0], [WIDTH, 69], 10)

    pygame.draw.line(screen, PURPLE, [0, 0], [WIDTH, 0], 10)
    pygame.draw.line(screen, PURPLE, [0, 69], [WIDTH, 69], 5)
    pygame.draw.line(screen, PURPLE, [(WIDTH/2), 0], [(WIDTH/2), 69], 5)

    score_font = pygame.font.Font('assets/PressStart2P (1).ttf', 20)
    score_text = score_font.render(f'Score: {score}', True, GREY)
    score_text_rect = score_text.get_rect()
    screen.blit(score_text, (350, 30))

    life_font = pygame.font.Font('assets/PressStart2P (1).ttf', 20)
    life_text = life_font.render('Life:', True, GREY)
    screen.blit(life_text, (20, 30))

    if life == 3:
        screen.blit(heart, (100, 0))
        screen.blit(heart, (150, 0))
        screen.blit(heart, (200, 0))
    elif life == 2:
        screen.blit(heart, (100, 0))
        screen.blit(heart, (150, 0))
    else:
        screen.blit(heart, (100, 0))
