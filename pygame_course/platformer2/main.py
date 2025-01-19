import pygame
from config import * 
from character import Character
grenade_group = pygame.sprite.Group()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
player = Character("player", 100, 300, 5, 60, 10)
moving_left = False
moving_right = False
jump = False
shoot_bullet = False
shoot_grenade = False
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jump = True
            if event.key == pygame.K_SPACE:
                shoot_bullet = True
            if event.key == pygame.K_g:
                shoot_grenade = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_SPACE:
                shoot_bullet = False
            if event.key == pygame.K_g:
                shoot_grenade = False
    if moving_left or moving_right:
        player.change_action("Run")
    elif jump:
        player.in_air = True
        player.yvel = -13
    else:
        player.change_action("Idle")
    if player.in_air:
        player.change_action("Jump")
    if shoot_bullet:
        player.shoot("bullet",player_bullet_group)
    if shoot_grenade:
        player.shoot("grenade", grenade_group)
    screen.fill((0,0,0))
    player.move(moving_left, moving_right)            
    player.draw(screen)  
    player_bullet_group.update()
    player_bullet_group.draw(screen)     
    grenade_group.update()
    grenade_group.draw(screen)     
    pygame.display.update() 
    clock.tick(FPS)