import pygame
import math

class Bullet:

    def __init__(self, x, y, target_x, target_y, damage):

        self.x = x
        self.y = y

        self.damage = damage

        self.radius = 5

        self.speed = 10

        dx = target_x - x
        dy = target_y - y

        dist = math.hypot(dx, dy)

        if dist == 0:
            dist = 1

        self.vx = dx / dist * self.speed
        self.vy = dy / dist * self.speed

    def update(self):

        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):

        pygame.draw.circle(
            screen,
            (255, 255, 0),
            (int(self.x), int(self.y)),
            self.radius
        )
