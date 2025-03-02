import pygame
from config import * 
from character import Character
player_grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player_bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
player = Character("player", 100, 300, 5, 60, 10)
enemy = Character("enemy", 300, 300, 5, 60, 10)
enemy_group = pygame.sprite.Group()
enemy_group.add(enemy)
moving_left = False
moving_right = False
jump = False
shoot_bullet = False
shoot_grenade = False
level = 1
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
                shoot = True
            if event.key == pygame.K_g:
                grenade_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jump = False
            if event.key == pygame.K_SPACE:
                shoot = False
            if event.key == pygame.K_g:
                grenade_shoot = False
    if player.alive:
        if moving_left or moving_right:
            player.change_animation("Run")
        elif jump and player.in_air == False:
            player.vely = -15
            player.in_air = True
            
        else:
            player.change_animation("Idle")
        if player.in_air:
            player.change_animation("Jump")
        if shoot_bullet:
            player.shoot("bullet",player_bullet_group)
        if shoot_grenade:
            player.shoot("grenade",player_grenade_group)
            
    if enemy.idle:
        enemy.change_animation("Idle")
    else:
        enemy.change_animation("Run")    
    if enemy.shoot_state:
        enemy.shoot("bullet", enemy_bullet_group)
    
    screen.fill((0,0,0))        
    enemy.draw(screen)
    enemy.ai(player)
   
    player.draw(screen)   
    player.move(moving_left, moving_right)    
    player_bullet_group.update()
    player_bullet_group.draw(screen) 
    enemy_bullet_group.update(player)
    enemy_bullet_group.draw(screen) 
    player_grenade_group.update(explosion_group)
    player_grenade_group.draw(screen) 
    explosion_group.update()
    explosion_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)