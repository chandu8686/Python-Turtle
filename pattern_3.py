import turtle
t=turtle.Turtle()
turtle.title('chandu_graphics')
s=turtle.Screen()
#t.pencolor(random.Random.choice(color))
t.pencolor('purple')
s.bgcolor('black')
t.speed(0)
t.pensize(2)
a=0
b=0
t.penup()
t.goto(0,200)
t.pendown()
t.hideturtle()
while True:
    t.forward(a)
    t.right(b)
    a+=3
    b+=1
    if b==310:
        break
turtle.mainloop()

