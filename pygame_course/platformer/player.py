from constants import *
class Player:
    def __init__(self, x,y):
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            image = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(image)
            image = pygame.transform.flip(image, True, False)
            self.left_images.append(image)
            
        self.image_number = 0
        self.image = self.right_images[self.image_number]
        self.rect = self.image.get_rect(topleft=(x,y))
        self.gravity = 0
        self.update_time = pygame.time.get_ticks()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        dx = 0
        dy = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx -= 5
        if keys[pygame.K_RIGHT]:
            dx += 5
        if keys[pygame.K_SPACE]:
            self.gravity = -13
        dy += self.gravity
        # self.gravity += 1
        self.rect.x += dx
        self.rect.y += dy
        self.animation()
        
    def animation(self):
        if pygame.time.get_ticks() - self.update_time > 100:
            self.image_number += 1
            self.update_time = pygame.time.get_ticks()
        if self.image_number >= len(self.right_images):
            self.image_number = 0
        self.image = self.right_images[self.image_number]
        
        