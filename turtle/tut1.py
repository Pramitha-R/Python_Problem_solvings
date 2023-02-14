from turtle import * 

pensize(10)

penup()
goto(-250,100)
color("yellow","red")
pendown()

"""
forward(200)
back(100)
right(90)
forward(200)

"""

begin_fill()
for i in range(4):
    forward(150)
    left(90)
end_fill()
exitonclick()