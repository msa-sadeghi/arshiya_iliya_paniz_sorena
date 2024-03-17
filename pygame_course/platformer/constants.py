import pygame
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750
FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

dirt_image = pygame.image.load("assets/dirt.png")
grass_image = pygame.image.load("assets/grass.png")