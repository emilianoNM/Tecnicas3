

print("PachecoJesus")
import math
a=int(input("Ingresa coeficiente cuadratico: "))
b=int(input("Ingresa coeficiente lineal: "))
c=int(input("Ingresa constante: "))
disc=b*b-4*a*c
if(a!=0):
 if(disc<0):
  print("La ecuacion tiene raices imaginarias")
 else:
  x1=(-b+(math.sqrt(disc)))/(2*a)
  x2=(-b-(math.sqrt(disc)))/(2*a)
  print("\nX1 = "+str(x1)+" \nX2 = "+str(x2))
else:
 print("El coefiente cuadratico debe ser diferente de cero")

