import pygame
from castle import Castle
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
bg = pygame.image.load("assets/bg.png")
bullet_group = pygame.sprite.Group()
my_castle = Castle(520, 300)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(bg, (0,0)) 
    my_castle.draw(screen)  
    my_castle.shoot(bullet_group) 
    bullet_group.update()    
    bullet_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)