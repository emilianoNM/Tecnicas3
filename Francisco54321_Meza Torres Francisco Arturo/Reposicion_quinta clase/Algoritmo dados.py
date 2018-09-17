from random import randint

def tiraDados():
	return randint(1,6)

def cuentaTiros(tiros):
	cuenta = [0 for x in range(1,12)]

	for x in tiros:
		cuenta[x-2] += 1

	return cuenta


def main():
	tiros = []
	
	for x in range(3600):
		tiros.append(tiraDados()+tiraDados())

	cuenta = cuentaTiros(tiros)

	for x in range(len(cuenta)):
		print("La suma: "+str(x+2)+" se repite "+str(cuenta[x])+" veces")
	if cuenta[5]/3600 >= 1/6 :
		print("Se comprueba la probabilidad")
main()
