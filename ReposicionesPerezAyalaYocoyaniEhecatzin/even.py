def even(numero1):	
	if numero1%2 == 0:
		return 1 
	else :
		return 0

def lectura(nombreDato):
	while True:
		try: 
			print("Inroduce el valor "+ nombreDato)
			lectura = int(input("--> "))
			break
		except:
			print("Valor no valido")
	return lectura

def main():
	numero1 = lectura("a evaluar")
	print(even(numero1))
main()