import turtle
t = turtle.Turtle()
t.shape('turtle')
turtle.bgcolor('blue')
t.pensize(3)
t.speed(100)
t.color('yellow')
t.circle(25)

t.right(90)
t.color('black')
t.circle(25)

t.penup()
t.circle(25, 270)
t.pendown()

t.left(90)
t.color('white')
t.circle(25)

t.penup()
t.circle(25, 90)
t.pendown()

t.right(90)
t.color('green')
t.circle(25)

t.penup()
t.circle(25, 270)
t.pendown()

t.left(90)
t.color('red')
t.circle(25)

t.penup()
t.color('orange')
t.home()
t.goto(150, 0)
t.write('jest!', font=("Comic Sanserif", 20, "bold"))

t.home()
t.goto(-200, 0)
t.write('Informatyka', font=("Comic Sanserif", 20, "bold"))

t.home()
t.goto(-20, -70)
t.write('mistrzem', font=("Comic Sanserif", 20, "bold"))
t.hideturtle()

turtle.exitonclick()
