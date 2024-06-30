from pygame.sprite import Sprite
import pygame
import math
class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        img = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(img, (30,30))
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = direction
        self.speed = 4
        group.add(self)
        
    def update(self):
        
        self.rect.x += self.speed * math.cos(self.direction)
        self.rect.y += -self.speed * math.sin(self.direction)