import turtle
import random

# Ustawienia ekranu
screen = turtle.Screen()
screen.title("Kliknij kulę, aby zniknęła")

# Lista kul i ich początkowych kolorów
colors = ["red", "green", "yellow", "purple", "orange"]
balls = []


# Funkcja tworząca kulę
def create_ball(x, y, color):
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color(color)
    ball.penup()
    ball.goto(x, y)
    balls.append(ball)
    return ball


# Funkcja usuwająca kulę po kliknięciu
def hide_ball_on_click(x, y):
    for ball in balls:
        if ball.distance(x, y) < 20:  # Jeśli kursor jest w zasięgu kuli
            ball.hideturtle()
            balls.remove(ball)
            break

        # Tworzenie 5 kul w losowych miejscach


for i in range(5):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    create_ball(x, y, colors[i])

# Przypisanie funkcji do zdarzenia kliknięcia myszą
screen.onclick(hide_ball_on_click)

# Rozpoczęcie pętli zdarzeń
screen.mainloop()