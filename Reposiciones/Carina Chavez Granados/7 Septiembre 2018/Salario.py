#Programa que calcula salario segun el numero de horas, el precio de esta y las horas extras considerando una jornada de 8hrs al dia y 5 dias a la semana
#Chavez Granados

horas = input("Inserte el numero de horas semanales: ")
precio = input("Inserte el precio de la hora (regular): ")
precioextra= input("Ingrese el precio de la hora(extra):")
if horas > 40:
 	hextra = horas - 40
        print 'El salario semanal es de:', 40 * precio + hextra*precioextra
else:
        print 'El salario semanal es de:', horas * precio

