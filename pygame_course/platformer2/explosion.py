from pygame.sprite import Sprite
import pygame
class Explosion(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.images = []
        for i in range(1,6):
            img = pygame.image.load(f"assets/img/explosion/exp{i}.png")
            self.images.append(img)
        self.image_number = 0
        self.image = self.images[self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.last_image_change_time = 0
           
    def update(self):
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.image_number]
        
        
        