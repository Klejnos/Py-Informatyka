pm25 = int(input("Podaj wartość parametru PM25 = "))
pm10 = int(input("Podaj wartość parametru PM10 = "))

def setPower(pm25, pm10):
    if (0 < pm25 <= 12):
        wynik25 = 0
    elif (13 <= pm25 <= 24):
        wynik25 = 1
    elif (25 <= pm25 <= 36):
        wynik25 = 2
    elif (pm25 > 36):
        wynik25 = 3
    
    if (0 < pm10 <= 20):
        wynik10 = 0
    elif (21 <= pm10 <= 50):
        wynik10 = 1
    elif (51 <= pm10 <= 80):
        wynik10 = 2
    elif (pm10 > 80):
        wynik10 = 3

    if (wynik10 > wynik25):
        gorsza = wynik10
    else: gorsza = wynik25

    if (gorsza == 0): stan = "Bardzo dobry,"
    elif (gorsza == 1): stan = "Dobry,"
    elif (gorsza == 2): stan = "Umiarkowany,"
    elif (gorsza == 3): stan = "Zły,"
    
    print(stan, "moc wentylatora =", gorsza)

setPower(pm25, pm10)