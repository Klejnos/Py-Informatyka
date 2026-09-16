wyniki = input("Podaj wyniki kolejnych rzutów kostką (np. 123456): ")
# wyniki = "123456123456"

def everyThird(txt):
    txt2 = ""
    y = 0
    for i in txt:
        if (y % 3 == 0):
            txt2 += txt[y]
        y += 1
    
    return txt2

print("Podaję co trzeci wynik rzutów kostką:", everyThird(wyniki))