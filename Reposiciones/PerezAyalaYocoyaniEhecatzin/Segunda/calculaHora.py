import time

def comparaHora(horaComp):
	
	hora = int(time.strftime("%I"))
	minutos = int(time.strftime("%M"))
	segundos = int(time.strftime("%S"))
	return hora*3600 + minutos*60 + segundos
	

def main():

	hora = [12, 0, 0, "pm"]
	print("La diferencia entre las 12 horas y la actual es "+str(comparaHora(hora))+" s")

main()