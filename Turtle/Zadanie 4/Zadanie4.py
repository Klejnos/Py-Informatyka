import turtle
t = turtle.Turtle()
t.shape('turtle')
t.pensize(3)


def trojkat(rozmiar, kolor):
    t.color(kolor)
    t.begin_fill()

    for i in range(3):
        t.right(120)
        t.forward(rozmiar)

    t.end_fill()
    t.color("black")

    for i in range(3):
        t.right(120)
        t.forward(rozmiar)


trojkat(100, "blue")
t.hideturtle()
turtle.exitonclick()
