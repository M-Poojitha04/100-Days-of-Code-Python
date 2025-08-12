import random
import turtle
from turtle import Turtle, Screen
tim = Turtle()
tim.shape("turtle")
tim.color("red")


# square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)


# dotted lines
# for _ in range(25):
#     tim.forward(5)
#     tim.up()
#     tim.forward(5)
#     tim.down()


# draw shapes
# sides = 3
colors = ["IndianRed","green","blue","yellow","orange","violet","magenta","DeepSkyBlue","grey","brown","purple","DarkOrchid","wheat","SeaGreen","LightSeaGreen","CornflowerBlue"]
# while sides != 10:
#     for i in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)
#     sides += 1
#     tim.color(random.choice(colors))


# random walk
# directions = [0,90,180,360]
# tim.pensize(15)
# tim.speed("fastest")
# for i in range(100):
#     tim.color(random.choice(colors))
#     tim.forward(50)
#     tim.setheading(random.choice(directions))


# random color
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tup = (r,g,b)
    return tup
# directions = [0,90,180,360]
# tim.pensize(15)
# tim.speed("fastest")
# for i in range(100):
#     tim.color(random_color())
#     tim.forward(50)
#     tim.setheading(random.choice(directions))

# spirograph
tim.speed("fastest")
tim.pensize(2)
for i in range(120):
    tim.color(random_color())
    tim.circle(100)
    tim.left(3)


screen = Screen()
screen.exitonclick()