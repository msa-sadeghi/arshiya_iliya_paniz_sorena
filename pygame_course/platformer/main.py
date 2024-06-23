from constants import *
from world import World
from player import Player
from button import Button
import pickle
level = 1
def go_to_next_level():
    global world_data
    f = open(f"level{level}", "rb")
    world_data = pickle.load(f)
    enemy_group.empty()
    door_group.empty()
    game_world = World(world_data, enemy_group, door_group)
    game_player.__init__(100, 400)
    return game_world 
pygame.init()
restart_button = Button(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2)
enemy_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
game_player = Player(100, 400)
game_world = go_to_next_level()   

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen) 
    game_player.draw(screen) 
    if game_player.alive:
        game_player.update(game_world.tiles, enemy_group, door_group)
    else:
        restart_button.draw(screen)
        if restart_button.update():
            game_player.__init__(100, 400)
            enemy_group.empty()
            door_group.empty()
            game_world = World(world_data, enemy_group, door_group)
    if game_player.next_level:
        level += 1
        game_world = go_to_next_level()   
                
    enemy_group.update()     
    enemy_group.draw(screen)
    door_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    