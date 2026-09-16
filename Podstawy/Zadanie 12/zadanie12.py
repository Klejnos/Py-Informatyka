vk = float(input("Podaj prędkość Kojota: "))
vs = float(input("Podaj prędkość Strusia: "))

def kto_wygral(vk, vs):
    zwyciezca = ""

    if vk > vs:
        zwyciezca = "Kojot"
    else: 
        zwyciezca = "Struś"

    return zwyciezca

print("Wygrał:", kto_wygral(vk, vs))