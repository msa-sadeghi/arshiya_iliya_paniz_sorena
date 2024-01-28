import turtle
import time
import random

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("snake game")

screen.tracer(False)


def create_turtle(tshape, tcolor):
    my_turtle = turtle.Turtle()
    my_turtle.shape(tshape)
    my_turtle.color(tcolor)
    my_turtle.penup()
    return my_turtle


def change_position():
    x = random.randint(-270, 270)
    y = random.randint(-270, 240)
    snake_food.goto(x, y)


def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        y += 20
        snake_head.sety(y)
    if snake_head.direction == "down":
        y = snake_head.ycor()
        y -= 20
        snake_head.sety(y)
    if snake_head.direction == "left":
        x = snake_head.xcor()
        x -= 20
        snake_head.setx(x)
    if snake_head.direction == "right":
        x = snake_head.xcor()
        x += 20
        snake_head.setx(x)


def go_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"


def go_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"


def go_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


def go_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"


snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle", "red")
change_position()
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")
score = 0
highscore = 0
scoreboard = create_turtle("square", "white")
scoreboard.ht()
scoreboard.goto(0, 260)

def end_game():
    global run
    run = False
    

root = screen._root
root.protocol("WM_DELETE_WINDOW", end_game)

snake_tails = []
is_dead = False
run = True
while run:
    scoreboard.clear()
    scoreboard.write(f"Score:{score}, highscore:{highscore}", font=("arial", 22), align="center")
    screen.update()
    if snake_head.distance(snake_food) < 20:
        change_position()
        score += 1
        if score > highscore:
            highscore = score
        new_tail = create_turtle("square", "darkgreen")
        snake_tails.append(new_tail)

    for i in range(len(snake_tails) - 1, 0, -1):
        x = snake_tails[i - 1].xcor()
        y = snake_tails[i - 1].ycor()
        snake_tails[i].goto(x, y)

    if len(snake_tails) > 0:
        snake_tails[0].goto(snake_head.xcor(), snake_head.ycor())
        
    if snake_head.xcor() > 290 or snake_head.xcor() < -290:
        snake_head.setx(-1 * snake_head.xcor())
        
    if snake_head.ycor() > 240:
        snake_head.sety(-290)
    if snake_head.ycor() < -290:
        snake_head.sety(240)
    move()
    for tail in snake_tails:
        if snake_head.distance(tail) < 20:
            is_dead = True
            
    if is_dead == True:
        is_dead = False
        snake_head.goto(0,0)
        snake_head.direction = ""
        score = 0
        for tail in snake_tails:
            tail.ht()
        snake_tails = []
        
            
            
            
    time.sleep(0.2)
