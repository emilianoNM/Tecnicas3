###programa para pedir 3 numeros y decir que numero es mayor.

num1 = int(input("Ingrese el primer n�mero: "))

num2 = int(input("Ingrese el segundo n�mero: "))

num3 = int(input("Ingrese el tercer n�mero: "))

if num1 > num2 and num1 > num3:
    print "el mayor es %d"%num1

elif num2 > num1 and num2 > num3:
    print "el mayor es %d"%num2

elif num3 > num1 and num3 > num2:
    print "el mayor es %d"%num3
else:
    print "2 o m�s n�meros son iguales"