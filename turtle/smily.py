import turtle
import time

t = turtle.Turtle()
delay=1
def curve():
    t.color("red")
    for i in range(75):
        t.left(1)
        t.forward(1)
    
    for i in range(75):
        t.left(1)
        t.forward(1)

    time.sleep(delay)


#set a face
#t.speed(0)
t.penup()
t.goto(0,-150)
t.pendown()
t.color("black","yellow")
t.begin_fill()
t.pensize(10)
t.circle(150)
t.end_fill()

t.penup()
t.goto(-70,55)
t.color("black","black")
t.pendown()
t.begin_fill()
t.pensize(5)
t.circle(10)
t.end_fill()


t.penup()
t.goto(70,55)
t.color("black","black")
t.pendown()
t.begin_fill()
t.pensize(5)
t.circle(10)
t.end_fill()


t.penup()
t.goto(-70,-55)
t.pendown()
t.right(75)
curve()