inferior = int(input("introduce rango inferior: "))
superior = int(input("Introduce rango superior: "))

print("numeros primos entre",inferior,"y",superior,"son:")

for num in range(inferior,superior + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
