#Este programa calcula la mediana entre 3 numeros

a = float(input("Introduzca el primer numero: "))
b = float(input("Introduzca el segundo numero: "))
c = float(input("Introduzca el tercero numero:"))

if a > b:
    if a < c:
        Mediana = a
    elif b > c:
        Mediana = b
    else:
        Mediana = c
else:
    if a > c:
        Mediana = a
    elif b < c:
        Mediana = b
    else:
        Mediana = c

print("La mediana es:", Mediana)