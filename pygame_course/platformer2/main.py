import pygame
from config import * 
from character import Character

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Character("player", 100, 300, 5, 60, 10)

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    player.draw(screen)       
    pygame.display.update()
    clock.tick(FPS)