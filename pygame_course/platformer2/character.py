from pygame.sprite import Sprite
import pygame
import os
class Character(Sprite):
    def __init__(self, type, x,y, speed, ammo, grenades):
        self.alive = True
        self.health = 100
        self.max_health = 100
        self.speed = speed
        self.ammo = ammo
        self.grenades = grenades
        self.type = type
        self.animations_types = ("Idle", "Run","Jump", "Death")
        self.all_images = {}
        for animation in self.animations_types:
            images = []
            num_of_files = len(os.listdir(f"assets/img/{type}/{animation}"))
            for i in range(num_of_files):
                img = pygame.image.load(f"assets/img/{type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2.5, img_h * 2.5))
                images.append(img)
            self.all_images[animation] = images
            
        self.image = self.all_images["Idle"][0]
        self.rect = self.image.get_rect(topleft = (x,y))
        self.image_number = 0
        self.action = "Idle"
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
            
        
     
