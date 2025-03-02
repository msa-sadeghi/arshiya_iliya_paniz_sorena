import pygame
import pickle
pygame.init()
clock = pygame.time.Clock()
from button import Button
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

current_tile = 0
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
        
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "white", (0, i * TILE_SIZE), (SCREEN_WIDTH, i * TILE_SIZE))
def draw_bg():
    screen.fill("green")
    width = bg4.get_width()
    for i in range(4):
        screen.blit(bg4, (i * width - scroll * 0.3,0))
        screen.blit(bg3, (i * width - scroll * 0.4,SCREEN_HEIGHT - bg3.get_height() - 300))
        screen.blit(bg1, (i * width - scroll * 0.5,SCREEN_HEIGHT - bg1.get_height() - 150))
        screen.blit(bg2, (i * width - scroll * 0.6,SCREEN_HEIGHT - bg2.get_height()))
        
images_list = list() 
for i in range(21):
    img = pygame.image.load(f"./assets/img/tile/{i}.png")  
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE)) 
    images_list.append(img)       

buttons_list = list()
col = 0
row = 0
for i in range(21):
    btn = Button(
        SCREEN_WIDTH + col * 70 + 60,
        row * 70 + 60,
        images_list[i]
    )
    col += 1
    if col == 3:
        col = 0
        row += 1
    buttons_list.append(btn)


world_data = []
for i in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)
for i in range(MAX_COLS):
    world_data[-1][i] = 0

def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] >= 0:
                screen.blit(images_list[world_data[i][j]], (j * TILE_SIZE - scroll, i * TILE_SIZE))


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
    draw_world()
    pygame.draw.rect(screen, "lightgreen", (SCREEN_WIDTH, 0, SIDE_MARGIN, LOWER_MARGIN + SCREEN_HEIGHT))
    for i in range(21):
        if buttons_list[i].draw(screen):
            current_tile = i
    mouse_pos = pygame.mouse.get_pos()
    col_number = (mouse_pos[0] + scroll) // TILE_SIZE
    row_number = mouse_pos[1] // TILE_SIZE
    if pygame.mouse.get_pressed()[0]:
        if world_data[row_number][col_number] != current_tile:
            world_data[row_number][col_number] = current_tile
    if pygame.mouse.get_pressed()[2]:
        world_data[row_number][col_number] = -1
    pygame.draw.rect(screen, "red", buttons_list[current_tile].rect, 3)
    pygame.display.update()