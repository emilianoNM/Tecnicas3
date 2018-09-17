#Este programa te da la Fecha y hora del dia de hoy y te muestra el calendario

import datetime
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))
Hoy = datetime.datetime.now()
print ("La Fecha y Hora del dia de hoy es: ")
print (Hoy.strftime("%Y-%m-%d %H:%M:%S"))