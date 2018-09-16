
while True:
        try :
            t= float(input("Escribe tiempo: "))
            break
        except :
            print("no")
if t != 0:
        v = float(180/(30+2*t))
        a= float((v-180)/t)
        print("La razon de cambio en el tiempo ",t,"s es ",a,"cm^3/s")


