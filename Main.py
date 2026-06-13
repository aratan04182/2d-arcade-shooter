import pygame
import random
import math

from player import Player
from enemy import Enemy
from bullet import Bullet
from boss import Boss

pygame.init()

WIDTH = 1280
HEIGHT = 720
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Survival Shooter")

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

while running:

    dt = clock.tick(FPS)

    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.update(keys, WIDTH, HEIGHT)

    # 敵スポーン

    spawn_timer += dt

    if spawn_timer >= 700:

        spawn_timer = 0

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

        enemy_type = random.choice(
            [
                "normal",
                "runner",
                "tank"
            ]
        )

        enemies.append(
            Enemy(
                x,
                y,
                enemy_type
            )
        )

    # ボス出現

    if not boss_spawned:

        if current_time - start_time > 30000:

            boss = Boss()

            boss_spawned = True

    # 自動射撃

    shoot_timer += dt

    if shoot_timer >= player.fire_rate:

        shoot_timer = 0

        targets = []

        for e in enemies:

            targets.append(e)

        if boss is not None:

            targets.append(boss)

        if len(targets) > 0:

            nearest = min(

                targets,

                key=lambda obj:

                math.hypot(

                    obj.x - player.x,

                    obj.y - player.y

                )

            )

            bullets.append(

                Bullet(

                    player.x,

                    player.y,

                    nearest.x,

                    nearest.y,

                    player.damage

                )

            )

    # 敵更新

    for enemy in enemies:

        enemy.update(player)

    if boss is not None:

        boss.update(player)
    # -------------------------
    # 弾の更新
    # -------------------------

    for bullet in bullets[:]:

        bullet.update()

        # 画面外に出たら削除
        if (
            bullet.x < -100
            or bullet.x > WIDTH + 100
            or bullet.y < -100
            or bullet.y > HEIGHT + 100
        ):

            bullets.remove(bullet)
            continue

        # 敵との当たり判定

        hit = False

        for enemy in enemies[:]:

            dx = bullet.x - enemy.x
            dy = bullet.y - enemy.y

            distance = math.hypot(dx, dy)

            if distance <= bullet.radius + enemy.radius:

                enemy.hp -= bullet.damage

                if bullet in bullets:
                    bullets.remove(bullet)

                hit = True

                if enemy.hp <= 0:

                    score += enemy.score

                    player.add_exp(enemy.exp)

                    enemies.remove(enemy)

                break

        if hit:
            continue

        # ボスとの当たり判定

        if boss is not None:

            dx = bullet.x - boss.x
            dy = bullet.y - boss.y

            distance = math.hypot(dx, dy)

            if distance <= bullet.radius + boss.radius:

                boss.hp -= bullet.damage

                if bullet in bullets:
                    bullets.remove(bullet)

                if boss.hp <= 0:

                    score += 1000

                    boss = None

    # -------------------------
    # プレイヤーへのダメージ
    # -------------------------

    for enemy in enemies[:]:

        dx = enemy.x - player.x
        dy = enemy.y - player.y

        if math.hypot(dx, dy) <= enemy.radius + player.radius:

            player.take_damage(enemy.damage)

            enemies.remove(enemy)

    if boss is not None:

        dx = boss.x - player.x
        dy = boss.y - player.y

        if math.hypot(dx, dy) <= boss.radius + player.radius:

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

    if boss is not None:
        boss.draw(screen)

    # UI

    hp_text = font.render(
        f"HP : {player.hp}/{player.max_hp}",
        True,
        (255, 255, 255)
    )

    lv_text = font.render(
        f"LEVEL : {player.level}",
        True,
        (100, 255, 100)
    )

    score_text = font.render(
        f"SCORE : {score}",
        True,
        (255, 255, 0)
    )

    exp_text = font.render(
        f"EXP : {player.exp}/{player.next_exp}",
        True,
        (100, 200, 255)
    )

    screen.blit(hp_text, (20, 20))
    screen.blit(lv_text, (20, 60))
    screen.blit(score_text, (20, 100))
    screen.blit(exp_text, (20, 140))

    # ボスHP

    if boss is not None:

        pygame.draw.rect(
            screen,
            (80, 80, 80),
            (250, 20, 780, 20)
        )

        pygame.draw.rect(
            screen,
            (255, 50, 100),
            (
                250,
                20,
                780 * (boss.hp / boss.max_hp),
                20
            )
        )

    # Game Over

    if player.hp <= 0:

        text = big_font.render(
            "GAME OVER",
            True,
            (255, 60, 60)
        )

        screen.blit(
            text,
            (
                WIDTH // 2 - text.get_width() // 2,
                HEIGHT // 2
            )
        )

    pygame.display.flip()

pygame.quit()
