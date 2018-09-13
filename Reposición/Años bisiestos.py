print("Comprobador de anios bisiestos")
fecha = int(input("Escriba un anio: "))

if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
    print( fecha, "es bisiesto.")
else:
    print( fecha, "no es bisiesto.")
