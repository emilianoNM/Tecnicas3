#Este programa te dice si un Numero que indroduzcas es par o impar

print("\n\tPar o impar\n")


Numero = int(input("Introduzca el Numero: "))
mod = Numero % 2 #Calculando su modulo podemos saber si sera par o impar, en donde un modulo diferente de 0 sera impar
if mod > 0: #Agregamos la condicion
    print(Numero, "es un numero Impar")
else:
    print(Numero, "es un numero Par")
