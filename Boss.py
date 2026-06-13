import pygame
import math

class Boss:

    def __init__(self):

        self.x = 200
        self.y = 200

        self.radius = 60

        self.max_hp = 1000
        self.hp = self.max_hp

        self.speed = 1.2

        self.damage = 30

        self.score = 1000
        self.exp = 500

        self.color = (200, 0, 255)

    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        dist = math.hypot(dx, dy)

        if dist != 0:

            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self, screen):

        # 本体
        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )

        # 外枠
        pygame.draw.circle(
            screen,
            (255, 255, 255),
            (int(self.x), int(self.y)),
            self.radius,
            3
        )

        # HPバー背景
        bar_w = 200
        bar_h = 10

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (self.x - bar_w // 2, self.y - self.radius - 25, bar_w, bar_h)
        )

        # HPバー本体
        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (
                self.x - bar_w // 2,
                self.y - self.radius - 25,
                bar_w * (self.hp / self.max_hp),
                bar_h
            )
        )
