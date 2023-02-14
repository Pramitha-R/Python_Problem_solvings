import turtle

turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(20)


for i in range(100):
    for colors in ["red","blue","cyan","green","yellow"]:
        turtle.color(colors)
        if(colors=="red"):
            turtle.circle(150)
        else:
            turtle.circle(100)

        turtle.left(10)
turtle.hideturtle()#hiding the turtle invisible somthing