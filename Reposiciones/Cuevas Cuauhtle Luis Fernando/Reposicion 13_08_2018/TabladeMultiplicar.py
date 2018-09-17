#Este programa crea una tabla de multiplicar con un numero que introduzcas

Numero = int(input("Introduzca el numero que quiera generar la tabla"))

# use for loop to iterate 10 times
for i in range(1,11):
   print(Numero,'x',i,'=',Numero*i)
