from pygame.sprite import Sprite
import pygame
import os
from bullet import Bullet
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
        self.last_image_change_time = 0
        self.direction = 1
        self.flip = False
        self.yvel = 0
        self.in_air = False
        self.last_bullet_shoot_time = 0
    def draw(self, screen):
        img = self.all_images[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)
        self.animation()
        
            
    def animation(self):
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
            self.last_image_change_time = pygame.time.get_ticks()
        
    def change_action(self, new_action)   :
        if self.action != new_action:
            self.action = new_action
            self.image_number = 0
            self.last_image_change_time = pygame.time.get_ticks()
            
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_left:
            self.direction = -1
            self.flip = True
            dx -= 5
        if moving_right:
            self.direction = 1
            self.flip = False
            dx += 5
        self.yvel += 1
        dy += self.yvel
        
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.yvel = 0
            self.in_air = False
        
        self.rect.y += dy    
        self.rect.x += dx
        
    def shoot(self, weapon_group):
        if self.ammo > 0 and pygame.time.get_ticks() - self.last_bullet_shoot_time > 100:
            self.last_bullet_shoot_time = pygame.time.get_ticks()
            self.ammo -= 1
            Bullet(self.type, 
                self.rect.centerx + self.direction * self.rect.size[0],
                self.rect.centery,
                weapon_group, 
                self.direction
                )
        
            
            
     
