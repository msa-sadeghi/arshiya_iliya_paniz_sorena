from pygame.sprite import Sprite
import pygame
class Enemy(Sprite):
    def __init__(self, type, x,y, group, speed):
        super().__init__()
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.type = type
        self.speed = speed
        group.add(self)
        self.all_images = []
        self.animation_types = ("walk", "attack", "death")
        for anim in self.animation_types:
            temp = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{self.type}/{anim}/{i}.png")
                img = pygame.transform.scale(img, (50, 70))
                temp.append(img)
            self.all_images.append(temp)
        self.image = self.all_images[0][0]
        self.action = 0
        self.image_number = 0
        self.rect = self.image.get_rect(topleft = (x,y))
        self.time = 0
    def update(self):
        self.rect.x += self.speed
        self.animation()
        
    def animation(self):
        self.image = self.all_images[self.action][self.image_number]
        if pygame.time.get_ticks() - self.time > 100:
            self.image_number += 1
            self.time = pygame.time.get_ticks()
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
        
            
        
        
              
        
    
        