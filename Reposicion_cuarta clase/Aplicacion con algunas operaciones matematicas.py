##Introducir dos valores A y B:
###Si A>=B, calcular e imprimir la suma 10+14+18+...+50 
###Si A/B<=30, calcular e imprimir el valor de (A^2+B^2)
a = input('Primer valor: ')
b = input('Segundo valor: ')
n = 10
suma = 0
sumas = 0
if a >= b:
    while n <= 50:
        suma += n
        n += 4
    print suma
if a/b <= 30:
    sumas = (a**2+b**2)
    print sumas
