import pygame
import pickle
pygame.init()
clock = pygame.time.Clock()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bg1 = pygame.image.load("./assets/img/background/pine1.png")
bg2 = pygame.image.load("./assets/img/background/pine2.png")
bg3 = pygame.image.load("./assets/img/background/mountain.png")
bg4 = pygame.image.load("./assets/img/background/sky_cloud.png")

def draw_bg():
    screen.fill("green")
    screen.blit(bg4, (0,0))
    screen.blit(bg3, (0,SCREEN_HEIGHT - bg3.get_height() - 300))
    screen.blit(bg2, (0,SCREEN_HEIGHT - bg1.get_height() - 150))
    screen.blit(bg1, (0,SCREEN_HEIGHT - bg2.get_height()))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_bg()
    
    pygame.display.update()