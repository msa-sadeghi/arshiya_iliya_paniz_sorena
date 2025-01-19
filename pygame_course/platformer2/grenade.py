from pygame.sprite import Sprite
import pygame
class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/img/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel_y = -15
        self.speed = 4
        self.direction = direction
        group.add(self)
        self.gravity = -13
        
        
    def update(self):
        dx = self.direction * self.speed
        dy = self.gravity
        self.gravity += 1
        self.rect.x += dx
        self.rect.y += dy
        
        