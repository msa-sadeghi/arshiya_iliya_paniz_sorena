from constants import *
from world import World
from level_creator import world_data
from player import Player
from button import Button
restart_button = Button(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
enemy_group = pygame.sprite.Group()
game_player = Player(100, 400)
game_world = World(world_data, enemy_group)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen) 
    game_player.draw(screen) 
    if game_player.alive:
        game_player.update(game_world.tiles, enemy_group) 
        enemy_group.empty()
        game_world = World(world_data, enemy_group)
        
    else:
        restart_button.draw(screen)
        if restart_button.update():
            game_player.__init__(100, 400)
            
    enemy_group.update()     
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    