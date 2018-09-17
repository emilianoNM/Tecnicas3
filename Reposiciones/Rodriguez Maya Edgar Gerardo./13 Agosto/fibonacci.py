###programa para imprimir la serie de fibonacci pidiendo el numero de terminos de esta

n = int(input("Ingrese número de términos para la sucesión? "))
a, b = 0,1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b