import turtle
import time

delay=0.1
#screan set up
wn=turtle.Screen()
wn.title("nokiya ")

wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.tracer(0)

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)
food.direction="stop"


def go_up():
    head.direction="up"
def go_down():
    head.direction="down"
def go_left():
    head.direction="left"
def go_right():
    head.direction="right"


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    elif head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    elif head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    elif head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"x")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()
    if head.distance(food)<20:

    move()

    #time.sleep(delay)
wn.mainloop()
