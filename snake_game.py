import turtle
import time
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
    snake_head.direction = "up"
def go_down():
    snake_head.direction = "down"
def go_left():
    snake_head.direction = "left"
def go_right():
    snake_head.direction = "right"

snake_head = create_turtle("square", "green")
snake_head.direction = ""
snake_food = create_turtle("circle","red")
snake_head.goto(100,100)
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_right, "d")
screen.onkeypress(go_left, "a")
run = True
while run:
    screen.update()
    move()
    time.sleep(0.2)