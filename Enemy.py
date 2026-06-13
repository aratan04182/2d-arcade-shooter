import pygame
import math
import random

class Enemy:

    def __init__(self, x, y, enemy_type="normal"):

        self.x = x
        self.y = y

        self.type = enemy_type

        # ---------------------
        # タイプ別ステータス
        # ---------------------

        if enemy_type == "normal":

            self.radius = 15
            self.hp = 20
            self.speed = 2
            self.damage = 10
            self.score = 10
            self.exp = 20
            self.color = (255, 80, 80)

        elif enemy_type == "runner":

            self.radius = 12
            self.hp = 12
            self.speed = 4
            self.damage = 8
            self.score = 15
            self.exp = 15
            self.color = (255, 180, 0)

        elif enemy_type == "tank":

            self.radius = 25
            self.hp = 80
            self.speed = 1
            self.damage = 20
            self.score = 40
            self.exp = 50
            self.color = (150, 60, 255)

        else:

            self.radius = 15
            self.hp = 20
            self.speed = 2
            self.damage = 10
            self.score = 10
            self.exp = 20
            self.color = (255, 255, 255)

    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        dist = math.hypot(dx, dy)

        if dist != 0:

            self.x += dx / dist * self.speed
            self.y += dy / dist * self.speed

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )

        # HPバー
        bar_width = self.radius * 2
        hp_ratio = self.hp / 80  # 最大想定

        pygame.draw.rect(
            screen,
            (60, 60, 60),
            (
                self.x - self.radius,
                self.y - self.radius - 10,
                bar_width,
                5
            )
        )

        pygame.draw.rect(
            screen,
            (0, 255, 0),
            (
                self.x - self.radius,
                self.y - self.radius - 10,
                bar_width * hp_ratio,
                5
            )
        )
