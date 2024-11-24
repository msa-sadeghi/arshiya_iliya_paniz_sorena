from tkinter import *
from random import randint
class Snake:
    def __init__(self):
        self.body_size = BODY_SIZE
        self.coordinates = []
        self.squares = []
        
        for i in range(BODY_SIZE):
            self.coordinates.append([0,0])
        for x,y in self.coordinates:
            square =  canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="green", tag = "snake")
            self.squares.append(square)

class Food:
    def __init__(self):
        x = randint(0, (GAME_WIDTH//SPACE_SIZE - 1)) * SPACE_SIZE
        y = randint(0, (GAME_HEIGHT//SPACE_SIZE - 1)) * SPACE_SIZE
        self.coordinate = [x,y]
        canvas.create_oval(x,y, x+SPACE_SIZE, y + SPACE_SIZE, fill="red", tag="food")



def next_turn(snake, food):
    x,y = snake.coordinates[0]
    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    if direction == "left":
        x -= SPACE_SIZE
    if direction == "right":
        x += SPACE_SIZE
    snake.coordinates.insert(0, [x,y])
    square =  canvas.create_rectangle(x,y, x + SPACE_SIZE, y + SPACE_SIZE, fill="green", tag = "snake")
    snake.squares.insert(0, square)
    
    if x == food.coordinate[0] and y == food.coordinate[1]:
        global score
        score += 1
        label.config(text=f"Score: {score}")
        canvas.delete("food")
        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        
            
        
    
    window.after(200, next_turn, snake, food)

def change_direction(new_dir):
    global direction
    if new_dir == "left":
        if direction != "right":
            direction = "left"
    elif new_dir == "right":
        if direction != "left":
            direction = "right"
    elif new_dir == "up":
        if direction != "down":
            direction = "up"
    elif new_dir == "down":
        if direction != "up":
            direction = "down"
    


window = Tk()

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPACE_SIZE = 50
BODY_SIZE = 2
direction = "down"
score = 0
label = Label(window, text=f"Score: {score}", font=("Courier", 30))
label.pack()
canvas = Canvas(window, bg="black", width=GAME_HEIGHT, height=GAME_HEIGHT)
canvas.pack()


window.update()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

x = screen_width//2 - window_width//2
y = screen_height//2 - window_height //2

window.bind("<Up>",lambda e: change_direction("up"))
window.bind("<Down>",lambda e: change_direction("down"))
window.bind("<Left>",lambda e: change_direction("left"))
window.bind("<Right>",lambda e: change_direction("right"))


window.geometry(f"{window_width}x{window_height}+{x}+{y}")
snake = Snake()
food = Food()
next_turn(snake, food)
window.mainloop()