###programa para saber numeros primos entre un rango dado 

menor = int(input("introduce rango inferior: "))
mayor = int(input("Introduce rango superior: "))

print("numeros primos entre",menor,"y",mayor,"son:")

for num in range(menor,mayor + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)