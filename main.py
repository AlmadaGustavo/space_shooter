import pygame
import sys
import random


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
bullet_sprite = pygame.image.load('assets/bullet.png')
bullet_sprite = pygame.transform.scale(bullet_sprite, (100, 100))
green_ship_sprite = pygame.image.load('assets/green_ship_undefended.png')
green_ship_sprite = pygame.transform.scale(green_ship_sprite, (100, 100))
green_shield_ship_sprite = pygame.image.load('assets/green_ship.png')
green_shield_ship_sprite = pygame.transform.scale(green_shield_ship_sprite, (100, 100))
yellow_ship_one = pygame.image.load('assets/yellow_ship.png')
yellow_ship_one = pygame.transform.scale(yellow_ship_one, (100, 100))
x_sprite = 275
y_sprite = 450



# Bullet stats
bullet_speed = 15
bullets = []
y_bullet = y_sprite - 25

# Shooting control
is_shooting = False


# Colors
GREY = (212, 218, 212)
PURPLE = (153, 51, 153)

# Ship
yellow_ship_speed = 5
yellow_ships = []

create_yellow_ship_timer = 0
create_yellow_ship_interval = 4000

green_ship_speed = 5
green_ships = []

create_green_ship_timer = 0
create_green_ship_interval = 6000

green_shield_ship_speed = 5
green_shield_ships = []

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_shooting:
                is_shooting = True
                bullet = {'x': x_sprite + 25, 'y': y_bullet, 'speed': bullet_speed}  # Create bullet
                bullets.append(bullet)
        else:
            is_shooting = False

        keys = pygame.key.get_pressed()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x_sprite += 15

    if keys[pygame.K_LEFT]:
        x_sprite -= 15

    # Bullet update
    for bullet in bullets:
        bullet['y'] -= bullet['speed']

    # Delete bullet
    new_bullets = []
    for bullet in bullets:
        if bullet['y'] > 70:
            new_bullets.append(bullet)
    bullets = new_bullets

    collisions_to_remove = []

    create_yellow_ship_timer += clock
    if create_yellow_ship_timer >= create_yellow_ship_interval:
        create_yellow_ship_timer = 0
        yellow_x = random.randint(0, WIDTH - 50)
        yellow_ships.append({'x': yellow_x, 'y': 0, 'speed': yellow_ship_speed})

    for yellow_ship in yellow_ships.copy():
        yellow_ship['y'] += yellow_ship['speed']
        screen.blit(yellow_ship_one, (yellow_ship['x'], yellow_ship['y']))

        # Collide bottom
        if yellow_ship['y'] > HEIGHT - 100:
            yellow_ships.remove(yellow_ship)

        player_rect = pygame.Rect(x_sprite, y_sprite, 150, 150)
        yellow_ship_rect = pygame.Rect(yellow_ship['x'], yellow_ship['y'], 100, 100)

        if player_rect.colliderect(yellow_ship_rect):
            yellow_ships.remove(yellow_ship)
            life -= 1

        # Collide player bullet
        for bullet in bullets.copy():
            bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 50, 50)
            yellow_ship_rect = pygame.Rect(yellow_ship['x'], yellow_ship['y'], 75, 75)

            if bullet_rect.colliderect(yellow_ship_rect):
                collisions_to_remove.append((yellow_ship, bullet))
                score += 1

    for yellow_ship, bullet in collisions_to_remove:
        yellow_ships.remove(yellow_ship)
        bullets.remove(bullet)

    create_green_ship_timer += clock
    if create_green_ship_timer >= create_green_ship_interval:
        create_green_ship_timer = 0
        green_x = random.randint(0, WIDTH - 100)
        green_ships.append({'x': green_x, 'y': 0, 'speed': green_ship_speed, 'shield_health': 5, 'has_shield': True})

    for green_ship in green_ships.copy():
        green_ship['y'] += green_ship['speed']

        if green_ship['has_shield']:
            screen.blit(green_shield_ship_sprite, (green_ship['x'], green_ship['y']))
        else:
            screen.blit(green_ship_sprite, (green_ship['x'], green_ship['y']))

        # Verificar colisão com o chão
        if green_ship['y'] > HEIGHT - 100:
            green_ships.remove(green_ship)

        # Verificar colisão com os tiros do jogador
        for bullet in bullets.copy():
            bullet_rect = pygame.Rect(bullet['x'], bullet['y'], 50, 50)
            green_ship_rect = pygame.Rect(green_ship['x'], green_ship['y'], 100, 100)

            if bullet_rect.colliderect(green_ship_rect):
                collisions_to_remove.append((green_ship, bullet))
                if green_ship['has_shield']:
                    green_ship['shield_health'] -= 1
                    if green_ship['shield_health'] <= 0:
                        green_ship['has_shield'] = False
                else:
                    green_ships.remove(green_ship)
                    score += 3

                bullets.remove(bullet)

                # Hud
    pygame.draw.line(screen, GREY, [0, 70], [0, HEIGHT], 10)
    pygame.draw.line(screen, GREY, [WIDTH, 70], [WIDTH, HEIGHT], 10)

    pygame.draw.line(screen, PURPLE, [0, 0], [0, 69], 10)
    pygame.draw.line(screen, PURPLE, [WIDTH, 0], [WIDTH, 69], 10)

    pygame.draw.line(screen, PURPLE, [0, 0], [WIDTH, 0], 10)
    pygame.draw.line(screen, PURPLE, [0, 69], [WIDTH, 69], 5)
    pygame.draw.line(screen, PURPLE, [(WIDTH/2), 0], [(WIDTH/2), 69], 5)

    for bullet in bullets:
        screen.blit(bullet_sprite, (bullet['x'], bullet['y']))

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
