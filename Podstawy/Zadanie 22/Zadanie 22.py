numer = int(input("Podaj numer z dziennika: "))
liczba = 1000 + numer * 100 + 15

def najblizsza_pierwsza(n):
    n += 1 # zaczynamy od 1 wiekszej od podanej


    while True: 
        pierwsza = True # zakladamy ze podana liczba jest pierwsza

        for i in range(2, int(n**0.5) + 1): # sprawdzamy czy liczba ma jakis dzielnik
            if n % i == 0: # jezeli nie jest pierwsza przerywa dzialanie petli
                pierwsza = False
                break

        if pierwsza == True: # jezeli sprawdzana liczba jest pierwsza to konczymy dzialanie funkcji
            return n
        

        n += 1

print(najblizsza_pierwsza(liczba))