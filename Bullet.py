import pygame
import math

class Bullet:

    def __init__(self, x, y, tx, ty, damage, angle_offset=0):

        self.x = x
        self.y = y

        self.damage = damage

        self.radius = 5

        self.speed = 10

        dx = tx - x
        dy = ty - y

        dist = math.hypot(dx, dy)
        if dist == 0:
            dist = 1

        # 角度補正（ショットガン用）
        angle = math.atan2(dy, dx) + math.radians(angle_offset)

        self.vx = math.cos(angle) * self.speed
        self.vy = math.sin(angle) * self.speed

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
