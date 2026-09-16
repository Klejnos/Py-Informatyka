import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(3)

def kolko1(x, kolor):
    t.color(kolor)
    t.begin_fill()
    t.circle(x)
    t.end_fill()

def kolko2(x, kolor):
    t.color(kolor)
    t.begin_fill()
    t.circle(x)
    t.end_fill()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.color("white")
    t.circle(x-10)
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
    t.right(180)

def przejscie(x):
    t.penup()
    t.circle(x, 60)
    t.right(180)
    t.pendown()

kolko1(80, "yellow")

t.penup()
t.left(90)
t.forward(40)
t.right(90)
t.pendown()

kolko1(40, "blue")

t.penup()
t.right(90)
t.forward(40)
t.left(90)
t.circle(80,30)
t.left(180)
t.pendown()

kolorki = ["yellow", "brown", "green", "red", "orange", "purple"]
for i in range(6):
    R = 80
    kolko2(R, kolorki[i])
    przejscie(R)

t.hideturtle()
turtle.exitonclick()