koszt = int(input("Ile kosztuje Twój wymarzony komputer? (zł): "))
odlozone = int(input("Ile masz już odłożone? (zł): "))
ile_mozna = int(input("Ile możesz odkładać co miesiąc? (zł): "))
miesiac = 0

while odlozone < koszt:
    odlozone += ile_mozna
    miesiac += 1
    print("Miesiąc", miesiac, ": Masz już", f"{odlozone:.2f}", "zł")

reszta = odlozone - koszt
print("GRATULACJE! Uzbierałeś już na komputer w", miesiac, "miesięcy.")
print("Zostanie ci jeszcze", f"{reszta:.1f}", "zł na gry!")