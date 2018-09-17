#Este programa comprueba si un ano es bisiesto o no



Fecha = int(input("Escribe un ano: "))

def es_bisiesto(t):

    return t % 400 == 0 or (t % 100 != 0 and t % 4 == 0)

 if Fecha % 400 == 0 or (Fecha % 100 != 0 and Fecha % 4 == 0):

    print( Fecha, "Si es bisiesto.")


Fecha = int(input("Escriba al ano que quieres comprobar: "))

if es_bisiesto(Fecha):

    print(Fecha, "Si es bisiesto.")
else:
    print( Fecha, "No lo es.")

print(Fecha, "No es un año bisiesto.")