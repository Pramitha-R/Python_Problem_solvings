import turtle
import math
start = turtle.Turtle()
 

for i in range(3):
    start.right(90)
    start.forward(100)

start.left(90)
start.forward(50)

start.right(135)
start.forward(100*math.sqrt(2))

start.right(90)
start.forward(100*math.sqrt(2))

start.right(135)
start.forward(50)
turtle.done()