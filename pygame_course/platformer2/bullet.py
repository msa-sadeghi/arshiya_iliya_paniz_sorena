from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, owner, x,y, group, direction):
        super().__init__()
        self.owner = owner
        self.image = pygame.image.load("assets/img/icons/bullet.png")
        self.rect = self.image.get_rect(tolpeft=(x,y))
        self.direction = direction
        group.add(self)
        
    def update(self):
        self.rect.x += self.direction * 4
        if self.rect.left <= 0 or self.rect.right>= 800:
            self.kill()
        