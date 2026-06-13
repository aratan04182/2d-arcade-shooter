import pygame
import math
import random

class Enemy:

    def __init__(self, x, y, enemy_type="normal"):

        self.x = x
        self.y = y

        self.type = enemy_type

        if enemy_type == "normal":
            self.radius = 15
            self.hp = 20
            self.speed = 2
            self.damage = 10
            self.exp = 20
            self.score = 10
            self.color = (255, 80, 80)

        elif enemy_type == "runner":
            self.radius = 12
            self.hp = 10
            self.speed = 4
            self.damage = 8
            self.exp = 15
            self.score = 15
            self.color = (255, 180, 0)

        elif enemy_type == "tank":
            self.radius = 25
            self.hp = 80
            self.speed = 1
            self.damage = 20
            self.exp = 50
            self.score = 40
            self.color = (150, 50, 255)

        elif enemy_type == "elite":
            self.radius = 30
            self.hp = 200
            self.speed = 1.5
            self.damage = 30
            self.exp = 150
            self.score = 100
            self.color = (255, 0, 255)

    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        distance = math.hypot(dx, dy)

        if distance != 0:

            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed

    def draw(self, screen):

        pygame.draw.circle(

            screen,

            self.color,

            (

                int(self.x),

                int(self.y)

            ),

            self.radius

        )

        # HPバー

        hp_width = self.radius * 2

        max_hp = 200 if self.type == "elite" else (
            80 if self.type == "tank" else (
                20 if self.type == "normal" else 10
            )
        )

        pygame.draw.rect(

            screen,

            (60, 60, 60),

            (

                self.x - self.radius,

                self.y - self.radius - 12,

                hp_width,

                5

            )

        )

        pygame.draw.rect(

            screen,

            (0, 255, 0),

            (

                self.x - self.radius,

                self.y - self.radius - 12,

                hp_width * (self.hp / max_hp),

                5

            )

        )
