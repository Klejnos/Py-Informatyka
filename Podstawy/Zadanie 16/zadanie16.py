a = int(input("Podaj liczbę a = "))
b = int(input("Podaj liczbę b = "))
c = int(input("Podaj liczbę c = "))


def sortuj_liczby(a, b, c):
    liczby = [a, b, c]
    najwieksza = max(liczby)
    najmniejsza = min(liczby)
    srodkowa = sum(liczby) - najwieksza - najmniejsza

    print("\nLiczba największa =", najwieksza)
    print("\nLiczba środkowa = ", srodkowa)
    print("\nLiczba najmniejsza = ", najmniejsza)


sortuj_liczby(a, b, c)