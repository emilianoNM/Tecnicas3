###programa para sacar hipotenusa de un triangulo

import math
cat1=float(input("ingrese un cateto\n"))
cat2=float(input("ingrese el otro cateto\n"))
hip=math.sqrt((cat1*cat1+cat2*cat2))
print(str(hip))