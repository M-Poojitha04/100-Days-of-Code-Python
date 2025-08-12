import random
# import colorgram
import turtle
from turtle import Turtle,Screen
# colors = colorgram.extract('image.jpg',20)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)
tim = Turtle()
my_color_list = [
 (255, 87, 34), (0, 188, 212), (156, 39, 176), (249, 228, 17),
 (213, 13, 9), (198, 12, 35), (231, 228, 5), (197, 69, 20),
 (33, 90, 188), (43, 212, 71), (234, 148, 40), (33, 30, 152),
 (16, 22, 55), (66, 9, 49), (76, 175, 80), (244, 39, 149),
 (65, 202, 229), (14, 205, 222), (63, 21, 10), (224, 19, 111)
]
turtle.colormode(255)
screen = Screen()
screen.setworldcoordinates(0,0,400,400)
tim.speed('fastest')
tim.hideturtle()
for i in range(10):
    for _ in range(9):
        tim.dot(20,random.choice(my_color_list))
        tim.up()
        tim.forward(40)
        tim.down()
        tim.dot(20,random.choice(my_color_list))
        tim.up()
    if i % 2 == 0:
        tim.left(90)
        tim.forward(40)
        tim.left(90)
        tim.down()
    else:
        tim.right(90)
        tim.forward(40)
        tim.right(90)
        tim.down()



screen.exitonclick()