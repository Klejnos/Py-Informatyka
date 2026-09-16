import turtle
import random
turtle.bgcolor(0,0,1)
zolw = turtle.Turtle()
zolw.speed(0)
for x in range(50, 90):
    zolw.color(random.choice(['white','red','blue','green','yellow']))
    zolw.circle(30)
    zolw.forward(2)
    zolw.right(10)
turtle.exitonclick()