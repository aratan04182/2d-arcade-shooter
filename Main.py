import pygame
import random
import math

from player import Player
from enemy import Enemy
from bullet import Bullet
from boss import Boss

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Shooter v1.0")

clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 72)

player = Player(WIDTH // 2, HEIGHT // 2)

enemies = []
bullets = []

boss = None
boss_spawned = False

score = 0

spawn_timer = 0
shoot_timer = 0

start_time = pygame.time.get_ticks()

running = True


def spawn_enemy():
    side = random.randint(0, 3)

    if side == 0:
        x = random.randint(0, WIDTH)
        y = -40
    elif side == 1:
        x = random.randint(0, WIDTH)
        y = HEIGHT + 40
    elif side == 2:
        x = -40
        y = random.randint(0, HEIGHT)
    else:
        x = WIDTH + 40
        y = random.randint(0, HEIGHT)

    enemy_type = random.choice(["normal", "runner", "tank"])

    enemies.append(Enemy(x, y, enemy_type))


while running:

    dt = clock.tick(60)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys, WIDTH, HEIGHT)

    # -------------------------
    # 敵スポーン
    # -------------------------
    spawn_timer += dt
    if spawn_timer > 700:
        spawn_timer = 0
        spawn_enemy()

    # -------------------------
    # ボス出現
    # -------------------------
    if not boss_spawned and current_time - start_time > 30000:
        boss = Boss()
        boss_spawned = True

    # -------------------------
    # 自動射撃
    # -------------------------
    # 自動射撃（強化版）
shoot_timer += dt

if shoot_timer > player.fire_rate:

    shoot_timer = 0

    targets = enemies[:]

    if boss:
        targets.append(boss)

    if targets:

        nearest = min(
            targets,
            key=lambda o: ((o.x - player.x)**2 + (o.y - player.y)**2)
        )

        # 武器別射撃
        if player.weapon == 0:
            # ピストル
            bullets.append(
                Bullet(player.x, player.y, nearest.x, nearest.y, player.damage)
            )

        elif player.weapon == 1:
            # ショットガン（3発）
            for a in [-10, 0, 10]:
                bullets.append(
                    Bullet(player.x, player.y, nearest.x, nearest.y, player.damage, a)
                )

        elif player.weapon == 2:
            # マシンガン（連射強化）
            for _ in range(2):
                bullets.append(
                    Bullet(player.x, player.y, nearest.x, nearest.y, player.damage)
                )
    # -------------------------
    # 更新
    # -------------------------
    for enemy in enemies:
        enemy.update(player)

    if boss:
        boss.update(player)

    for bullet in bullets:
        bullet.update()

    # -------------------------
    # 弾の処理
    # -------------------------
    for bullet in bullets[:]:

        if bullet.x < -100 or bullet.x > WIDTH + 100 or bullet.y < -100 or bullet.y > HEIGHT + 100:
            bullets.remove(bullet)
            continue

        # 敵ヒット
        for enemy in enemies[:]:

            if math.hypot(bullet.x - enemy.x, bullet.y - enemy.y) < enemy.radius + bullet.radius:

                enemy.hp -= bullet.damage

                bullets.remove(bullet)

                if enemy.hp <= 0:
                    score += enemy.score
                    player.add_exp(enemy.exp)
                    enemies.remove(enemy)

                break

        # ボスヒット
        if boss and bullet in bullets:

            if math.hypot(bullet.x - boss.x, bullet.y - boss.y) < boss.radius + bullet.radius:

                boss.hp -= bullet.damage
                bullets.remove(bullet)

                if boss.hp <= 0:
                    score += 1000
                    boss = None

    # -------------------------
    # 接触ダメージ
    # -------------------------
    for enemy in enemies[:]:

        if math.hypot(enemy.x - player.x, enemy.y - player.y) < enemy.radius + player.radius:
            player.take_damage(enemy.damage)
            enemies.remove(enemy)

    if boss:

        if math.hypot(boss.x - player.x, boss.y - player.y) < boss.radius + player.radius:
            player.take_damage(1)

    # -------------------------
    # 描画
    # -------------------------
    screen.fill((25, 25, 35))

    player.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    for bullet in bullets:
        bullet.draw(screen)

    if boss:
        boss.draw(screen)

    # -------------------------
    # UI
    # -------------------------
    screen.blit(font.render(f"HP: {player.hp}/{player.max_hp}", True, (255, 255, 255)), (20, 20))
    screen.blit(font.render(f"LV: {player.level}", True, (100, 255, 100)), (20, 60))
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 0)), (20, 100))
    screen.blit(font.render(f"EXP: {player.exp}/{player.next_exp}", True, (100, 200, 255)), (20, 140))

    # boss HP
    if boss:
        pygame.draw.rect(screen, (80, 80, 80), (300, 20, 600, 10))
        pygame.draw.rect(screen, (255, 0, 0), (300, 20, 600 * (boss.hp / boss.max_hp), 10))

    # GAME OVER
    if player.hp <= 0:
        text = big_font.render("GAME OVER", True, (255, 50, 50))
        screen.blit(text, (WIDTH//2 - text.get_width()//2, HEIGHT//2))

    pygame.display.flip()

pygame.quit()
import random

if random.random() < 0.3:
    # アイテムドロップ（簡易）
    player.hp = min(player.max_hp, player.hp + 10)
