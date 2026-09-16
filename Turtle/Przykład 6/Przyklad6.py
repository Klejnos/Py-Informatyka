import turtle
# Ustawienie żółwia w początkowej pozycji
turtle.penup()
turtle.goto(50, 100) # Przesunięcie żółwia na współrzędne (50, 100)
# Pobranie bieżącej pozycji żółwia
pozycja = turtle.pos()
print("Pozycja żółwia:", pozycja) # Wydrukuje np. (50.00, 100.00)