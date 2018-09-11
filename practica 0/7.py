

print("PachecoJesus")

def presion():
    print ("P(t) = 30 + 2t [cmHg]")
    print ("Vi = 60 cm3")
    t = float(input("Introduce el tiempo a calcular: "))
            
    if t != 0:
        volumen = float(180/(30+2*t))
        cambio = float((volumen-180)/t)
        print("La razon de cambio es ",cambio,"[cm^3/s]")
presion()
