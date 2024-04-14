from constants import *
from world import World
from level_creator import world_data
from player import Player

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
    game_player.update(game_world.tiles) 
    enemy_group.update()     
    enemy_group.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    