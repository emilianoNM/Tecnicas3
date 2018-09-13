def es_bisiesto(t):
    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

print("Comprobador de anios bisiestos")
fecha = int(input("Escriba un anio, el programa indicará su naturaleza: "))
if es_bisiesto(fecha):
    print(fecha, "es un año bisiesto.")
else:
    print(fecha, "no es un año bisiesto.")
