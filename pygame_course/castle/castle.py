from pygame.sprite import Sprite
import pygame
from bullet import Bullet
import math
class Castle(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.health = 1000
        self.max_health = 1000
        img = pygame.image.load("assets/castle/castle_100.png")
        img_w = img.get_width()
        img_h = img.get_height()
        self.image_100 = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
        img = pygame.image.load("assets/castle/castle_50.png")
        self.image_50 = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
        img = pygame.image.load("assets/castle/castle_25.png")
        self.image_25 = pygame.transform.scale(img, (img_w * 0.2, img_h * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sh = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def shoot(self, group):
        if pygame.mouse.get_pressed()[0] and not self.sh:
            self.sh = True
            mouse_pos = pygame.mouse.get_pos()
            y_dist = -(mouse_pos[1] - self.rect.midleft[1])
            x_dist = mouse_pos[0] - self.rect.midleft[0]
            Bullet(self.rect.midleft[0], self.rect.midleft[1], math.atan2(y_dist, x_dist), group)
            
        if not pygame.mouse.get_pressed()[0]:
            self.sh = False
            