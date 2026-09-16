import turtle

turtle.bgcolor('blue')

zolw = turtle.Turtle()
zolw.shape('turtle')
zolw.color('yellow')
zolw.circle(30)
zolw.right(90)
zolw.circle(30)
zolw.penup()
zolw.goto(-300, 0)
zolw.pendown()
zolw.color('black')
zolw.write('Informatyka', font=("Comic Sanserif", 30, "bold"))
zolw.hideturtle()
turtle.exitonclick()