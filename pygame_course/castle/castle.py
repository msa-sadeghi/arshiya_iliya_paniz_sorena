from pygame.sprite import Sprite
import pygame
class Castle(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 1000
        self.max_health = 1000
        self.image_100 = pygame.image.load("assets/castle/castle_100.png")
        self.image_50 = pygame.image.load("assets/castle/castle_50.png")
        self.image_25 = pygame.image.load("assets/castle/castle_25.png")
        self.image = self.image_100
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y