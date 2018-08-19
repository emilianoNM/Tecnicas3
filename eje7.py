
while True:
        try :
            t= float(input("Escribe tiempo: "))
            break
        except :
            print("no")
if t != 0:
        v = float(180/(30+2*ti))
        a= float((volumen-180)/ti)
        print("La razon de cambio en el tiempo ",t,"s es ",a,"cm^3/s")


