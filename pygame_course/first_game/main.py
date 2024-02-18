import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FPS = 60
clock = pygame.time.Clock()

rabbit_left_image = pygame.image.load("first_game/assets/rabbit.png")
rabbit_right_image = pygame.transform.flip(rabbit_left_image, True, False)

rabbit_image = rabbit_right_image
rabbit_rect = rabbit_image.get_rect()
rabbit_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

carrot_image = pygame.image.load("first_game/assets/carrot.png")
carrot_rect = carrot_image.get_rect()
carrot_rect.centerx = random.randint(0, SCREEN_WIDTH)
carrot_rect.y = 700

# pygame.mixer.music.load("اسم و آدرس موزیک")
# pygame.mixer.music.play(-1)

eat_sound = pygame.mixer.Sound("اسم و آدرس صدا")


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rabbit_rect.left > 0:
        rabbit_image = rabbit_left_image
        rabbit_rect.x -= 5
    if keys[pygame.K_RIGHT] and rabbit_rect.right < SCREEN_WIDTH:
        rabbit_image = rabbit_right_image
        rabbit_rect.x += 5
    if keys[pygame.K_UP] and rabbit_rect.top > 0:
        rabbit_rect.y -= 5
    if keys[pygame.K_DOWN] and rabbit_rect.bottom < SCREEN_HEIGHT:
        rabbit_rect.y += 5
    carrot_rect.y -= 5
    if carrot_rect.top <= 0:
        carrot_rect.centerx = random.randint(0, SCREEN_WIDTH)
        carrot_rect.y = 700
    if rabbit_rect.colliderect(carrot_rect):
        carrot_rect.centerx = random.randint(0, SCREEN_WIDTH)
        carrot_rect.y = 700
        # TODO
        
    
        
    screen.fill((190, 20, 200))   
    screen.blit(rabbit_image, rabbit_rect)
    screen.blit(carrot_image, carrot_rect)
    pygame.display.update()
    clock.tick(FPS)
    