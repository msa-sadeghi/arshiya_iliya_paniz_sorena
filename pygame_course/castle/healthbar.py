import pygame
class HealthBar:
    def __init__(self, x,y, health, max_health):
        self.x = x
        self.y = y
        self.health = health
        self.max_health = max_health
        self.font = pygame.font.SysFont("arial", 16)
        
    def update(self, screen, health):
        
        r = health/self.max_health
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, 100, 20))
        pygame.draw.rect(screen, (0,255,0), (self.x, self.y, 100 * r, 20))
        h = self.font.render(str(health), True, (0,0,0))
        screen.blit(h, (self.x + 20,self.y ))
        