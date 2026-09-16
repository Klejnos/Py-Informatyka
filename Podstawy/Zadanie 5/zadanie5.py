a = int(input("Podaj liczbe a: "))
b = int(input("\nPodaj liczbe b: "))

def suma(a, b):
    print("\nsuma = ", a + b)

def roznica(a, b):
    print("\nroznica = ", a - b)

def iloczyn(a, b):
    print("\niloczyn = ", a * b)

def iloraz(a, b):
    print("\niloraz = ", round(a / b, 2))

def reszta(a, b):
    print("\nreszta = ", a % b)

def pierwiastek(x):
    print("\npierwiastek kwadratowy z liczby ", x, " = ", round(x ** 0.5, 2))

suma(a, b)
roznica(a, b)
iloczyn(a, b)
iloraz(a, b)
reszta(a, b)
pierwiastek(a)
pierwiastek(b)
print("\n\n")