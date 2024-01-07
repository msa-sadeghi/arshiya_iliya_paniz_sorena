# for i in range(5):
#  print('ok',i)
#  print("blalalalla")

# for i in range(1000, 1501, 3):
#     print(i)

import turtle

main_screen = turtle.Screen()
main_screen.title("hello")
main_screen.bgcolor("cyan")
main_screen.setup(600,600)


my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("green")
my_turtle.shapesize(2)
my_turtle.pensize(3)
my_turtle.pencolor("red")
my_turtle.begin_fill()
for i in range(3):
    my_turtle.fd(130)
    my_turtle.left(120)
my_turtle.end_fill()

turtle.done()

# TODO
# کشیدن مربع، پنج و شش و هفت ضلعی
# با کمک حلقه فور اعداد 1 تا 1000 را با هم جمع نمائید