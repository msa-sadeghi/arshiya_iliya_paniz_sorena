from constants import *
from world import World
from level_creator import world_data
from player import Player

game_player = Player(100, 400)
game_world = World(world_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    game_world.draw(screen) 
    game_player.draw(screen) 
    game_player.update()      
    pygame.display.update()
    clock.tick(FPS)
    