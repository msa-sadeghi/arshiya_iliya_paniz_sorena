from pygame.sprite import Sprite
import pygame
from explosion import Explosion
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
        self.timer = 100
        
        
    def update(self, explosion_group):
        dx = self.direction * self.speed
        dy = self.gravity
        self.gravity += 1
        self.timer -= 1
        if self.timer <= 0:
            self.kill()
            Explosion(self.rect.centerx, self.rect.centery, explosion_group)
        
        
        if self.rect.bottom + dy >= 300:
            dy = 300 - self.rect.bottom
            self.gravity = 0
            dx = 0
        self.rect.x += dx
        self.rect.y += dy
        
        