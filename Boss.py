import pygame
import math

class Boss:

    def __init__(self):

        self.x = 100
        self.y = 100

        self.radius = 50

        self.max_hp = 1000
        self.hp = self.max_hp

        self.speed = 1.2

        self.damage = 30

        self.color = (180, 0, 255)

        self.score = 1000
        self.exp = 500

    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        distance = math.hypot(dx, dy)

        if distance != 0:

            self.x += dx / distance * self.speed
            self.y += dy / distance * self.speed

    def draw(self, screen):

        # 本体
        pygame.draw.circle(

            screen,

            self.color,

            (

                int(self.x),

                int(self.y)

            ),

            self.radius

        )

        # 外枠
        pygame.draw.circle(

            screen,

            (255, 255, 255),

            (

                int(self.x),

                int(self.y)

            ),

            self.radius,

            3

        )

        # HPバー

        bar_width = 120
        bar_height = 10

        pygame.draw.rect(

            screen,

            (80, 80, 80),

            (

                self.x - bar_width // 2,

                self.y - self.radius - 20,

                bar_width,

                bar_height

            )

        )

        pygame.draw.rect(

            screen,

            (255, 0, 0),

            (

                self.x - bar_width // 2,

                self.y - self.radius - 20,

                bar_width * (self.hp / self.max_hp),

                bar_height

            )

        )
