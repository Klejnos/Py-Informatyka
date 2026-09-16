while True: 
    t = int(input("Podaj temperaturę wewnątrz szklarni: "))
    if t <= 0: 
        print ("Bezpieczne wyłączanie programu")
        break
    elif t >= 30:
        print ("ALARM! Temperatura za wysoka! Wyłączam system")
        break
    else:
        print ("Temperatura w normie")