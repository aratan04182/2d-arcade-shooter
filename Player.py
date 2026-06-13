import pygame

class Player:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.radius = 20

        self.speed = 5

        self.hp = 100
        self.max_hp = 100

        self.level = 1
        self.exp = 0
        self.next_exp = 100

        self.damage = 10
        self.fire_rate = 300

    def update(self, keys, width, height):

        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed

        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed

        # 画面外に出ないようにする
        if self.x < self.radius:
            self.x = self.radius

        if self.x > width - self.radius:
            self.x = width - self.radius

        if self.y < self.radius:
            self.y = self.radius

        if self.y > height - self.radius:
            self.y = height - self.radius

    def add_exp(self, amount):

        self.exp += amount

        if self.exp >= self.next_exp:

            self.exp -= self.next_exp

            self.level += 1

            # レベルアップ時の強化
            self.max_hp += 10
            self.hp = self.max_hp

            self.damage += 2

            if self.fire_rate > 100:
                self.fire_rate -= 20

            self.next_exp += 50

    def take_damage(self, damage):

        self.hp -= damage

        if self.hp < 0:
            self.hp = 0

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (50, 200, 255),
            (int(self.x), int(self.y)),
            self.radius
        )

        # プレイヤーの向きが分かるマーク
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y - 8)),
            4
        )
