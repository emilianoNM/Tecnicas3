#suma de numeros
inicio=int(raw_input("ingresa inicio:"))
fin=int(raw_input("ingresa fin:"))
suma=0

for i in range (inicio,fin+1):
    
     suma=suma+i

print("la suma es %s",suma)
