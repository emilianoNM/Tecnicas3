import math
a=int(input("ingresa lado\n"))
b=int(input("ingresa lado\n"))
c=int(input("ingresa lado\n"))

if(abs(a-c)<b)and(b<(a+c)):
   
   print("si forma un triangulo")
else:
   print("no forma un triangulo")
   
