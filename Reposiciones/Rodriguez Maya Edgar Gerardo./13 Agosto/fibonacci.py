###programa para imprimir la serie de fibonacci pidiendo el numero de terminos de esta

n = int(input("Ingrese n�mero de t�rminos para la sucesi�n? "))
a, b = 0,1
for i in range(n):
    print(a, end=' ')
    a, b = b, a + b