import pygame
class Player:
    def __init__(self, x,y):
        self.image = pygame.image.load("second_game/sonic.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.speed = 5
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        
player1 = Player(100, 100)
player2 = Player(300, 100)

screen = pygame.display.set_mode((600, 400))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    player1.draw(screen)        
    player2.draw(screen)  
    player1.move()      
    player2.move()      
    pygame.display.update()
        