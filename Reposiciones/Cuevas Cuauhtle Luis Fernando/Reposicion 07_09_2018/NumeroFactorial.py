#Este programa calcula el Factorial de un numero 

Numero=int(raw_input("Escriba el numero que quiera Factorial:"))

Factorial=1

for i in range(1,(Numero+1)):
     
        Factorial=Factorial*i


print("El Factorial de", Numero, "es: ", Factorial)



