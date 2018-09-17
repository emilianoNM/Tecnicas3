#Este programa eleva al cuadrado a un intervalo de numeros


Fin = int(input("\nIntroduzca el numero de elementos de la lista cuadratica: "))

print("\n")

def Valores():
	l = list()
	for i in range(1,Fin):
		l.append(i**2)
	print(l)
		
Valores()