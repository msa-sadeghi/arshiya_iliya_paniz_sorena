import pygame

class Button:
    def __init__(self, x,y, image):
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))
        
        
    def draw(self, screen):
        click = False
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                click = True
        screen.blit(self.image, self.rect)        
        return click