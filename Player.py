import pygame

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 5
        self.hp = 100
        self.size = 20

    def update(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            (0, 200, 255),
            (int(self.x), int(self.y)),
            self.size
        )
