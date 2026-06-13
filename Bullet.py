import pygame
import math

class Bullet:

    def __init__(self, x, y, tx, ty):

        self.x = x
        self.y = y

        dx = tx - x
        dy = ty - y

        d = math.sqrt(dx*dx + dy*dy)

        self.vx = dx / d * 8
        self.vy = dy / d * 8

        self.size = 5

    def update(self):

        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.x), int(self.y)),
            self.size
        )
