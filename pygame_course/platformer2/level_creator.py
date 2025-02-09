import pygame
import pickle
pygame.init()
clock = pygame.time.Clock()

scroll = 0
scroll_speed = 1
scroll_left, scroll_right = (False, False)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
SIDE_MARGIN = 300
LOWER_MARGIN = 100

ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS


screen = pygame.display.set_mode((SCREEN_WIDTH  + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))

bg1 = pygame.image.load("./assets/img/background/pine1.png")
bg2 = pygame.image.load("./assets/img/background/pine2.png")
bg3 = pygame.image.load("./assets/img/background/mountain.png")
bg4 = pygame.image.load("./assets/img/background/sky_cloud.png")

def draw_grid():
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "white", 
                         (i * TILE_SIZE - scroll, 0),
                         (i * TILE_SIZE - scroll, SCREEN_HEIGHT)
                         )
        # TODO draw horintal lines
def draw_bg():
    screen.fill("green")
    width = bg4.get_width()
    for i in range(4):
        screen.blit(bg4, (i * width - scroll * 0.3,0))
        screen.blit(bg3, (i * width - scroll * 0.4,SCREEN_HEIGHT - bg3.get_height() - 300))
        screen.blit(bg1, (i * width - scroll * 0.5,SCREEN_HEIGHT - bg1.get_height() - 150))
        screen.blit(bg2, (i * width - scroll * 0.6,SCREEN_HEIGHT - bg2.get_height()))
        
            

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1
  
    if scroll_left and scroll > 0:
        scroll -= scroll_speed * 5
    if scroll_right:
        scroll += scroll_speed * 5
    draw_bg()
    draw_grid()
    pygame.display.update()