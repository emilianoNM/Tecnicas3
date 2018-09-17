#Este programa te da la Fecha y hora del dia de hoy y te muestra el calendario

import datetime
import calendar


Hoy = datetime.datetime.now()
print ("\nLa Fecha y Hora del dia de hoy es:\n\t ")
print (Hoy.strftime("%Y-%m-%d %H:%M:%S"))

print("\n\tSe imprimira el calendario del Mes y Ano que especifiques:\n (Introducir mes en numero [1,2,3...12])\n")

Ano = int(input("Introduzca el Ano: "))
Mes = int(input("Introduzca el Mes : "))

print(calendar.month(Ano, Mes))