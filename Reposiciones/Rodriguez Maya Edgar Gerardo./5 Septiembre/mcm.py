### calcular el minimo comun multiplo

def lcm(x, y):
  
   if x > y:
       mayor = x
   else:
       mayor = y
 
   while(True):
       if((mayor % x == 0) and (mayor % y == 0)):
           lcm = mayor
           break
       mayor += 1
 
   return lcm
 
 
num1 = int(input("Introduce el primer numero: "))
num2 = int(input("Introduce el segundo numero: "))
 
print "El minimo comun multiplo de ", num1," y ", num2," es ", lcm(num1, num2)