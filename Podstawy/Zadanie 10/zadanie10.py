x = int(input("Proszę wpisać liczbę x:\n"))
y = int(input("Proszę wpisać liczbę y:\n"))

def wieksza(x, y):
    if x > y:
        return x
    return y

print("Liczba wieksza to", wieksza(x, y))