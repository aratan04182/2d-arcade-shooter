import pygame
import math

class Boss:

    def __init__(self):

        self.x = 100
        self.y = 100

        self.hp = 500
        self.speed = 1
        self.size = 40

    def update(self, player):

        dx = player.x - self.x
        dy = player.y - self.y

        d = math.sqrt(dx*dx + dy*dy)

        if d != 0:
            self.x += dx / d * self.speed
            self.y += dy / d * self.speed

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (180, 0, 255),
            (int(self.x), int(self.y)),
            self.size
        )
