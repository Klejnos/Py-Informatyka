import turtle
window = turtle.Screen()
t = turtle.Turtle()
def circle():
    t.circle(90)
window.onkey(circle,'c')
window.listen()
window.mainloop()