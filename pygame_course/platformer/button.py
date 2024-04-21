import pygame
class Button:
    def __init__(self, x,y):
        self.image = pygame.image.load("assets/restart_btn.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def update(self):
        clicked = False
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                clicked = True
        return clicked
        