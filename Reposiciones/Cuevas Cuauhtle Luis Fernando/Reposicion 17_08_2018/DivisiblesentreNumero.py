#Este programa encuentra los numeros divisibles entre un rango intruoducido


Rango=[]

Inicio = int(input("\nPorfavor Introduzca el inicio del Intervalo:"))

Fin = int(input("\nPorfavor Introduzca el fin del Intervalo:"))

print("\n")

for x in range(Inicio, Fin):

    if (x%7==0) and (x%5==0):

        Rango.append(str(x))

print (','.join(Rango))
