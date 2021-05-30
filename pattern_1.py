import turtle
#color=["White","Black","Brown","Magenta","Aquamarine","Turquoise","Silver","Lime","Teal","Indigo","Violet",
        "Pink","Gray","Olive","Maroon","Navy Blue",'yellow']

t=turtle.Turtle()
s=turtle.Screen()

t.pencolor('white')
s.bgcolor('black')

for x in range(4):
    t.forward(88)
    t.right(90)

t.hideturtle()

turtle.done()
