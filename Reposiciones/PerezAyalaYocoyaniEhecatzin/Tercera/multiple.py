def multiple(numero1, multiplo):	
	if multiplo%numero1 == 0:
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
	numero1 = lectura("base")
	multiplo = lectura("multiplo")
	print(multiple(numero1, multiplo))

main()