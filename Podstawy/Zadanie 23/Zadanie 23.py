while True:
    dol = int(input("Podaj dolną granicę: "))
    gor = int(input("Podaj górną granicę: "))

    if (gor > dol) :
        break
    else:
        print("Dolna granica musi być mniejsza od górnej!")

suma = 0

for x in range (dol, gor + 1): # gor jest +1 aby range obiejmowalo tez liczbe gor
    czy_pierwsza = True # zakladamy ze liczba jest pierwsza aby pozniej ewentualnie udowodnic ze nie jest

    if x < 2:
        czy_pierwsza = False
    for i in range(2, int (x ** 0.5) + 1): # szukanie dzielnika
        if (x % i == 0):
            czy_pierwsza = False
            break
    
    if czy_pierwsza == True:
        print(f"Liczba {x} to liczba pierwsza")
        suma += x

print(f"Suma = {suma}")