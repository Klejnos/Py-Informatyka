print("--- SYSTEM GENEROWANIA CYBER-KLUCZY ---")
limit = int(input("Podaj górny zakres wyszukiwania (N): "))
print(f"\nSzukam par liczb bliźniaczych do {limit}...")

def czy_pierwsza(liczba):
    pary = 0

    for x in range(2, liczba + 1):
        pierwsza = True
        
        for i in range(2, int(x ** 0.5) + 1):
            if (x % i == 0):
                pierwsza = False
                break
        
        if pierwsza == True:
            druga = x + 2
            druga_pierwsza = True

            for i in range(2, int(druga ** 0.5) + 1):
                if druga % i == 0:
                    druga_pierwsza = False
                    break
            
            if druga_pierwsza and druga <= liczba:
                print(f"Znaleziono cyber-klucz: ({x}, {druga})")
                pary += 1
    print("\nOperacja zakończona. Łącznie znaleziono par:", pary)

czy_pierwsza(limit)