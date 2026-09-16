a = float(input("Wprowadź drogę pokonaną przez pojazd w metrach: "))
b = float(input("Podaj czas jazdy w sekundach: "))

def predkosc(a, b):
    return round(a/b)

print("Prędkość wyniosła", predkosc(a, b), "m/s")