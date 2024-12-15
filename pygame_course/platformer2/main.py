import pygame
from config import * 


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    pygame.display.update()
    clock.tick(FPS)