a = int(input("Podaj bok a = "))
b = int(input("Podaj bok b = "))
c = int(input("Podaj bok c = "))


def sprawdz_trojkat(a, b, c):
    if(a + b > c and a + c > b and b + c > a):
        return "Można zespawać trójkąt"
    else:
        return "Nie można zespawać trójkąta"


print(sprawdz_trojkat(a, b, c))