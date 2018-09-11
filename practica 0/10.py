

print("PachecoJesus")
import math
x=1
i=0
Error=100
while Error>.0001:
    y = -math.log(x)+math.exp(-x)
    dy=-math.exp(-x)- 1/x
    x1=x-y/dy
    Error=abs((x-x1)/(x1))
    x=x1
    i=i+1
    print("Iteracion",i, "Funcion",x,  "Derivada",y,   "Error",Error)