import pygame
import random
import math

from player import Player
from enemy import Enemy
from bullet import Bullet

pygame.init()

WIDTH = 1280
HEIGHT = 720

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Shooter")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)

player = Player(WIDTH // 2, HEIGHT // 2)

enemies = []
bullets = []

spawn_timer = 0
shoot_timer = 0

score = 0

running = True

while running:

    dt = clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.update(keys, WIDTH, HEIGHT)

    spawn_timer += dt

    if spawn_timer > 800:

        spawn_timer = 0

        side = random.randint(0, 3)

        if side == 0:
            x = random.randint(0, WIDTH)
            y = -30

        elif side == 1:
            x = random.randint(0, WIDTH)
            y = HEIGHT + 30

        elif side == 2:
            x = -30
            y = random.randint(0, HEIGHT)

        else:
            x = WIDTH + 30
            y = random.randint(0, HEIGHT)

        enemies.append(Enemy(x, y))

    shoot_timer += dt

    if shoot_timer > 300:

        shoot_timer = 0

        if len(enemies) > 0:

            nearest = min(
                enemies,
                key=lambda e: math.hypot(
                    e.x - player.x,
                    e.y - player.y
                )
            )

            bullets.append(
                Bullet(
                    player.x,
                    player.y,
                    nearest.x,
                    nearest.y
                )
            )

    for enemy in enemies:
        enemy.update(player)

    for bullet in bullets:
        bullet.update()

    for bullet in bullets[:]:

        if bullet.x < -50 or bullet.x > WIDTH + 50:
            bullets.remove(bullet)
            continue

        if bullet.y < -50 or bullet.y > HEIGHT + 50:
            bullets.remove(bullet)
            continue

        for enemy in enemies[:]:

            dx = bullet.x - enemy.x
            dy = bullet.y - enemy.y

            if math.hypot(dx, dy) < bullet.radius + enemy.radius:

                enemy.hp -= 10

                if bullet in bullets:
                    bullets.remove(bullet)

                if enemy.hp <= 0:

                    if enemy in enemies:
                        enemies.remove(enemy)

                    score += 10

                break

    screen.fill((20, 20, 30))

    player.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    hp_text = font.render(
        f"HP : {player.hp}",
        True,
        (255, 255, 255)
    )

    score_text = font.render(
        f"Score : {score}",
        True,
        (255, 255, 0)
    )

    screen.blit(hp_text, (20, 20))
    screen.blit(score_text, (20, 60))

    pygame.display.flip()

pygame.quit()
