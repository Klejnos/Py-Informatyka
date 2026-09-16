import turtle

turtle.shape("turtle")
turtle.pensize(3)


def trojkat():
    for i in range(3):
        turtle.right(120)


turtle.forward(100)

trojkat()

for i in range(3):
    turtle.right(60)
    turtle.begin_fill()
    turtle.fillcolor("red")
    trojkat()
    turtle.end_fill()

turtle.mainloop()