import turtle
from turtle import *
import random

t=Turtle()
s=Screen()
color=["White","Black","Brown","Magenta","Aquamarine","Turquoise","Silver","Lime","Teal","Indigo","Violet",
        "Pink","Gray","Olive","Maroon","Navy Blue",'yellow']

t.pencolor(random.choice(color))
s.bgcolor('black')
t.speed(0)
c=0
d=0

while True:
    for x in range(4):
        t.forward(80)
        t.right(90)
    t.right(15)
    c +=1
    if c >= 390/15:
        t.forward(50)
        c=0
        d +=1
        if d>=12:
            break

t.hideturtle()

turtle.mainloop()
