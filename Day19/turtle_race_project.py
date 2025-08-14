from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)
def move_backward():
    tim.backward(20)
def counter_clockwise():
    tim.left(90)
def clockwise():
    tim.right(90)
def clear_everything():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=counter_clockwise)
screen.onkey(key="d",fun=clockwise)
screen.onkey(key="c",fun=clear_everything)

screen.exitonclick()