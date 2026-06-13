import pygame
import math

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 20
        self.speed = 2
        self.size = 15

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
            (255, 80, 80),
            (int(self.x), int(self.y)),
            self.size
        )
