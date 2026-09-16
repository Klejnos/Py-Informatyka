x = int(input("Podaj liczbę od 1 do 7:"))

def dzien_tygodnia(x):
    if 0 < x < 8:
        return True
    return False

print(dzien_tygodnia(x))