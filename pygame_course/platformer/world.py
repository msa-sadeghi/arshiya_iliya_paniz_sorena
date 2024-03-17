from constants import *
class World:
    def __init__(self, data):
        self.tiles = []
        self.image = pygame.image.load("assets/background.png")
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 1:
                    image = pygame.transform.scale(dirt_image, (50,50))
                    rect = image.get_rect(topleft=(j * 50, i * 50))
                    tile = (image, rect)
                    self.tiles.append(tile)
                if data[i][j] == 2:
                    image = pygame.transform.scale(grass_image, (50,50))
                    rect = image.get_rect(topleft=(j * 50, i * 50))
                    tile = (image, rect)
                    self.tiles.append(tile)
                    
    def draw(self, screen):
        screen.blit(self.image,(0,0))
        for t in self.tiles:
            screen.blit(t[0], t[1])
        